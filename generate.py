#!/usr/bin/env python3
"""Regenera los 10 CSV del repositorio (5 plataformas x 2 idiomas) desde source.json.

Pipeline:
    1. export_jira.py   -> source.json         (Jira = fuente de verdad)
    2. generate.py      -> 10 CSV en 5 carpetas:
                           - jira/      (Jira + Xray / Zephyr Scale)
                           - azure/     (Azure DevOps Test Plans)
                           - testrail/  (TestRail)
                           - qase/      (Qase.io)
                           - gitlab/    (GitLab Test Cases / GitHub Issues MD)

Datos auxiliares:
    - fallback_steps.json   pasos manuales curados de respaldo
    - translations_es.json  traducciones ES indexadas por "action||result"

Uso:
    python3 generate.py          # regenera los 10 CSV
"""
import csv
import json
import os
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


def ensure_dir(folder):
    os.makedirs(folder, exist_ok=True)


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


def labels_for(test, sep=";"):
    lvl = test.get("level")
    kind = "A11Y_AUTO" if test.get("test_type") == "Automated" else "A11Y_MANUAL"
    parts = ["A11Y", lvl, kind] if lvl else ["A11Y", kind]
    return sep.join(parts)


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


def write_csv(path, rows):
    ensure_dir(os.path.dirname(path))
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_ALL).writerows(rows)


def write_jira_csv(path, tests, fallback, trans, lang):
    rows = [["TCID", "Test Summary", "Issue Type", "Test Type", "Priority",
             "Labels", "Description", "Test Repository Path",
             "Step #", "Action", "Data", "Expected Result"]]
    for tcid, test in enumerate(tests, 1):
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        labels = labels_for(test, ";")
        test_type = test.get("test_type") or "Manual"
        desc = description_for(test, lang)
        repo_path = folder_leaf(test, lang)
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
    write_csv(path, rows)


def write_azure_csv(path, tests, fallback, trans, lang):
    base_area = AREA_ES if lang == "es" else AREA_EN
    rows = [["ID", "Work Item Type", "Title", "Test Step", "Step Action",
             "Step Expected", "Step Data", "Description", "Priority",
             "Automation Status", "Area Path", "State", "Tags"]]
    for test in tests:
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        area = f"{base_area}\\{folder_leaf(test, lang)}"
        auto_status = "Automated" if test.get("test_type") == "Automated" else "Not Automated"
        tags = labels_for(test, ";")
        desc = description_for(test, lang)
        rows.append(["", "Test Case", test["title"], "", "", "", "",
                     desc, "2", auto_status, area, "Ready", tags])
        for i, s in enumerate(steps, 1):
            data = s.get("data", "")
            action = f"{s['action']} [{data}]" if data else s["action"]
            rows.append(["", "", "", str(i), action, s["result"], data,
                         "", "", "", "", "", ""])
    write_csv(path, rows)


def write_testrail_csv(path, tests, fallback, trans, lang):
    base_sec = AREA_ES if lang == "es" else AREA_EN
    rows = [["Title", "Section", "Type", "Priority", "References",
             "Automation Type", "Preconditions", "Step", "Additional Info",
             "Expected Result"]]
    for test in tests:
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        section = f"{base_sec} > {folder_leaf(test, lang)}"
        ref = f"WCAG {test['criterion']} ({test['level']})"
        desc = description_for(test, lang)
        for i, s in enumerate(steps, 1):
            first = i == 1
            rows.append([test["title"] if first else "",
                         section if first else "",
                         "Accessibility" if first else "",
                         PRIORITY if first else "",
                         ref if first else "",
                         "None" if first else "",
                         desc if first else "",
                         s["action"], s.get("data", ""), s["result"]])
    write_csv(path, rows)


