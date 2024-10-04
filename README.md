
# Capacitación Docker


## Versión: v1.1.0

En este ejercicio, se crea una API con un nuevo endpoint que guarda una lista no ordenada en una base de datos MongoDB utilizando Docker y la librería `pymongo`.

## Requisitos previos

- Docker instalado en el sistema.
- Python instalado.
- Librerías `pymongo` y `uuid`.


## Pasos
#### 1. Crear una red en Docker: 
Crea una red en Docker llamada `mongodb-net` para que el contenedor de MongoDB y el de la API puedan comunicarse:

```bash
  docker network create mongodb-net
```

#### 2. Iniciar MongoDB en un contenedor: 
Utiliza la imagen oficial de MongoDB para crear un contenedor y asócialo a la red creada:

```bash
  docker run --name mongodb --network mongodb-net -d mongo
```

#### 3. Iniciar el contenedor de la API 
Ejecuta el contenedor de la API, asociándolo a la red mongodb-net y configurando las variables de entorno necesarias:
```bash
 docker run --name python-api --network mongodb-net -e MONGODB_HOST=mongodb -e MONGODB_PORT=27017 -d python-api
```

#### 4. Verificar los contenedores corriendo 
Puedes listar todos los contenedores que están corriendo para verificar que tanto `mongodb` como `python-api` están funcionando correctamente:

```bash
  docker ps
```

#### 5. Ejemplo de llamada al endpoint:
```bash
  http://host_my_api/guardar-lista-no-ordenada?lista-no-ordenada=[5,4,7,2,7,2]
```

#### 6. Respuesta del Endpoint:
Después de procesar la solicitud, el endpoint responde con un mensaje en formato JSON indicando que la lista ha sido guardada exitosamente junto con el ID generado. Ejemplo:
```json
  {
    "msg": "La lista ordenada fue guardada con el id: 9743ee94-6690-11ef-a4d5-089df4cb467e"
  }
```

#### 7. Apagar y eliminar los contenedores
Cuando termines de trabajar con los contenedores, puedes apagarlos y eliminarlos con los siguientes comandos:

```bash
docker stop python-api mongodb
docker rm python-api mongodb
```

# Datos de conexión con MongoDB:
La API utiliza las variables de entorno MONGODB_HOST y MONGODB_PORT para conectarse a MongoDB. Estas deben estar configuradas antes de correr el contenedor de la API. Para este ejercicio, los valores serían:

- `MONGODB_HOST`:`mongodb`
- `MONGODB_PORT`:`27017`



