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


def load_json(path):
    return json.load(open(path, encoding="utf-8"))


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
            out.append(t)
        return out
    return fallback.get(test["criterion"], {}).get("es", [])


def write_jira_csv(path, tests, fallback, trans, lang):
    rows = [["TCID", "Test Summary", "Issue Type", "Priority", "Labels",
             "Step #", "Action", "Data", "Expected Result"]]
    tcid = 0
    for test in tests:
        tcid += 1
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        labels = f"A11Y;{test['level']}" if test["level"] else "A11Y"
        if not steps:
            rows.append([str(tcid), test["title"], "Test", PRIORITY, labels,
                         "", "", "", ""])
            continue
        for i, s in enumerate(steps, 1):
            first = i == 1
            rows.append([str(tcid) if first else "",
                         test["title"] if first else "",
                         "Test" if first else "",
                         PRIORITY if first else "",
                         labels if first else "",
                         str(i), s["action"], s.get("data", ""), s["result"]])
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.writer(f, quoting=csv.QUOTE_ALL).writerows(rows)


def write_azure_csv(path, tests, fallback, trans, lang):
    area = AREA_ES if lang == "es" else AREA_EN
    rows = [["ID", "Work Item Type", "Title", "Test Step", "Step Action",
             "Step Expected", "Automation Status", "Area Path", "State", "Tags"]]
    for test in tests:
        steps = steps_en(test, fallback) if lang == "en" else steps_es(test, fallback, trans)
        rows.append(["", "Test Case", test["title"], "", "", "",
                     "Not Automated", area, "Ready", "A11Y"])
        for i, s in enumerate(steps, 1):
            rows.append(["", "", "", str(i), s["action"], s["result"], "", "", ""])
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
