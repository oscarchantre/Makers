# Prueba técnica QA Integral

## Descripción
Repositorio con colecciones de Postman, Newman ,automatización con playwright y Gherkin, casos de prueba y evidencias. 

Objetivo: Realizar las siguientes pruebas:

Módulo de Automatización – Smoke Test de Inicio de Sesión (SauceDemo)
Pruebas Funcionales, Producto ficticio: MakersPay, una billetera digital
prueba funcional API: https://student.geekqa.net/api/ 

## Estructura del repositorio
- `Postman` - colección exportada desde Postman y documentación.
- `Documentación Makers` - casos de prueba manuales (Escenarios - Casos de pruebas - reporte bug), Evidencia Smoke Test de Inicio de Sesión.
- `Proyecto Cucumber` -Módulo de Automatización – Smoke Test de Inicio de Sesión (SauceDemo).

## Requisitos locales
- git
- Postman Newman Codigo de ejecución para reportes: npx newman run Students.postman_collection.json

- Playwright con python y Gherkin ejecutar prueba:
   pytest -v tests/ --headed --browser chromium
con un informe:
   pytest -v tests/ --headed --browser chromium --html=reportes/reporte.html --self-contained-html

