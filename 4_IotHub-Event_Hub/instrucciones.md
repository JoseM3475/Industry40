# Desplegar Azure Iot Hub y Azure Event Hub

## Crear Grupo de Recursos

az group create `
  --name Industry40 `
  --location eastus2

## Desplegar Bicep con Azure Iot Hub

az deployment group create `
  --resource-group Industry40 `
  --template-file iothub.bicep

## Verificar despliegue

az iot hub show `
  --name fabrica `
  --resource-group Industry40 `
  --output table

## Crear Azure Event Hubs Namespace

az eventhubs namespace create `
  --resource-group Industry40 `
  --name industry40ehns `
  --location eastus2 `
  --sku Standard

# Crear un Event Hub dentro del namespace

az eventhubs eventhub create `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --name telemetria


## Crear una política de acceso

az eventhubs eventhub authorization-rule create `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --eventhub-name telemetria `
  --name lecturaescritura `
  --rights Listen Send

## Obtener la connection string:

az eventhubs eventhub authorization-rule keys list `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --eventhub-name telemetria `
  --name lecturaescritura

## Ver los Even Hubs creados

az eventhubs eventhub list `
  --resource-group Industry40 `
  --namespace-name industry40ehns `
  --output table

# Enviar la telemetria a Azure Event Hub

## Crear un endpoint de Event Hub en el IoT Hub

az iot hub routing-endpoint create `
  --resource-group Industry40 `
  --hub-name fabrica `
  --endpoint-name ehtelemetria `
  --endpoint-resource-group Industry40 `
  --endpoint-subscription-id 05ca285f-d2ae-4f9e-abdc-d6ce4aa76182 `
  --endpoint-type eventhub `
  --connection-string ""

## Crear una ruta

az iot hub route create `
  --resource-group Industry40 `
  --hub-name fabrica `
  --name RouteToEventHub `
  --source-type DeviceMessages `
  --endpoint-name ehtelemetria `
  --enabled true

## Crear Dispositivo en Azure IoT Hub

az iot hub device-identity create `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01

az iot hub device-identity show `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01

## Obtener la cadena de conexión del sensor

az iot hub device-identity connection-string show `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01

## Copiar la cadena de conexión en el fichero .env

## Crear entorno virtual de Python

python -m venv venv

.\venv\Scripts\Activate.ps1

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

## Instalar dependencias

pip install -r requirements.txt

## Ejecutar sensor

python temperature_sensor.py

## Verificar que el sensor funciona:

az iot hub monitor-events `
  --hub-name fabrica.azure-devices.net `
  --device-id sensor-temperatura-01



## Borrar grupo de recursos

az group delete `
  --name Industry40 `
  --yes `
  --no-wait

## Desactivar entorno virtual Python

deactivate

### Otros comandos de la CLI de Azure útiles

az iot hub device-identity list \
  --hub-name fabrica.azure-devices.net

az iot hub device-identity delete \
  --hub-name fabrica.azure-devices.net \
  --device-id temp-sensor-01

