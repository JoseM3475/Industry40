# Desplegar Azure Iot Hub

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

