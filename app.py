from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI()

# Permite que o navegador se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Carrega base de conhecimento
with open("base_conhecimento.json", "r", encoding="utf-8") as f:
    conhecimento = json.load(f)

@app.post("/perguntar")
async def perguntar(request: Request):
    dados = await request.json()
    pergunta = dados.get("pergunta", "").lower()

    resposta = conhecimento.get(pergunta, "Desculpe, ainda não sei responder isso.")
    return {"resposta": resposta}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)