<div align="center">

# ♿ WCAG 2.2 Accessibility Test Cases Repository

### **El repositorio definitivo de casos de prueba de accesibilidad web (WCAG 2.2) listo para importar en un clic**
*The ultimate, production-ready WCAG 2.2 test case suite for QA Engineers, Accessibility Auditors & Engineering Teams*

[![WCAG 2.2](https://img.shields.io/badge/WCAG-2.2_W3C_Recommendation-005A9C?style=for-the-badge&logo=w3c&logoColor=white)](https://www.w3.org/TR/WCAG22/)
[![Test Cases](https://img.shields.io/badge/Test_Cases-87%2F87_(A%20%C2%B7%20AA%20%C2%B7%20AAA)-2EA043?style=for-the-badge)](#%EF%B8%8F-cobertura-wcag-22--wcag-22-coverage)
[![Test Steps](https://img.shields.io/badge/Test_Steps-187_Curated_Steps-7048E8?style=for-the-badge)](#-descarga-rápida-por-plataforma--quick-download-by-platform)
[![axe-core](https://img.shields.io/badge/axe--core-Rules_Mapped-D9381E?style=for-the-badge)](https://github.com/dequelabs/axe-core)
[![Languages](https://img.shields.io/badge/Languages-ES_%F0%9F%87%AA%F0%9F%87%B8_%7C_EN_%F0%9F%87%BA%F0%9F%87%B8-F59E0B?style=for-the-badge)](#-descarga-rápida-por-plataforma--quick-download-by-platform)
[![License: MIT](https://img.shields.io/badge/License-MIT-111827?style=for-the-badge)](./LICENSE)

<br />

[![GitHub stars](https://img.shields.io/github/stars/ingelectronicadj/test-cases-a11y?style=social)](https://github.com/ingelectronicadj/test-cases-a11y/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ingelectronicadj/test-cases-a11y?style=social)](https://github.com/ingelectronicadj/test-cases-a11y/network/members)

[**🚀 Descargar CSVs**](#-descarga-rápida-por-plataforma--quick-download-by-platform) · [**🧭 Cobertura WCAG 2.2**](#%EF%B8%8F-cobertura-wcag-22--wcag-22-coverage) · [**📖 Guías de Importación**](#-guías-de-importación-paso-a-paso--step-by-step-import-guides) · [**⚙️ Pipeline de Generación**](#%EF%B8%8F-arquitectura-y-pipeline--architecture--pipeline)

</div>

---

## ✨ ¿Por qué usar este repositorio? / Why this repository?

Construir desde cero un repositorio de pruebas de accesibilidad en **Jira**, **Azure DevOps**, **TestRail**, **Qase** o **GitLab** lleva semanas de redacción, clasificación y traducción. Este proyecto te entrega un **catálogo curado en producción bancaria** con **paridad 1:1** entre plataformas e idiomas:

| Característica / Feature | Qué incluye / What's inside |
| :--- | :--- |
| 🎯 **100% Cobertura WCAG 2.2** | Los **87 criterios de conformidad** (`32 A` · `24 AA` · `31 AAA`), incluyendo los nuevos de WCAG 2.2 (`2.4.11`, `2.4.12`, `2.4.13`, `2.5.7`, `2.5.8`, `3.2.6`, `3.3.7`, `3.3.8`, `3.3.9`). |
| 🧪 **187 Pasos de Experto** | Cada criterio cuenta con **2 a 4 pasos manuales accionables** (`Action` + `Expected Result`), redactados para validación con teclado, lector de pantalla, zoom/reflow e inspector DOM. |
| 🤖 **Mapeo Híbrido `axe-core`** | Los criterios con cobertura automática incluyen en su campo `Data` las **reglas exactas de `axe-core`** y su etiqueta (`axe-core (wcag131): list, td-headers-attr...`). |
| 🗂️ **Jerarquía de Carpetas Lista** | Cada archivo incluye la ruta de carpeta por principio WCAG (`1. Perceivable`, `2. Operable`, `3. Understandable`, `4. Robust`) para que tu herramienta cree el árbol automáticamente al importar. |
| 🌍 **Bilingüe Nativo (ES / EN)** | Todos los pasos, descripciones de pautas y rutas de carpetas están disponibles en **Español** e **Inglés** manteniendo los títulos internacionales del estándar W3C. |
| 🔄 **Single Source of Truth** | Generado desde `source.json` mediante `generate.py`: **cero deriva** entre plataformas o idiomas. |

---

## 🚀 Descarga Rápida por Plataforma / Quick Download by Platform

Todos los archivos contienen exactamente los **87 Test Cases** y **187 pasos** con paridad 1:1:

| Plataforma / Platform | 🇪🇸 Español (CSV) | 🇺🇸 English (CSV) | Soporta Carpetas | Soporta Tags / Nivel | Reglas `axe-core` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Jira (Xray / Zephyr Scale)** | [**📥 `Jira_ES.csv`**](./jira/A11Y_Repository_Jira_ES.csv) | [**📥 `Jira_EN.csv`**](./jira/A11Y_Repository_Jira_EN.csv) | ✅ `Test Repository Path` | ✅ `A11Y;AA;A11Y_MANUAL` | ✅ Columna `Data` |
| **Azure DevOps Test Plans** | [**📥 `Azure_ES.csv`**](./azure/A11Y_Repository_Azure_ES.csv) | [**📥 `Azure_EN.csv`**](./azure/A11Y_Repository_Azure_EN.csv) | ✅ `Area Path` | ✅ `A11Y;AA;A11Y_MANUAL` | ✅ `Step Action` + `Step Data` |
| **TestRail** | [**📥 `TestRail_ES.csv`**](./testrail/A11Y_Repository_TestRail_ES.csv) | [**📥 `TestRail_EN.csv`**](./testrail/A11Y_Repository_TestRail_EN.csv) | ✅ `Section Hierarchy` | ✅ `References` (`WCAG X.Y.Z`) | ✅ `Additional Info` |
| **Qase.io** | [**📥 `Qase_ES.csv`**](./qase/A11Y_Repository_Qase_ES.csv) | [**📥 `Qase_EN.csv`**](./qase/A11Y_Repository_Qase_EN.csv) | ✅ `suite` | ✅ `tags` | ✅ `steps_data` |
| **GitLab / GitHub Issues** | [**📥 `GitLab_ES.csv`**](./gitlab/A11Y_Repository_GitLab_ES.csv) | [**📥 `GitLab_EN.csv`**](./gitlab/A11Y_Repository_GitLab_EN.csv) | ✅ Badge en Markdown | ✅ `/label ~A11Y ~AA` | ✅ Tabla + Checklist `- [ ]` |

---

## 🏷️ Convención de Nombres y Estructura / Naming Convention & Anatomy

Cada caso de prueba sigue una nomenclatura internacional consistente para facilitar el filtrado por JQL / WIQL / búsqueda rápida:

```text
TC - [A11Y] - {Guideline Number} {Guideline Name} - {Criterion Number} {Criterion Name}
```

**Ejemplo real del repositorio / Live example:**

```text
Title:       TC - [A11Y] - 1.4 Distinguishable - 1.4.3 Contrast (Minimum)
Folder:      1. Perceivable (EN)  |  1. Perceptible (ES)
Labels/Tags: A11Y;AA;A11Y_MANUAL
Description: Guideline 1.4 Distinguishable. Success Criteria: 1.4.3 Contrast (Minimum) (Level AA)
Step 1:      Verify contrast in all states (normal, hover, focus, disabled)
  ├─ Data:   axe-core (wcag143): color-contrast
  └─ Result: All interactive element states must meet required contrast ratios (4.5:1 normal, 3:1 large text)
Step 2:      Review text over images or gradient backgrounds
  └─ Result: Overlaid text must have sufficient contrast throughout or use shadows/overlays
```

---

## 🗺️ Cobertura WCAG 2.2 / WCAG 2.2 Coverage

| Principio / Principle | Pautas / Guidelines | Test Cases | Nivel A | Nivel AA | Nivel AAA | Pasos Totales |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Perceivable / Perceptible** | `1.1` – `1.4` | **29** | 9 | 7 | 13 | 62 |
| **2. Operable / Operable** | `2.1` – `2.5` | **34** | 14 | 8 | 12 | 72 |
| **3. Understandable / Comprensible** | `3.1` – `3.3` | **21** | 7 | 7 | 7 | 46 |
| **4. Robust / Robusto** | `4.1` | **3** | 2 | 1 | 0 | 7 |
| **TOTAL WCAG 2.2** | **13 Pautas** | **87 Criterios** | **32** | **24** | **31** | **187 Pasos** |

> 💡 **Conformidad habitual en la industria (EN 301 549 / Section 508 / EAA / ADA):** Filtra por las etiquetas `A` y `AA` tras importar para obtener los **56 criterios obligatorios AA**, o incluye `AAA` para auditorías de excelencia. *(Se incluye `4.1.1 Parsing` como referencia para compatibilidad con auditorías legacy).*

---

## 📖 Guías de Importación Paso a Paso / Step-by-Step Import Guides

Haz clic en tu plataforma para desplegar las instrucciones de mapeo de columnas:

<details open>
<summary><b>🟦 1. Jira — Xray Test Case Importer & Zephyr Scale</b></summary>
<br />

**Archivos:** [`jira/A11Y_Repository_Jira_ES.csv`](./jira/A11Y_Repository_Jira_ES.csv) · [`jira/A11Y_Repository_Jira_EN.csv`](./jira/A11Y_Repository_Jira_EN.csv)

**Columnas incluidas (12):**
`TCID, Test Summary, Issue Type, Test Type, Priority, Labels, Description, Test Repository Path, Step #, Action, Data, Expected Result`

#### Pasos en Xray (Jira Cloud / Data Center):
1. Ve a **Testing Board** → **Test Repository** → menú **Import** → **Test Case Importer (CSV)**.
2. Selecciona `jira/A11Y_Repository_Jira_ES.csv` (o `EN.csv`) con delimitador `,` y codificación `UTF-8`.
3. Mapea los campos:
   - `TCID` → **Test Case Identifier** *(imprescindible para agrupar los pasos de cada TC)*
   - `Test Summary` → **Summary**
   - `Issue Type` → **Issue Type** (`Test`)
   - `Test Type` → **Test Type** (`Manual`)
   - `Priority` → **Priority** (`Medium`)
   - `Labels` → **Labels** (marca el separador `;`)
   - `Description` → **Description**
   - `Test Repository Path` → **Test Repository Path** *(crea las 4 carpetas por principio)*
   - `Action` → **Step Action**
   - `Data` → **Step Data**
   - `Expected Result` → **Step Expected Result**
4. Ejecuta la importación: obtendrás los **87 Test Cases** organizados en sus 4 carpetas.

</details>

<details>
<summary><b>🔷 2. Azure DevOps — Test Plans</b></summary>
<br />

**Archivos:** [`azure/A11Y_Repository_Azure_ES.csv`](./azure/A11Y_Repository_Azure_ES.csv) · [`azure/A11Y_Repository_Azure_EN.csv`](./azure/A11Y_Repository_Azure_EN.csv)

**Columnas incluidas (13):**
`ID, Work Item Type, Title, Test Step, Step Action, Step Expected, Step Data, Description, Priority, Automation Status, Area Path, State, Tags`

#### Pasos en Azure DevOps:
1. Antes de importar, reemplaza en el CSV el prefijo de `Area Path` (`Accesibilidad\...` o `Accessibility\...`) por el nombre del área raíz de tu proyecto si fuera necesario.
2. Ve a **Test Plans** → **Test Suites** → clic en el icono de importar CSV (**Import test cases from CSV**).
3. Sube el archivo `azure/A11Y_Repository_Azure_ES.csv` (o `EN.csv`) y confirma.

</details>

<details>
<summary><b>🟩 3. TestRail</b></summary>
<br />

**Archivos:** [`testrail/A11Y_Repository_TestRail_ES.csv`](./testrail/A11Y_Repository_TestRail_ES.csv) · [`testrail/A11Y_Repository_TestRail_EN.csv`](./testrail/A11Y_Repository_TestRail_EN.csv)

**Columnas incluidas (10):**
`Title, Section, Type, Priority, References, Automation Type, Preconditions, Step, Additional Info, Expected Result`

#### Pasos en TestRail:
1. Abre tu proyecto en TestRail → **Test Cases** → icono **Import Cases** → **Import from CSV**.
2. Sube el archivo y elige la opción **"Test cases use multiple rows"** detectando un nuevo caso cuando cambia `Title`.
3. Mapea `Section` a **Section Hierarchy** (usa `>` para crear `Accessibility > 1. Perceivable`) y `Step / Additional Info / Expected Result` a tu plantilla de **Separated Steps**.

</details>

<details>
<summary><b>🟪 4. Qase (`qase.io`)</b></summary>
<br />

**Archivos:** [`qase/A11Y_Repository_Qase_ES.csv`](./qase/A11Y_Repository_Qase_ES.csv) · [`qase/A11Y_Repository_Qase_EN.csv`](./qase/A11Y_Repository_Qase_EN.csv)

#### Pasos en Qase:
1. Ve a tu repositorio en Qase → **Repository** → **Import** → selecciona **Qase CSV**.
2. Sube `qase/A11Y_Repository_Qase_ES.csv` (o `EN.csv`). El formato utiliza las 25 columnas oficiales de Qase v2 (`v2_id`, `suite`, `steps_actions`, `steps_data`, `steps_result`, `tags`) por lo que se importa directamente sin mapeo manual.

</details>

<details>
<summary><b>🟧 5. GitLab Test Cases / GitHub Issues (Markdown + Checklists)</b></summary>
<br />

**Archivos:** [`gitlab/A11Y_Repository_GitLab_ES.csv`](./gitlab/A11Y_Repository_GitLab_ES.csv) · [`gitlab/A11Y_Repository_GitLab_EN.csv`](./gitlab/A11Y_Repository_GitLab_EN.csv)

#### Pasos en GitLab:
1. Ve a **Build → Test cases** (o **Plan → Issues**) → botón **Import CSV**.
2. Sube el archivo: cada uno de los 87 criterios se creará con una tabla Markdown de pasos, las reglas `axe-core`, una **checklist interactiva `- [ ]`** y la acción rápida `/label ~A11Y ~AA ~A11Y_MANUAL`.

</details>

---

## ⚙️ Arquitectura y Pipeline / Architecture & Pipeline

```text
test-cases-a11y/
├── jira/                              # Jira + Xray / Zephyr Scale (ES & EN)
│   ├── A11Y_Repository_Jira_ES.csv
│   └── A11Y_Repository_Jira_EN.csv
├── azure/                             # Azure DevOps Test Plans (ES & EN)
│   ├── A11Y_Repository_Azure_ES.csv
│   └── A11Y_Repository_Azure_EN.csv
├── testrail/                          # TestRail (ES & EN)
│   ├── A11Y_Repository_TestRail_ES.csv
│   └── A11Y_Repository_TestRail_EN.csv
├── qase/                              # Qase.io v2 (ES & EN)
│   ├── A11Y_Repository_Qase_ES.csv
│   └── A11Y_Repository_Qase_EN.csv
├── gitlab/                            # GitLab Test Cases & GitHub Issues (ES & EN)
│   ├── A11Y_Repository_GitLab_ES.csv
│   └── A11Y_Repository_GitLab_EN.csv
├── source.json                        # Fuente única de verdad (87 TCs / 187 pasos)
├── translations_es.json               # Diccionario curado EN -> ES (192 entradas)
├── fallback_steps.json                # Espejo de pasos base por criterio
├── export_jira.py                     # Extractor desde Jira/Xray Cloud GraphQL
├── generate.py                        # Compilador multi-plataforma (emite los 10 CSV)
└── CHANGELOG.md                       # Historial de versiones (SemVer)
```

### Regenerar los 10 CSVs desde la fuente de verdad

Nunca edites los CSV a mano. Si modificas un paso en `source.json` o una traducción en `translations_es.json`, ejecuta:

```bash
python3 generate.py
# -> generados 10 CSV (5 plataformas x ES/EN): 87 test cases cada uno
```

*(Si falta una traducción en español para cualquier paso, `generate.py` detiene la compilación indicando el criterio y texto exacto).*

---

## 🤝 Contribuciones y Comunidad / Contributing

Las mejoras en la redacción de pasos, nuevas plataformas de Test Management o nuevos idiomas son bienvenidas:

1. Haz un **Fork** del repositorio.
2. Edita `source.json` / `translations_es.json` o añade un nuevo exportador en `generate.py`.
3. Ejecuta `python3 generate.py` para regenerar los artefactos en bloque.
4. Abre un **Pull Request**.

---

<div align="center">

### ⭐ ¿Te ha ahorrado horas de trabajo este repositorio? / Did this save you hours of work?

Si este catálogo te resulta útil para tus auditorías o tu equipo de QA, **dale una estrella ⭐ arriba a la derecha** y compártelo con tu comunidad de accesibilidad.

**Hecho con rigor WCAG por [Diego Mena](https://github.com/ingelectronicadj)** · Licencia [MIT](./LICENSE)

</div>
