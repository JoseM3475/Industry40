# Flujo de Trabajo para representar un edificio en un gemelo digital en Azure

## Flujo de Trabajo

1. Modelar los activos físicos
            
2. Crear los modelos DTDL
            
3. Desplegar Azure Digital Twins
            
4. Crear los Twins (instancias)
            
5. Crear relaciones entre Twins
            
6. Conectar dispositivos IoT
            
7. Actualizar propiedades en tiempo real
            
8. Realizar consultas y análisis
            
9. Visualizar la información

## 1. Identificar y modelar los activos físicos

Las entidades del Digital Twin van a ser Buliding, Floor y Room.
La habitación tiene un atributo: temperatura.


## 2. Crear los modelos DTDL

Building
```JSON
{
  "@id": "dtmi:empresa:Building;1",
  "@type": "Interface",
  "displayName": "Building",
  "contents": [
    {
      "@type": "Property",
      "name": "name",
      "schema": "string"
    },
    {
      "@type": "Relationship",
      "name": "containsFloor",
      "target": "dtmi:empresa:Floor;1"
    }
  ],
  "@context": "dtmi:dtdl:context;2"
}
```
Floor
```JSON
{
  "@id": "dtmi:empresa:Floor;1",
  "@type": "Interface",
  "displayName": "Floor",
  "contents": [
    {
      "@type": "Property",
      "name": "floorNumber",
      "schema": "integer"
    },
    {
      "@type": "Relationship",
      "name": "containsRoom",
      "target": "dtmi:empresa:Room;1"
    }
  ],
  "@context": "dtmi:dtdl:context;2"
}
```
Room
```JSON
{
  "@id": "dtmi:empresa:Room;1",
  "@type": "Interface",
  "displayName": "Room",
  "contents": [
    {
      "@type": "Property",
      "name": "roomName",
      "schema": "string"
    },
    {
      "@type": "Property",
      "name": "temperature",
      "schema": "double",
      "displayName": "Temperature"
    }
  ],
  "@context": "dtmi:dtdl:context;2"
}
```
## 3. Crear la instancia de Azure Digital Twins

### Crear/borras Grupo de Recursos

```bash
az group create \
  --name Industry40ADT \
  --location eastus2

az group delete \
  --name Industry40ADT \
  --yes \
  --no-wait
```
### Crear Recurso de Azure Digital Twin

```bash
# Crear Azure Digital Twins
az dt create \
  --dt-name Industry40ADT-DT \
  --resource-group Industry40ADT \
  --location eastus2

# Mostrar detalles
az dt show \
  --dt-name Industry40ADT-DT

# Eliminar Azure Digital Twins
az dt delete \
  --dt-name Industry40ADT-DT \
  --yes
```
## Roles

Para trabajar con Azure Digital Twins (ADT) debes distinguir entre dos tipos de permisos:

- **Control Plane** → administrar el recurso Azure Digital Twins (crear instancia, configurar endpoints, networking, etc.).
- **Data Plane** → trabajar con modelos, twins, relaciones y consultas del grafo.

### Azure Digital Twins Data Owner

Es el rol que normalmente necesitan los desarrolladores y administradores funcionales de ADT.

Permite:

- Crear y borrar modelos DTDL.
- Crear, modificar y borrar twins.
- Crear y borrar relationships.
- Ejecutar consultas sobre el grafo.
- Gestionar event routes.

### Azure Digital Twins Data Reader

Permite:

- Leer modelos.
- Consultar twins.
- Leer relaciones.
- Ejecutar queries.

No permite modificar nada.

## Gestion RBAC ADT

```bash
az dt role-assignment create \
  -n Industry40ADT-DT \
  --assignee usuario@empresa.com \
  --role "Azure Digital Twins Data Owner"

az dt role-assignment create \
-n Industry40ADT-DT \
--assignee usuario@empresa.com \
--role "Azure Digital Twins Data Reader"

# Listar assignaciones
az dt role-assignment list \
  -n Industry40ADT-DT

```

## 4. Subir los modelos
```bash
az dt model create \
    --dt-name Industry40ADT-DT \
    --models Building.json

az dt model create \
    --dt-name Industry40ADT-DT \
    --models Floor.json

az dt model create \
    --dt-name Industry40ADT-DT \
    --models  Room.json

#Comprobar que están cargados
az dt model list \
    --dt-name Industry40ADT-DT
```




