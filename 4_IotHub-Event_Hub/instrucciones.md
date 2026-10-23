# Desplegar Azure Iot Hub y Azure Event Hub

## Crear Grupo de Recursos
```powershell
az group create `
  --name Industry40 `
  --location eastus2
```
## Desplegar Bicep con Azure Iot Hub

```powershell
az deployment group create `
  --resource-group Industry40 `
  --template-file iothub.bicep
```
## Verificar despliegue

```powershell
az iot hub show `
  --name fabrica `
  --resource-group Industry40 `
  --output table
```
## Crear Azure Event Hubs Namespace
```powershell
az eventhubs namespace create `
  --resource-group Industry40 `
  --name industry40ehns `
  --location eastus2 `
  --sku Standard
```
# Crear un Event Hub dentro del namespace
```powershell
az eventhubs eventhub create `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --name telemetria
```

## Crear una política de acceso
```powershell
az eventhubs eventhub authorization-rule create `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --eventhub-name telemetria `
  --name lecturaescritura `
  --rights Listen Send
```
## Obtener la connection string:
```powershell
az eventhubs eventhub authorization-rule keys list `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --eventhub-name telemetria `
  --name lecturaescritura
```
## Ver los Even Hubs creados
```powershell
az eventhubs eventhub list `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --output table
```
# Enviar la telemetria a Azure Event Hub

## Crear un endpoint de Event Hub en el IoT Hub
```powershell
az iot hub routing-endpoint create `
  --resource-group Industry40 `
  --hub-name fabrica `
  --endpoint-name ehtelemetria `
  --endpoint-resource-group Industry40 `
  --endpoint-subscription-id 05ca285f-d2ae-4f9e-abdc-d6ce4aa76182 `
  --endpoint-type eventhub `
  --connection-string ""
```
## Crear una ruta

```powershell
az iot hub route create `
  --resource-group Industry40 `
  --hub-name fabrica `
  --name RouteToEventHub `
  --source-type DeviceMessages `
  --endpoint-name ehtelemetria `
  --enabled true
```

## Crear Dispositivo en Azure IoT Hub
```powershell
az iot hub device-identity create `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01

az iot hub device-identity show `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01
```
## Obtener la cadena de conexión del sensor
```powershell
az iot hub device-identity connection-string show `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01
```
## Copiar la cadena de conexión en el fichero .env

## Crear entorno virtual de Python
```powershell
python -m venv venv

.\venv\Scripts\Activate.ps1

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
## Instalar dependencias
```powershell
pip install -r requirements.txt
```
## Ejecutar sensor
```powershell
python temperature_sensor.py
```
## Verificar que el sensor funciona:
```powershell
az iot hub monitor-events `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01
```


## Borrar grupo de recursos
```powershell
az group delete `
  --name Industry40 `
  --yes `
  --no-wait
```
## Desactivar entorno virtual Python
```powershell
deactivate
```
### Otros comandos de la CLI de Azure útiles
```powershell
az iot hub device-identity list \
  --hub-name fabrica.azure-devices.net

az iot hub device-identity delete \
  --hub-name fabrica.azure-devices.net \
  --device-id temp-sensor-01
```