def write_qase_csv(path, tests, fallback, trans, lang):
    base_suite = AREA_ES if lang == "es" else AREA_EN
    rows = [["v2_id", "title", "description", "preconditions", "postconditions",
             "tags", "priority", "severity", "type", "behavior", "automation",
             "status", "is_flaky", "layer", "milestone", "custom_fields",
             "steps_type", "steps_actions", "steps_result", "steps_data",
             "suite_id", "suite_parent_id", "suite", "suite_without_cases",
             "parameters"]]
    for tcid, test in enumerate(tests, 1):
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        suite = f"{base_suite}\t{folder_leaf(test, lang)}"
        tags = labels_for(test, ",")
        desc = description_for(test, lang)
        for i, s in enumerate(steps, 1):
            first = i == 1
            rows.append([str(tcid) if first else "",
                         test["title"] if first else "",
                         desc if first else "",
                         "", "",
                         tags if first else "",
                         "medium" if first else "",
                         "normal" if first else "",
                         "functional" if first else "",
                         "positive" if first else "",
                         "is-not-automated" if first else "",
                         "actual" if first else "",
                         "no" if first else "",
                         "e2e" if first else "",
                         "", "",
                         "classic" if first else "",
                         s["action"], s["result"], s.get("data", ""),
                         "", "",
                         suite if first else "",
                         "", ""])
    write_csv(path, rows)


def write_gitlab_csv(path, tests, fallback, trans, lang):
    rows = [["Title", "Description"]]
    hdr_step = "Paso" if lang == "es" else "Step"
    hdr_act = "Acción" if lang == "es" else "Action"
    hdr_dat = "Datos / Reglas axe-core" if lang == "es" else "Data / axe-core Rules"
    hdr_res = "Resultado Esperado" if lang == "es" else "Expected Result"
    hdr_chk = "Checklist de Ejecución" if lang == "es" else "Execution Checklist"
    for test in tests:
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        desc = description_for(test, lang)
        principle = folder_leaf(test, lang)
        lvl = test.get("level") or "A"
        lines = [
            f"**WCAG 2.2** - `{test['criterion']}` (Level **{lvl}**) · *{principle}*",
            "",
            f"> {desc}",
            "",
            f"| {hdr_step} | {hdr_act} | {hdr_dat} | {hdr_res} |",
            "| :---: | :--- | :--- | :--- |",
        ]
        for i, s in enumerate(steps, 1):
            dat = f"`{s['data']}`" if s.get("data") else "-"
            lines.append(f"| **{i}** | {s['action']} | {dat} | {s['result']} |")
        lines.append("")
        lines.append(f"### {hdr_chk}")
        for i, s in enumerate(steps, 1):
            lines.append(f"- [ ] **{hdr_step} {i}:** {s['action']} → *{s['result']}*")
        lines.append("")
        lines.append(f"/label ~A11Y ~\"{lvl}\" ~A11Y_MANUAL")
        rows.append([test["title"], "\n".join(lines)])
    write_csv(path, rows)


def main():
    src = load_json(SOURCE)
    fallback = load_json(FALLBACK)
    trans = load_json(TRANSLATIONS)
    tests = [t for t in src["tests"] if t.get("criterion")]
    for lang, suf in (("en", "EN"), ("es", "ES")):
        write_jira_csv(f"jira/A11Y_Repository_Jira_{suf}.csv", tests, fallback, trans, lang)
        write_azure_csv(f"azure/A11Y_Repository_Azure_{suf}.csv", tests, fallback, trans, lang)
        write_testrail_csv(f"testrail/A11Y_Repository_TestRail_{suf}.csv", tests, fallback, trans, lang)
        write_qase_csv(f"qase/A11Y_Repository_Qase_{suf}.csv", tests, fallback, trans, lang)
        write_gitlab_csv(f"gitlab/A11Y_Repository_GitLab_{suf}.csv", tests, fallback, trans, lang)
    print(f"generados 10 CSV (5 plataformas x ES/EN): {len(tests)} test cases cada uno")


if __name__ == "__main__":
    main()
