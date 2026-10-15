# Changelog

Todos los cambios relevantes de este repositorio se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/) y el
versionado [SemVer](https://semver.org/lang/es/).

## [2.0.0] - 2026-10-15

Reorganización en carpetas por plataforma, soporte para **5 gestores de casos de prueba** (10 CSVs bilingües ES/EN) y paridad 1:1 completa con el repositorio canónico en Jira/Xray.

### Añadido

- **Organización limpia en 5 subcarpetas por plataforma (`jira/`, `azure/`, `testrail/`, `qase/`, `gitlab/`)**:
  - `jira/A11Y_Repository_Jira_ES.csv` y `EN.csv` (Jira + Xray / Zephyr Scale)
  - `azure/A11Y_Repository_Azure_ES.csv` y `EN.csv` (Azure DevOps Test Plans)
  - `testrail/A11Y_Repository_TestRail_ES.csv` y `EN.csv` (TestRail con jerarquía de secciones y referencias WCAG)
  - `qase/A11Y_Repository_Qase_ES.csv` y `EN.csv` (Qase.io formato oficial v2)
  - `gitlab/A11Y_Repository_GitLab_ES.csv` y `EN.csv` (GitLab Test Cases / GitHub Issues con tablas Markdown, checklists `- [ ]` y etiquetas rápidas `/label`)
- **Unificación de los 87 TCs como `Manual` con pasos completos en Jira/Xray y CSV**:
  los 26 criterios que estaban como `Automated` sin tabla de pasos en Xray pasan a
  `Manual` con 2 pasos detallados cada uno (incrementando el total de **166 → 187 pasos**),
  conservando en la columna `Data` del primer paso sus reglas y etiquetas `axe-core`
  (`axe-core (wcagXXX): ...`).
- **Paridad 1:1 de metadatos en todas las plataformas (ES y EN)**:
  - `Test Type` (`Manual`), `Priority`, `Description` bilingüe, carpeta por principio WCAG (`1. Perceivable`..`4. Robust` / `1. Perceptible`..`4. Robusto`), etiquetas completas (`A11Y;<Nivel>;A11Y_MANUAL`) y reglas `axe-core`.
- `translations_es.json` ampliado de **171 a 192 traducciones ES**.

### Cambiado

- Rediseño integral de `README.md` con insignias, matriz de descarga rápida para las 5 plataformas, anatomía de un caso de prueba, desglose por principio/nivel y guías de importación desplegables (`<details>`).
- Normalizados los espacios de no separación (`\u00a0`) a espacios ASCII estándar en los 86 títulos de Jira, `source.json` y los 10 CSV.

### Eliminado

- Eliminados los 4 archivos CSV sueltos de la raíz en favor de las carpetas `jira/` y `azure/`.

## [1.1.0] - 2025-10-13

Refinamiento del test repository canónico en Jira (proyecto RD, carpeta
`WEALTH-GLOBAL/ACCESSIBILITY`) y alineación de los CSV con Jira como fuente
única de verdad.

### Añadido

- Criterio **3.3.9 Accessible Authentication (Enhanced)** — nivel AAA
- Criterio **2.5.5 Target Size (Enhanced)** — nivel AAA
- Pipeline de regeneración: `export_jira.py` → `source.json` → `generate.py` → 4 CSV
- `source.json`: exportación de los 87 TCs canónicos (tipo, pasos, etiquetas, carpeta)
- `fallback_steps.json`: pasos manuales curados para los 26 criterios ejecutados
  por automatización (axe-core), que no llevaban pasos en Jira
- `translations_es.json`: 171 traducciones ES indexadas por `action||result`
- `.gitignore`

### Cambiado

- CSVs regenerados desde el repositorio canónico de Jira: **102 → 166 pasos**
  de prueba en total (61 criterios enriquecidos, 0 criterios con pérdida)
- `generate.py` falla de forma explícita si un paso no tiene traducción ES
- `README.md`: 86 → 87 criterios, tabla de cobertura actualizada (Operable 33 → 34),
  nueva sección *Pipeline de Regeneración*

### Eliminado

- `__pycache__/`: bytecode compilado de scripts de traducción antiguos sin
  código fuente en el repositorio

## [1.0.0] - 2025

### Añadido

- Repositorio inicial: 86 criterios WCAG 2.2 en 4 CSV
  (Azure DevOps / Jira × ES/EN)
