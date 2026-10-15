# WCAG 2.2 Test Cases - Azure DevOps & Jira (Xray / Zephyr)

Repositorio estandarizado con **87 casos de prueba** basados en los criterios de accesibilidad **WCAG 2.2**, listos para importación masiva en **Azure DevOps Test Plans** y **Jira** (compatible con Xray y Zephyr Scale).

Standardized repository with **87 test cases** based on **WCAG 2.2** accessibility criteria, ready for bulk import into **Azure DevOps Test Plans** and **Jira** (compatible with Xray and Zephyr Scale).

## Archivos Disponibles / Available Files

| Archivo / File                 | Plataforma / Platform      | Idioma / Language |
| ------------------------------ | -------------------------- | ----------------- |
| `A11Y_Repository_Azure_ES.csv` | Azure DevOps Test Plans    | 🇪🇸 Español        |
| `A11Y_Repository_Azure_EN.csv` | Azure DevOps Test Plans    | 🇺🇸 English        |
| `A11Y_Repository_Jira_ES.csv`  | Jira + Xray / Zephyr Scale | 🇪🇸 Español        |
| `A11Y_Repository_Jira_EN.csv`  | Jira + Xray / Zephyr Scale | 🇺🇸 English        |

Los cuatro archivos contienen los **mismos 87 criterios WCAG 2.2** (Niveles A, AA y AAA) con **1-4 pasos de prueba** cada uno. Selecciona el archivo según tu plataforma e idioma preferido.

All four files contain the **same 87 WCAG 2.2 criteria** (Levels A, AA, and AAA) with **1-4 test steps** each. Select the file based on your platform and preferred language.

### Nomenclatura estandarizada / Standardized Naming

Todos los test cases siguen el formato / All test cases follow the format:

```
TC - [A11Y] - {Guideline Number} {Guideline Name} - {Criterion Number} {Criterion Name}
```

**Ejemplo / Example:**

```
TC - [A11Y] - 1.2 Time-based Media - 1.2.5 Audio Description (Prerecorded)
```

---

## Uso en Azure DevOps

### Estructura del CSV

```csv
ID,Work Item Type,Title,Test Step,Step Action,Step Expected,Step Data,Description,Priority,Automation Status,Area Path,State,Tags
```

| Columna               | Descripción                                                           | Valor por defecto                                                            |
| --------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **ID**                | Vacío — Azure genera IDs automáticamente al importar                  | `""`                                                                         |
| **Work Item Type**    | Tipo de work item                                                     | `"Test Case"`                                                                |
| **Title**             | Título estandarizado del criterio WCAG                                | `"TC - [A11Y] - 1.1 Text Alternatives - 1.1.1 Non-text Content"`             |
| **Test Step**         | Número del paso                                                       | `"1"`, `"2"`, `"3"`                                                          |
| **Step Action**       | Acción que realiza el tester (incluye referencia `axe-core` si aplica)| Texto descriptivo                                                            |
| **Step Expected**     | Resultado esperado                                                    | Texto descriptivo                                                            |
| **Step Data**         | Reglas `axe-core` y tag WCAG asociados al paso                        | `"axe-core (wcag111): image-alt, role-img-alt..."`                           |
| **Description**       | Pauta y criterio WCAG (en la fila cabecera del Test Case, ES/EN)      | `"Guideline 1.1 Text Alternatives. Success Criteria: 1.1.1..."`              |
| **Priority**          | Prioridad del Test Case en Azure DevOps (`2` = Medium)                | `"2"`                                                                        |
| **Automation Status** | Estado de automatización                                              | `"Not Automated"`                                                            |
| **Area Path**         | Área y subcarpeta por principio WCAG                                  | `"Accesibilidad\1. Perceptible"` (ES) / `"Accessibility\1. Perceivable"` (EN)|
| **State**             | Estado del test case                                                  | `"Ready"`                                                                    |
| **Tags**              | Etiquetas (incluye nivel y tipo, paridad 1:1 con Jira)                | `"A11Y;A;A11Y_MANUAL"`                                                       |

### Pasos de Importación

1. **Descarga** `A11Y_Repository_Azure_ES.csv` o `A11Y_Repository_Azure_EN.csv`
2. **Navega** a tu proyecto en Azure DevOps → **Test Plans** → **Test Cases**
3. **Importa** haciendo clic en el menú (⋯) → **Import test cases from CSV**
4. **Carga** el archivo CSV
5. **Verifica** los 87 test cases importados y asigna testers según necesidad

