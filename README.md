# WCAG 2.2 Test Cases — Azure DevOps & Jira (Xray / Zephyr)

Repositorio estandarizado con **86 casos de prueba** basados en los criterios de accesibilidad **WCAG 2.2**, listos para importación masiva en **Azure DevOps Test Plans** y **Jira** (compatible con Xray y Zephyr Scale).

## 📁 Archivos Disponibles

| Archivo | Plataforma | Formato |
|---------|-----------|---------|
| `A11Y_Repository_Azure.csv` | Azure DevOps Test Plans | CSV con columnas Azure (Work Item Type, Test Steps) |
| `A11Y_Repository_Jira.csv` | Jira + Xray / Zephyr Scale | CSV con columnas Xray (TCID, Test Summary, Steps) |

Ambos archivos contienen los **mismos 86 criterios WCAG 2.2** (Niveles A, AA y AAA) con **2-4 pasos de prueba** cada uno.

---

## 🔵 Uso en Azure DevOps

### Estructura del CSV

```csv
ID,Work Item Type,Title,Test Step,Step Action,Step Expected,Automation Status,Area Path,State,Tags
```

| Columna | Descripción | Valor por defecto |
|---------|-------------|-------------------|
| **ID** | Vacío — Azure genera IDs automáticamente al importar | `""` |
| **Work Item Type** | Tipo de work item | `"Test Case"` |
| **Title** | Título con número de criterio WCAG | `"[1.1.1] Contenido no textual..."` |
| **Test Step** | Número del paso | `"1"`, `"2"`, `"3"` |
| **Step Action** | Acción que realiza el tester | Texto descriptivo |
| **Step Expected** | Resultado esperado | Texto descriptivo |
| **Automation Status** | Estado de automatización | `"Not Automated"` |
| **Area Path** | Área del proyecto | `"Accesibilidad"` |
| **State** | Estado del test case | `"Ready"` |
| **Tags** | Etiquetas | `"A11Y"` |

### Pasos de Importación

1. **Descarga** `A11Y_Repository_Azure.csv`
2. **Navega** a tu proyecto en Azure DevOps → **Test Plans** → **Test Cases**
3. **Importa** haciendo clic en el menú (⋯) → **Import test cases from CSV**
4. **Carga** el archivo CSV
5. **Verifica** los 86 test cases importados y asigna testers según necesidad

### Personalización

- **Area Path**: Modifica `"Accesibilidad"` por el área de tu proyecto
- **State**: Cambia entre `Design`, `Ready` o `Closed` según tu flujo
- **Tags**: Agrega etiquetas adicionales separadas por `;`
- **Assigned To**: Agrega una columna con el email del tester asignado

### Referencia

- [Importar/Exportar Test Cases en Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/test/bulk-import-export-test-cases?view=azure-devops)

---

## 🟢 Uso en Jira (Xray / Zephyr Scale)

### Estructura del CSV

```csv
TCID,Test Summary,Issue Type,Priority,Labels,Step #,Action,Data,Expected Result
```

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| **TCID** | ID local para agrupar pasos del mismo test | `"1"`, `"2"`, ... `"86"` |
| **Test Summary** | Título del test (solo en primer paso) | `"TC - [A11y] - 1.1 - Text Alternatives - 1.1.1 - Non-text Content"` |
| **Issue Type** | Tipo de issue Jira (solo en primer paso) | `"Test"` |
| **Priority** | Prioridad (solo en primer paso) | `"Medium"` |
| **Labels** | Etiquetas separadas por `;` (solo en primer paso) | `"A11Y;A"`, `"A11Y;AA"`, `"A11Y;AAA"` |
| **Step #** | Número del paso | `"1"`, `"2"`, `"3"` |
| **Action** | Acción del paso de prueba | Texto descriptivo |
| **Data** | Datos de prueba (vacío por defecto) | `""` |
| **Expected Result** | Resultado esperado | Texto descriptivo |

### Importar con Xray

1. **Navega** a tu proyecto en Jira
2. **Ve** a **Xray** → **Test Case Importer** (o **Import Tests**)
3. **Selecciona** "CSV" como fuente
4. **Carga** `A11Y_Repository_Jira.csv`
5. **Mapea** las columnas:
   - `Test Summary` → Summary
   - `Issue Type` → Issue Type
   - `Priority` → Priority
   - `Labels` → Labels
   - `Action` → Step Action
   - `Data` → Step Data
   - `Expected Result` → Step Expected Result
   - `TCID` → Test Case Identifier (para agrupar pasos)
6. **Importa** y verifica los 86 test cases

### Importar con Zephyr Scale

1. **Navega** a tu proyecto en Jira
2. **Ve** a **Zephyr Scale** → **Test Cases** → **Import**
3. **Selecciona** "CSV" como fuente
4. **Carga** `A11Y_Repository_Jira.csv`
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

## 📊 Cobertura WCAG 2.2

| Principio | Pautas | Test Cases | Niveles |
|-----------|--------|------------|---------|
| **1. Perceptible** | 1.1 – 1.4 | 29 criterios | A, AA, AAA |
| **2. Operable** | 2.1 – 2.5 | 33 criterios | A, AA, AAA |
| **3. Comprensible** | 3.1 – 3.3 | 21 criterios | A, AA, AAA |
| **4. Robusto** | 4.1 | 3 criterios | A, AA |
| **Total** | | **86 criterios** | |

> **Nota**: Se incluye el criterio 4.1.1 (Parsing) que fue marcado como obsoleto en WCAG 2.2 pero se mantiene como referencia.

## 📝 Notas Técnicas

### Formato de Archivos

- **Codificación**: UTF-8
- **Delimitador**: Coma (`,`)
- **Comillas**: Dobles (`"`) para encapsular campos
- **Idioma de pasos**: Español (los títulos en Jira están en inglés siguiendo convención internacional)

### Limitaciones

| Plataforma | Límite de importación |
|------------|----------------------|
| Azure DevOps | Máximo 1000 test cases por importación |
| Xray | Sin límite práctico |
| Zephyr Scale | Máximo 2000 test cases por importación |

### Personalización Recomendada

Después de importar, puedes:
- Agregar **precondiciones** específicas para tu aplicación
- Asociar test cases a **test suites** por principio WCAG (Perceptible, Operable, etc.)
- Vincular test cases a **requisitos** o **historias de usuario**
- Modificar **prioridades** según el nivel de conformidad objetivo (A, AA o AAA)

## 📚 Referencias

- [WCAG 2.2 — Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [WCAG 2.2 — W3C Recommendation](https://www.w3.org/TR/WCAG22/)
- [Azure DevOps — Test Plans Documentation](https://learn.microsoft.com/en-us/azure/devops/test/?view=azure-devops)
- [Xray — Test Management for Jira](https://docs.getxray.app/)
- [Zephyr Scale — Documentation](https://support.smartbear.com/zephyr-scale-cloud/docs/)

## 🤝 Contribuciones

Este repositorio está diseñado para equipos de QA y accesibilidad. Si encuentras mejoras o criterios adicionales:

1. Haz un fork del repositorio
2. Crea una rama para tus cambios
3. Mantén la estructura CSV compatible con ambas plataformas
4. Asegura que ambos archivos (Azure y Jira) contengan los mismos test cases
5. Envía un pull request con descripción detallada