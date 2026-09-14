git branch -M main
git remote add origin https://github.com/JoseM3475/Industry40.git
git push -u origin main

Crea una plantilla bicep que cree un recurso Azure Iot Hub llamado fabrica, con sku=standard, en un gurpo de recursos llamado Industria40 en EastUs2 que tenga un grupo de consumidores llamado adx. Crea dentro de el un device llamado sensor-temperatura-01. 

Crea también un Azure Data Explorer cluster llado adx-fabrica en el mismo grupo de recursos y region. Debe tener una base de datos llamada metricas-fabrica, y una tabla llamada temperaturas que permita almacenar la información que emite sensor-temperatura-01, que es de la forma: {'sensorId': 'temp-sensor-01', 'temperature': 24.14, 'unit': 'C'}. Crea una Data Conexion que mande la información del sensor-temperatura-01 a la tabla temperaturas.

Crea el consumer group adx.
Crea el clúster ADX adx-fabrica.
Crea la base de datos metricas-fabrica.
Crea la Data Connection entre IoT Hub y ADX utilizando el consumer group adx.
Incluye un deploymentScript que ejecuta los comandos KQL para crear:
tabla temperaturas
mapping JSON correspondiente.