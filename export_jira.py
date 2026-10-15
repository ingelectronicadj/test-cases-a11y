#!/usr/bin/env python3
"""Exporta el test repository canónico de accesibilidad desde Jira/Xray a source.json.

Fuente de verdad: TCs de accesibilidad en Jira/Xray con summary "TC - [A11y]".
Genera el insumo anonimizado y canónico que consume generate.py para
reconstruir los 10 CSV multi-plataforma.

Uso:
    export JIRA_URL JIRA_EMAIL JIRA_API_TOKEN XRAY_CLIENT_ID XRAY_CLIENT_SECRET
    export JIRA_JQL='issuetype=Test AND summary ~ "TC - [A11y]" AND status != Dropped'  # opcional
    python3 export_jira.py
"""
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request

DEFAULT_JQL = 'issuetype=Test AND summary ~ "TC - [A11y]" AND status != Dropped'
JIRA = os.environ.get("JIRA_URL", "").rstrip("/")
XRAY = os.environ.get("XRAY_URL", "https://xray.cloud.getxray.app").rstrip("/")
JQL = os.environ.get("JIRA_JQL", DEFAULT_JQL)

ALLOWED_LABELS = {
    "A", "AA", "AAA", "A11Y", "A11Y_AUTO", "A11Y_MANUAL",
    "A11Y_AUDIO_VIDEO", "A11Y_COGNITIVE", "A11Y_COLOR_CONTRAST",
    "A11Y_DESIGN", "A11Y_FOCUS", "A11Y_FORMS", "A11Y_HEADINGS",
    "A11Y_IMG", "A11Y_KEYBOARD", "A11Y_LANDMARKS", "A11Y_LANGUAGE",
    "A11Y_LINKS", "A11Y_MOBILE", "A11Y_MODALS", "A11Y_NAVIGATION",
    "A11Y_PAGE_TITLE", "A11Y_PARSING", "A11Y_POINTER", "A11Y_RESIZE",
    "A11Y_SCREENREADERS", "A11Y_SEIZURES", "A11Y_SEMANTICS",
    "A11Y_TABLES", "A11Y_TIMING", "A11Y_ZOOM",
}


def die(msg):
    sys.exit(f"error: {msg}")


def jira_search(jql, fields):
    out, tok = [], None
    while True:
        body = {"jql": jql, "maxResults": 100, "fields": fields.split(",")}
        if tok:
            body["nextPageToken"] = tok
        req = urllib.request.Request(
            f"{JIRA}/rest/api/3/search/jql", data=json.dumps(body).encode(),
            method="POST", headers={
                "Authorization": basic, "Accept": "application/json",
                "Content-Type": "application/json"})
        with urllib.request.urlopen(req) as r:
            d = json.loads(r.read().decode())
        out += d.get("issues", [])
        tok = d.get("nextPageToken")
        if not tok or d.get("isLast"):
            break
    return out


def jira_issue(key, fields):
    req = urllib.request.Request(
        f"{JIRA}/rest/api/3/issue/{key}?fields={fields}",
        headers={"Authorization": basic})
    return json.loads(urllib.request.urlopen(req).read().decode())


def xray_auth():
    body = json.dumps({"client_id": os.environ["XRAY_CLIENT_ID"],
                       "client_secret": os.environ["XRAY_CLIENT_SECRET"]}).encode()
    req = urllib.request.Request(f"{XRAY}/api/v2/authenticate", data=body,
                                 headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(req).read().decode().strip('"')


def gql(query):
    req = urllib.request.Request(
        f"{XRAY}/api/v2/graphql", data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"Bearer {xray_token}",
                 "Content-Type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req).read().decode())
    except urllib.error.HTTPError as e:
        die(f"graphql {e.code}: {e.read().decode()[:300]}")


def adf_text(node):
    if not node:
        return ""
    return " ".join(c.get("text", "")
                    for n in node.get("content", [])
                    for c in n.get("content", []))


def criterion(summary):
    m = re.search(r"(\d\.\d\.\d+)", summary)
    return m.group(1) if m else None


for var in ("JIRA_URL", "JIRA_EMAIL", "JIRA_API_TOKEN", "XRAY_CLIENT_ID", "XRAY_CLIENT_SECRET"):
    if not os.environ.get(var):
        die(f"falta la variable de entorno {var}")

basic = "Basic " + base64.b64encode(
    f"{os.environ['JIRA_EMAIL']}:{os.environ['JIRA_API_TOKEN']}".encode()).decode()
xray_token = xray_auth()

issues = jira_search(JQL, "summary,status,labels,description")
keys = [i["key"] for i in issues]
meta = {}
for i in issues:
    f = i["fields"]
    clean_summary = f["summary"].replace("\xa0", " ").replace("  ", " ").strip()
    meta[i["key"]] = {
        "summary": clean_summary,
        "status": f["status"]["name"],
        "labels": f["labels"],
        "description": adf_text(f.get("description")).replace("\xa0", " ").strip(),
        "criterion": criterion(clean_summary),
    }

# Datos Xray (tipo, pasos, definition, carpeta) en bloques de 50
xray = {}
for i in range(0, len(keys), 50):
    ks = ",".join(keys[i:i + 50])
    r = gql('{ getTests(jql:"key in (%s)", limit:100){ results{ '
            'jira(fields:["key"]) testType{name} steps{action data result} '
            'unstructured folder{path} } } }' % ks)
    for t in (r.get("data") or {}).get("getTests", {}).get("results", []):
        xray[t["jira"]["key"]] = t

out = []
for k in keys:
    m = meta[k]
    t = xray.get(k, {})
    labels = [l for l in m["labels"] if l in ALLOWED_LABELS]
    level = next((l for l in labels if l in ("A", "AA", "AAA")), None)
    raw_folder = (t.get("folder") or {}).get("path") or ""
    leaf_folder = raw_folder.split("/")[-1].strip()
    canonical_folder = f"/ACCESSIBILITY/{leaf_folder}" if leaf_folder else "/ACCESSIBILITY"
    out.append({
        "key": k,
        "criterion": m["criterion"],
        "title": m["summary"],
        "status": m["status"],
        "level": level,
        "test_type": (t.get("testType") or {}).get("name"),
        "labels": labels,
        "folder": canonical_folder,
        "description": m["description"],
        "steps": [{"action": s.get("action") or "",
                   "data": s.get("data") or "",
                   "result": s.get("result") or ""}
                  for s in (t.get("steps") or [])],
        "automated_definition": (t.get("unstructured") or "").strip() or None,
    })

out.sort(key=lambda x: [int(p) for p in x["criterion"].split(".")] if x["criterion"] else [99])
for idx, item in enumerate(out, 1):
    item["key"] = f"A11Y-{idx:03d}"

with open("source.json", "w", encoding="utf-8") as f:
    json.dump({"source": "jira", "jql": DEFAULT_JQL, "tests": out},
              f, ensure_ascii=False, indent=2)

n_manual = sum(1 for t in out if t["test_type"] == "Manual")
n_auto = sum(1 for t in out if t["test_type"] == "Automated")
print(f"source.json: {len(out)} tests "
      f"({n_manual} manual, {n_auto} automated), "
      f"{len({t['criterion'] for t in out})} criterios")
missing = [t["key"] for t in out if t["test_type"] == "Manual" and not t["steps"]]
if missing:
    print("aviso: manuales sin pasos:", missing)
