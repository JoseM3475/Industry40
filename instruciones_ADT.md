# Instrucciones Azure Digital Twin

## Crear grupo de recursos

```bash
az group create \
  --name Industry40ADT \
  --location eastus2#
```
## Eliminar Grupo de Recursos

```bash
az group delete \
  --name Industry40ADT \
  --yes \
  --no-wait
```

## Azure Digital Twin

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
-n mi-adt \
--assignee usuario@empresa.com \
--role "Azure Digital Twins Data Reader"

# Listar assignaciones
az dt role-assignment list \
  -n Industry40ADT-DT




```