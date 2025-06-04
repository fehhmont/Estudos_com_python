from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False

app = FastAPI()

produtos = [
    Produto(id=1, nome='Playstation 5',preco=44.55,em_oferta=True),
    Produto(id=2, nome='Playstation 4',preco=34.55),
    Produto(id=3, nome='Playstation 3',preco=64.55,em_oferta=True),
    Produto(id=4, nome='Playstation 2',preco=74.55),
]

@app.get('/')
async def index():
    return{"Felipe": "Anthonyy"}

@app.get('/produtos/{id}')
async def buscar_produto(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
    return None

@app.put('/produtos/{id}')
async def atualizar_produto(id:int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto

            return prod
    return None
