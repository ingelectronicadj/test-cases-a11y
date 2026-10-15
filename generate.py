#!/usr/bin/env python3
"""Regenera los 4 CSV del repositorio a partir de source.json.

Pipeline:
    1. export_jira.py   -> source.json         (Jira = fuente de verdad)
    2. generate.py      -> 4 CSV               (Azure/Jira x ES/EN)

Datos auxiliares:
    - fallback_steps.json   pasos manuales curados para criterios 'Automated'
                            (los TC automáticos no tienen pasos en Jira)
    - translations_es.json  traducciones ES indexadas por "action||result"

Uso:
    python3 generate.py          # regenera los 4 CSV
"""
import csv
import json
import sys

SOURCE = "source.json"
FALLBACK = "fallback_steps.json"
TRANSLATIONS = "translations_es.json"

PRIORITY = "Medium"
AREA_ES, AREA_EN = "Accesibilidad", "Accessibility"

FOLDER_ES = {
    "1. Perceivable": "1. Perceptible",
    "2. Operable": "2. Operable",
    "3. Understandable": "3. Comprensible",
    "4. Robust": "4. Robusto",
}

GUIDELINE_ES = {
    "1.1 Text Alternatives": "1.1 Alternativas textuales",
    "1.2 Time-based Media": "1.2 Medios tempodependientes",
    "1.3 Adaptable": "1.3 Adaptable",
    "1.4 Distinguishable": "1.4 Distinguible",
    "2.1 Keyboard Accessible": "2.1 Accesible por teclado",
    "2.2 Enough Time": "2.2 Tiempo suficiente",
    "2.3 Seizures and Physical Reactions": "2.3 Convulsiones y reacciones físicas",
    "2.4 Navigable": "2.4 Navegable",
    "2.5 Input Modalities": "2.5 Modalidades de entrada",
    "3.1 Readable": "3.1 Legible",
    "3.2 Predictable": "3.2 Predecible",
    "3.3 Input Assistance": "3.3 Asistencia en la entrada de datos",
    "4.1 Compatible": "4.1 Compatible",
}


def load_json(path):
    return json.load(open(path, encoding="utf-8"))


def folder_leaf(test, lang):
    raw = (test.get("folder") or "").split("/")[-1].strip()
    if not raw:
        c = (test.get("criterion") or "1").split(".")[0]
        raw = {"1": "1. Perceivable", "2": "2. Operable",
               "3": "3. Understandable", "4": "4. Robust"}.get(c, "1. Perceivable")
    return FOLDER_ES.get(raw, raw) if lang == "es" else raw


def description_for(test, lang):
    desc = (test.get("description") or "").strip()
    if lang == "en" or not desc:
        return desc
    out = desc.replace("Guideline ", "Pauta ").replace("Success Criteria:", "Criterio de Conformidad:")
    for en_g, es_g in GUIDELINE_ES.items():
        out = out.replace(f"Pauta {en_g}", f"Pauta {es_g}")
    return out


def labels_for(test):
    lvl = test.get("level")
    kind = "A11Y_AUTO" if test.get("test_type") == "Automated" else "A11Y_MANUAL"
    return f"A11Y;{lvl};{kind}" if lvl else f"A11Y;{kind}"


def steps_en(test, fallback):
    """Pasos en inglés: los de Jira (Manual) o el fallback curado (Automated)."""
    if test["steps"]:
        return test["steps"]
    return fallback.get(test["criterion"], {}).get("en", [])


def steps_es(test, fallback, trans):
    """Pasos en español vía translations_es.json; fallback ES como red."""
    if test["steps"]:
        out = []
        for s in test["steps"]:
            key = s["action"] + "||" + s["result"]
            t = trans.get(key)
            if not t:
                sys.exit(f"falta traduccion ES para: {test['criterion']} | {s['action'][:70]}")
            out.append({"action": t["action"], "data": s.get("data", ""), "result": t["result"]})
        return out
    return fallback.get(test["criterion"], {}).get("es", [])


def write_jira_csv(path, tests, fallback, trans, lang):
    rows = [["TCID", "Test Summary", "Issue Type", "Test Type", "Priority",
             "Labels", "Description", "Test Repository Path",
             "Step #", "Action", "Data", "Expected Result"]]
    tcid = 0
    for test in tests:
        tcid += 1
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        labels = labels_for(test)
        test_type = test.get("test_type") or "Manual"
        desc = description_for(test, lang)
        repo_path = folder_leaf(test, lang)
        if not steps:
            rows.append([str(tcid), test["title"], "Test", test_type, PRIORITY,
                         labels, desc, repo_path, "", "", "", ""])
            continue
        for i, s in enumerate(steps, 1):
            first = i == 1
            rows.append([str(tcid) if first else "",
                         test["title"] if first else "",
                         "Test" if first else "",
                         test_type if first else "",
                         PRIORITY if first else "",
                         labels if first else "",
                         desc if first else "",
                         repo_path if first else "",
                         str(i), s["action"], s.get("data", ""), s["result"]])
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_ALL).writerows(rows)


def write_azure_csv(path, tests, fallback, trans, lang):
    base_area = AREA_ES if lang == "es" else AREA_EN
    rows = [["ID", "Work Item Type", "Title", "Test Step", "Step Action",
             "Step Expected", "Step Data", "Description", "Priority",
             "Automation Status", "Area Path", "State", "Tags"]]
    for test in tests:
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        area = f"{base_area}\\{folder_leaf(test, lang)}"
        auto_status = "Automated" if test.get("test_type") == "Automated" else "Not Automated"
        tags = labels_for(test)
        desc = description_for(test, lang)
        rows.append(["", "Test Case", test["title"], "", "", "", "",
                     desc, "2", auto_status, area, "Ready", tags])
        for i, s in enumerate(steps, 1):
            data = s.get("data", "")
            action = f"{s['action']} [{data}]" if data else s["action"]
            rows.append(["", "", "", str(i), action, s["result"], data,
                         "", "", "", "", "", ""])
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_ALL).writerows(rows)


def main():
    src = load_json(SOURCE)
    fallback = load_json(FALLBACK)
    trans = load_json(TRANSLATIONS)
    tests = [t for t in src["tests"] if t.get("criterion")]
    write_jira_csv("A11Y_Repository_Jira_EN.csv", tests, fallback, trans, "en")
    write_jira_csv("A11Y_Repository_Jira_ES.csv", tests, fallback, trans, "es")
    write_azure_csv("A11Y_Repository_Azure_EN.csv", tests, fallback, trans, "en")
    write_azure_csv("A11Y_Repository_Azure_ES.csv", tests, fallback, trans, "es")
    print(f"generados 4 CSV: {len(tests)} test cases")


if __name__ == "__main__":
    main()
