from contextlib import asynccontextmanager
from schemas import SeriesDTO
from fastapi import FastAPI, HTTPException
import sqlite3
import json

series = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    global series
    with open("series.json", "r", encoding="utf-8") as arquivo:
        series = json.load(arquivo)
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    print(series)
    return {"mensagem": "Catálogo de Séries em construção"}


@app.post("/series")
def criar_series(serie_dto: SeriesDTO):
    dicionario_series = serie_dto.model_dump()
    series.append(dicionario_series)
    with open('series.json', 'w') as arquivo:
        json.dump(series, arquivo, indent=4)
    
    return {
        "mensagem": "Série cadastrada com sucesso!",
        "serie": dicionario_series
    }

@app.get("/series")
def listar_series():
    with open('series.json', 'r') as arquivo:
        arquivo_lido = json.load(arquivo)
    if not arquivo_lido:
        return []
    else:
        return arquivo_lido

@app.get("/series/{titulo}")
def buscar_serie(titulo: str):
    conexao = sqlite3.connect('series.db')
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM catalogo WHERE LOWER(titulo) = LOWER(?)",
        (titulo,)
    )

    serie = cursor.fetchone()
    conexao.close()

    if serie is None:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    return serie
