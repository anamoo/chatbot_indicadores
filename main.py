from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bot import procesar_mensaje

app = FastAPI()

# permitir conexión con la página web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")

def chat(mensaje: dict):

    texto = mensaje["texto"]

    respuesta = procesar_mensaje(texto)

    return respuesta