### Personalización

- **Area Path**: Modifica `"Accesibilidad"` / `"Accessibility"` por el área de tu proyecto
- **State**: Cambia entre `Design`, `Ready` o `Closed` según tu flujo
- **Tags**: Agrega etiquetas adicionales separadas por `;`
- **Assigned To**: Agrega una columna con el email del tester asignado

### Referencia

- [Importar/Exportar Test Cases en Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/test/bulk-import-export-test-cases?view=azure-devops)

---

## Uso en Jira (Xray / Zephyr Scale)

### Estructura del CSV

```csv
TCID,Test Summary,Issue Type,Test Type,Priority,Labels,Description,Test Repository Path,Step #,Action,Data,Expected Result
```

| Columna                  | Descripción                                                   | Ejemplo                                                              |
| ------------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------- |
| **TCID**                 | ID local para agrupar pasos del mismo test                    | `"1"`, `"2"`, ... `"87"`                                             |
| **Test Summary**         | Título estandarizado del test (solo en primer paso)           | `"TC - [A11Y] - 1.1 Text Alternatives - 1.1.1 Non-text Content"`     |
| **Issue Type**           | Tipo de issue Jira (solo en primer paso)                      | `"Test"`                                                             |
| **Test Type**            | Tipo de test en Xray (solo en primer paso)                    | `"Manual"`                                                           |
| **Priority**             | Prioridad (solo en primer paso)                               | `"Medium"`                                                           |
| **Labels**               | Etiquetas separadas por `;` (solo en primer paso)             | `"A11Y;A;A11Y_MANUAL"`, `"A11Y;AA;A11Y_MANUAL"`                      |
| **Description**          | Pauta y criterio WCAG (solo en primer paso, ES/EN)            | `"Guideline 1.1 Text Alternatives. Success Criteria: 1.1.1..."`      |
| **Test Repository Path** | Carpeta por principio en Xray Test Repository                 | `"1. Perceivable"` (EN) / `"1. Perceptible"` (ES)                    |
| **Step #**               | Número del paso                                               | `"1"`, `"2"`, `"3"`                                                  |
| **Action**               | Acción del paso de prueba                                     | Texto descriptivo                                                    |
| **Data**                 | Reglas `axe-core` y tag WCAG asociados (cuando aplica)        | `"axe-core (wcag111): image-alt, role-img-alt..."`                   |
| **Expected Result**      | Resultado esperado                                            | Texto descriptivo                                                    |

### Importar con Xray

1. **Navega** a tu proyecto en Jira
2. **Ve** a **Xray** → **Test Case Importer** (o **Import Tests**)
3. **Selecciona** "CSV" como fuente
4. **Carga** `A11Y_Repository_Jira_ES.csv` o `A11Y_Repository_Jira_EN.csv`
5. **Mapea** las columnas:
   - `Test Summary` → Summary
   - `Issue Type` → Issue Type
   - `Test Type` → Test Type
   - `Priority` → Priority
   - `Labels` → Labels
   - `Description` → Description
   - `Test Repository Path` → Test Repository Path
   - `Action` → Step Action
   - `Data` → Step Data
   - `Expected Result` → Step Expected Result
   - `TCID` → Test Case Identifier (para agrupar pasos)
6. **Importa** y verifica los 87 test cases

### Importar con Zephyr Scale

1. **Navega** a tu proyecto en Jira
2. **Ve** a **Zephyr Scale** → **Test Cases** → **Import**
3. **Selecciona** "CSV" como fuente
4. **Carga** `A11Y_Repository_Jira_ES.csv` o `A11Y_Repository_Jira_EN.csv`
5. **Mapea** las columnas:
   - `Test Summary` → Name
   - `Priority` → Priority
   - `Labels` → Labels
   - `Action` → Test Script (Step-by-Step) - Step
   - `Data` → Test Script (Step-by-Step) - Test Data
   - `Expected Result` → Test Script (Step-by-Step) - Expected Result
6. **Importa** y verifica

### Importar con CSV Importer nativo de Jira

Si no usas Xray ni Zephyr, puedes usar el importador CSV estándar de Jira:

