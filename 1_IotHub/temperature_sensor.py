import json
import os
import random
import time

from dotenv import load_dotenv
from azure.iot.device import IoTHubDeviceClient, Message

# Cargar variables de entorno
load_dotenv(override=True)

# Obtener la Connection String desde el .env
connection_string = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

if not connection_string:
    raise ValueError(
        "No se encontró la variable IOTHUB_DEVICE_CONNECTION_STRING en el fichero .env"
    )

# Crear cliente IoT Hub
client = IoTHubDeviceClient.create_from_connection_string(
    connection_string
)

try:
    print("Conectando a Azure IoT Hub...")
    client.connect()
    print("Conectado correctamente.")

    while True:
        # Simulación de temperatura
        temperature = round(random.uniform(18.0, 35.0), 2)

        payload = {
            "sensorId": "temp-sensor-01",
            "temperature": temperature,
            "unit": "C"
        }

        message = Message(json.dumps(payload))
        message.content_type = "application/json"
        message.content_encoding = "utf-8"

        # Generar alerta si supera 30 ºC
        if temperature > 30:
            message.custom_properties["temperatureAlert"] = "true"

        client.send_message(message)

        print(f"Mensaje enviado: {payload}")

        time.sleep(10)

except KeyboardInterrupt:
    print("Sensor detenido por el usuario.")

finally:
    client.shutdown()