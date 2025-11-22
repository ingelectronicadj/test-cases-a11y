# WCAG 2.2 Test Cases para Azure DevOps

Este repositorio contiene un conjunto completo de casos de prueba (test cases) basados en los criterios de accesibilidad **WCAG 2.2** (Web Content Accessibility Guidelines), preparados para importación masiva en **Azure DevOps**.

## Contenido

- **86 criterios WCAG 2.2** cubiertos (Niveles A, AA y AAA)
- **Pasos de prueba detallados** (2-4 pasos por test case)
- **Formato CSV** compatible con Azure DevOps Test Plans
- Estructura lista para carga masiva

## Cómo Usar

### Prerrequisitos

1. Tener acceso a **Azure DevOps**
2. Permisos de **Test Plans** en tu proyecto
3. Permisos para crear y editar test cases

### Pasos de Importación

1. **Descarga el archivo CSV**

2. **Accede a Azure DevOps Test Plans**
   - Navega a tu proyecto en Azure DevOps
   - Ve a **Test Plans** > **Test Cases**

3. **Importa el CSV**
   - Haz clic en el botón de menú (tres puntos) en la barra superior
   - Selecciona **Import test cases**
   - Carga el archivo `wcag-2.2-test-cases.csv`

4. **Verifica la importación**
   - Azure DevOps procesará el archivo
   - Revisa los test cases importados
   - Asigna a los testers correspondientes según sea necesario

### Tutorial Oficial

Para más detalles sobre el proceso de importación, consulta la [documentación oficial de Microsoft](https://learn.microsoft.com/en-us/azure/devops/test/bulk-import-export-test-cases?view=azure-devops).

## 📊 Estructura del CSV

El archivo CSV utiliza las siguientes **cabeceras obligatorias** según el formato de Azure DevOps:

```csv
"ID","Work Item Type","Title","Test Step","Step Action","Step Expected","Assigned To","State"
```

### Descripción de Cabeceras

| Cabecera | Descripción | Obligatorio | Ejemplo |
|----------|-------------|-------------|---------|
| **ID** | Identificador único del work item (vacío para nuevos) | No | `""` |
| **Work Item Type** | Tipo de elemento de trabajo | Sí | `"Test Case"` |
| **Title** | Título descriptivo del test case | Sí | `"[1.1.1] Contenido no textual - Imágenes"` |
| **Test Step** | Número del paso de prueba | Sí | `"1"`, `"2"`, `"3"` |
| **Step Action** | Acción que debe realizar el tester | Sí | `"Inspeccionar todas las imágenes..."` |
| **Step Expected** | Resultado esperado de la acción | Sí | `"Cada imagen debe tener..."` |
| **Assigned To** | Usuario asignado (email o nombre) | No | `""` o `"usuario@dominio.com"` |
| **State** | Estado del test case | No | `"Design"`, `"Ready"`, `"Closed"` |

### Cambiar Estados

Modifica la columna **"State"** según tu flujo de trabajo:
- `Design` - En diseño (por defecto)
- `Ready` - Listo para ejecutar
- `Closed` - Completado

### Agregar Más Campos

Azure DevOps permite campos adicionales. Consulta la [documentación de campos personalizados](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/work-item-field?view=azure-devops) para extender la plantilla.

## 📝 Notas Importantes

### Formato del Archivo

- **Codificación**: UTF-8 con BOM
- **Delimitador**: Coma (`,`)
- **Comillas**: Dobles (`"`) para encapsular campos con comas o saltos de línea
- **Saltos de línea**: Los campos con múltiples líneas deben estar entre comillas

### Limitaciones de Azure DevOps

- Máximo **1000 test cases** por importación (este archivo contiene 86 test cases, bien dentro del límite)
- Los **IDs duplicados** serán actualizados en lugar de crear nuevos
- Los campos personalizados deben existir previamente en tu proyecto


## Referencias

- [WCAG 2.2 Official Guidelines](https://www.w3.org/WAI/WCAG22/quickref/)
- [Azure DevOps - Bulk Import Test Cases](https://learn.microsoft.com/en-us/azure/devops/test/bulk-import-export-test-cases?view=azure-devops)
- [Azure DevOps - Test Plans Documentation](https://learn.microsoft.com/en-us/azure/devops/test/?view=azure-devops)

## 🤝 Contribuciones

Este repositorio está diseñado para equipos de QA y accesibilidad. Si encuentras mejoras o criterios adicionales:

1. Haz un fork del repositorio
2. Crea una rama para tus cambios
3. Mantén la estructura de CSV compatible con Azure DevOps
4. Envía un pull request con descripción detallada