1. **Ve** a **Jira** → **System** → **External System Import** → **CSV**
2. **Carga** el archivo y mapea las columnas básicas (`Test Summary`, `Issue Type`, `Priority`, `Labels`)
3. Los pasos de prueba se importarán como texto en la descripción

### Referencia

- [Xray - CSV Test Case Importer](https://docs.getxray.app/display/XRAY/Importing+Test+Cases+-+CSV)
- [Zephyr Scale - Import Test Cases](https://support.smartbear.com/zephyr-scale-cloud/docs/test-cases/import-test-cases.html)

---

## Cobertura WCAG 2.2

| Principio           | Pautas    | Test Cases       | Niveles    |
| ------------------- | --------- | ---------------- | ---------- |
| **1. Perceptible**  | 1.1 – 1.4 | 29 criterios     | A, AA, AAA |
| **2. Operable**     | 2.1 – 2.5 | 34 criterios     | A, AA, AAA |
| **3. Comprensible** | 3.1 – 3.3 | 21 criterios     | A, AA, AAA |
| **4. Robusto**      | 4.1       | 3 criterios      | A, AA      |
| **Total**           |           | **87 criterios** |            |

> **Nota**: Se incluye el criterio 4.1.1 (Parsing) que fue marcado como obsoleto en WCAG 2.2 pero se mantiene como referencia.

## Pipeline de Regeneración / Regeneration Pipeline

Los CSV se generan desde una fuente única de verdad. **No editar los CSV a mano**.

| Archivo                | Rol                                                                 |
| ---------------------- | ------------------------------------------------------------------- |
| `source.json`          | Export de los 87 TCs canónicos desde Jira/Xray (tipo, pasos, labels) |
| `fallback_steps.json`  | Pasos manuales curados para criterios ejecutados por automatización  |
| `translations_es.json` | Traducciones ES indexadas por `action\|\|result`                     |
| `export_jira.py`       | Extrae el test repository canónico de Jira → `source.json`           |
| `generate.py`          | Renderiza los 4 CSV desde `source.json` + datos auxiliares           |

```bash
# 1. Exportar desde Jira (requiere credenciales en el entorno)
export JIRA_EMAIL JIRA_API_TOKEN XRAY_CLIENT_ID XRAY_CLIENT_SECRET
python3 export_jira.py

# 2. Regenerar los CSV
python3 generate.py
```

Si un paso manual no tiene traducción ES, `generate.py` falla indicando el paso exacto: añádala en `translations_es.json` y repita.

## Notas Técnicas

### Formato de Archivos

- **Codificación**: UTF-8
- **Delimitador**: Coma (`,`)
- **Comillas**: Dobles (`"`) para encapsular campos
- **Archivos ES**: Pasos de prueba en español
- **Archivos EN**: Pasos de prueba en inglés
- **Títulos**: Siempre en inglés siguiendo convención internacional WCAG

### Limitaciones

| Plataforma   | Límite de importación                  |
| ------------ | -------------------------------------- |
| Azure DevOps | Máximo 1000 test cases por importación |
| Xray         | Sin límite práctico                    |
| Zephyr Scale | Máximo 2000 test cases por importación |

### Personalización Recomendada

Después de importar, puedes:

- Agregar **precondiciones** específicas para tu aplicación
- Asociar test cases a **test suites** por principio WCAG (Perceptible, Operable, etc.)
- Vincular test cases a **requisitos** o **historias de usuario**
- Modificar **prioridades** según el nivel de conformidad objetivo (A, AA o AAA)

## Referencias

- [WCAG 2.2 — Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [WCAG 2.2 — W3C Recommendation](https://www.w3.org/TR/WCAG22/)
- [Azure DevOps — Test Plans Documentation](https://learn.microsoft.com/en-us/azure/devops/test/?view=azure-devops)
- [Xray — Test Management for Jira](https://docs.getxray.app/)
- [Zephyr Scale — Documentation](https://support.smartbear.com/zephyr-scale-cloud/docs/)

## Contribuciones

Este repositorio está diseñado para equipos de QA y accesibilidad. Si encuentras mejoras o criterios adicionales:

1. Haz un fork del repositorio
2. Crea una rama para tus cambios
3. Mantén la estructura CSV compatible con ambas plataformas
4. Asegura que los cuatro archivos (Azure ES/EN y Jira ES/EN) contengan los mismos test cases
5. Envía un pull request con descripción detallada
