# Changelog

Todos los cambios relevantes de este repositorio se documentan en este archivo.
El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/) y el
versionado [SemVer](https://semver.org/lang/es/).

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
