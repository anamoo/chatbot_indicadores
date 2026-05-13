from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bot import procesar_mensaje

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

# permitir conexión con la página web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")

def chat(mensaje: dict):

    texto = mensaje["texto"]

    respuesta = procesar_mensaje(texto)

    return respuesta