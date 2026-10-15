# Changelog

Todos los cambios relevantes de este repositorio se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/) y el
versionado [SemVer](https://semver.org/lang/es/).

## [1.2.0] - 2026-10-15

Paridad 1:1 completa entre el repositorio canónico en Jira/Xray
(`WEALTH-GLOBAL/ACCESSIBILITY`) y los 4 archivos CSV.

### Añadido

- **Unificación de los 87 TCs como `Manual` con pasos completos en Jira/Xray y CSV**:
  los 26 criterios que estaban como `Automated` sin tabla de pasos en Xray pasan a
  `Manual` con 2 pasos detallados cada uno (incrementando el total de **166 → 187 pasos**),
  conservando en la columna `Data` del primer paso sus reglas y etiquetas `axe-core`
  (`axe-core (wcagXXX): ...`).
- **Nuevas columnas de paridad 1:1 en `A11Y_Repository_Jira_*.csv`**:
  - `Test Type` (`Manual`)
  - `Description` (pauta y criterio WCAG en inglés en `EN.csv` y en español en `ES.csv`)
  - `Test Repository Path` (`1. Perceivable`..`4. Robust` en EN / `1. Perceptible`..`4. Robusto` en ES)
  - `Labels` enriquecidos (`A11Y;<Nivel>;A11Y_MANUAL`)
  - `Data` poblado con las reglas `axe-core` de cada criterio aplicable
- **Paridad 1:1 también en `A11Y_Repository_Azure_*.csv` (ES y EN)**:
  - Añadidas las columnas `Description`, `Priority` (`"2"`) y `Step Data` (además de embeber `[axe-core ...]` en `Step Action` cuando aplica).
  - `Area Path` jerárquico por principio WCAG (`Accesibilidad\1. Perceptible` en ES / `Accessibility\1. Perceivable` en EN).
  - `Tags` completos (`A11Y;<Nivel>;A11Y_MANUAL`), idénticos a las etiquetas de Jira.
- `translations_es.json` ampliado de **171 a 192 traducciones ES**.

### Cambiado

- Normalizados los espacios de no separación (`\u00a0`) a espacios ASCII estándar
  en los 86 títulos de Jira, `source.json` y los 4 CSV.
- Actualizado `README.md` con las nuevas columnas de Xray/Azure y corregidas las
  referencias residuales de 86 a 87 test cases.

## [1.1.0] - 2025-10-13

Refinamiento del test repository canónico en Jira (proyecto RD, carpeta
`WEALTH-GLOBAL/ACCESSIBILITY`) y alineación de los CSV con Jira como fuente
única de verdad.

### Added

- Criterio **3.3.9 Accessible Authentication (Enhanced)** — nivel AAA
- Criterio **2.5.5 Target Size (Enhanced)** — nivel AAA
- Pipeline de regeneración: `export_jira.py` → `source.json` → `generate.py` → 4 CSV
- `source.json`: export de los 87 TCs canónicos (tipo, pasos, labels, carpeta)
- `fallback_steps.json`: pasos manuales curados para los 26 criterios ejecutados
  por automatización (axe-core), que no llevan pasos en Jira
- `translations_es.json`: 171 traducciones ES indexadas por `action||result`
- `.gitignore`

### Changed

- CSVs regenerados desde el repositorio canónico de Jira: **102 → 166 pasos**
  de prueba en total (61 criterios enriquecidos, 0 criterios con pérdida)
- `generate.py` falla de forma explícita si un paso no tiene traducción ES
- README: 86 → 87 criterios, tabla de cobertura actualizada (Operable 33 → 34),
  nueva sección *Pipeline de Regeneración*

### Removed

- `__pycache__/`: bytecode compilado de scripts de traducción antiguos sin
  código fuente en el repo

## [1.0.0] - 2025

### Added

- Repositorio inicial: 86 criterios WCAG 2.2 en 4 CSV
  (Azure DevOps / Jira × ES/EN)
