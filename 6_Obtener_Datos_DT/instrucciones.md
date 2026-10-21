# Obtener datos del DT

## Instalar CLI Azure

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```
## Crear un entorno virtual de Python
Sitúate en la carpeta de tu proyecto

```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
## Conectarse al servicio ADT. Obtén la URL de tu instancia:

```bash
az dt show \
  --dt-name Industry40ADT-DT \
  --query hostName
  ```