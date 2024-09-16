from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import threading
from produtor import publicar_mensagem
from consumidor import consumir_mensagens

app = FastAPI()

# comunicacao com a API
origins = [
    "http://localhost",  # frontend local
    "http://localhost:8000",  # api local
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# enviar mensagem
@app.post("/enviar/")
async def enviar_mensagem(mensagem: str):
    publicar_mensagem(mensagem)
    return {"status": "Mensagem enviada"}

#consumir mensagens
@app.get("/consumir/")
async def consumir():
    threading.Thread(target=consumir_mensagens).start()
    return {"mensagens": ["Exemplo de mensagem 1", "Exemplo de mensagem 2"]}

# comando p rodar uvicorn api-gateway.py:app --reload