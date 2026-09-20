# Proyecto Urban Grocers 

## ¿Qué es esto?
Este proyecto es una suite de pruebas automatizadas en Python enfocada en validar la API del servicio Urban Grocers, asegurando la calidad en los flujos de registro de usuarios y creación de kits de productos.

## Producto / Funcionalidad bajo prueba
- Endpoint de creación de usuario (`POST /api/v1/users`) para la obtención del `authToken`.
- Endpoint de creación de kits de productos (`POST /api/v1/kits`) bajo diferentes criterios de validación en el parámetro `name`.

## Objetivo
Verificar la estabilidad y la correcta respuesta del backend ante peticiones válidas e inválidas, asegurando que los límites de caracteres y formatos especiales en los campos cumplan con la especificación técnica.

## Alcance
- **Incluido:** Pruebas de integración para generación de token, pruebas unitarias/funcionales de bordes (límites de 1, 511, 0, y 512 caracteres, tipos de datos no válidos y ausencias de parámetros).
- **Excluido:** Pruebas de carga/rendimiento y pruebas de interfaz de usuario (UI).

## Artefactos en esta carpeta
- `configuration.py`: Configuración de URLs base y rutas de endpoints.
- `data.py`: Cuerpos de solicitud (payloads) y encabezados HTTP.
- `sender_stand_request.py`: Lógica para el envío de peticiones HTTP (`requests`).
- `create_kit_name_kit_test.py`: Suite de casos de prueba ejecutables con `pytest`.

## Decisiones clave
- **Priorización de escenarios críticos:** Se dio prioridad a la creación de usuarios para garantizar la autenticación fluida de las pruebas posteriores.
- **Pruebas de límite (Boundary Testing):** Se priorizaron los valores límite en el nombre del kit (1 y 511 caracteres) para prevenir fallos en la base de datos por desbordamiento de cadenas.

## Resultados
- **Cobertura alcanzada:** 100% de los escenarios de la lista de verificación automatizados ejecutándose de forma exitosa.

## ¿Qué mejoraría después?
- Implementar integración continua con GitHub Actions para ejecutar las pruebas automáticamente en cada push.
- Generar reportes visuales detallados integrando herramientas como Allure Framework.
