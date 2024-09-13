from fastapi import FastAPI, Query
from datetime import datetime
from pymongo import MongoClient
import uuid
import os

app = FastAPI()

# Configuración de la conexión a MongoDB usando variables de entorno
mongodb_host = os.getenv('MONGODB_HOST', 'localhost')
mongodb_port = int(os.getenv('MONGODB_PORT', 27017))
client = MongoClient(f"mongodb://{mongodb_host}:{mongodb_port}/")
db = client["python_app"]
collection = db["listas_no_ordenadas"]

@app.get("/lista-ordenada")
def lista_ordenada(lista_no_ordenada: str = Query(..., alias="lista-no-ordenada")):
    lista_no_ordenada = lista_no_ordenada.strip('[]').split(',')
    lista_no_ordenada = [int(i) for i in lista_no_ordenada]
    lista_ordenada = sorted(lista_no_ordenada)

    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    respuesta = {
        "hora_sistema": hora_sistema,
        "lista_ordenada": lista_ordenada
    }

    return respuesta

@app.get("/guardar-lista-no-ordenada")
def guardar_lista(lista_no_ordenada: str = Query(..., alias="lista-no-ordenada")):
    # Convertir la lista de string a una lista de enteros
    lista_no_ordenada = lista_no_ordenada.strip('[]').split(',')
    lista_no_ordenada = [int(i) for i in lista_no_ordenada]

    # Obtener la hora actual y generar un UUID
    hora_sistema = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_documento = str(uuid.uuid4())

    # Crear el documento a insertar
    documento = {
        "_id": id_documento,
        "lista_no_ordenada": lista_no_ordenada,
        "hora_sistema": hora_sistema
    }

    # Insertar el documento en la colección
    result = collection.insert_one(documento)

    # Respuesta personalizada con el ID
    return {"msg": f"La lista no ordenada fue guardada con el id: {result.inserted_id}"}

@app.get("/healthcheck")
def healthcheck():
    respuesta = "OK"

    return respuesta