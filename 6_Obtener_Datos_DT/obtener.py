from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient

url = "Industry40ADT-DT.api.eus2.digitaltwins.azure.net"

credential = DefaultAzureCredential()

client = DigitalTwinsClient(url, credential)

room = client.get_digital_twin("Habitacion1")

print(room["temperature"])