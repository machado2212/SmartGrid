from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Minha Primeira API")

# Modelo de dados esperado no corpo da requisição
class Item(BaseModel):
    nome: str
    preco: float
    disponivel: bool = True

# Banco de dados simulado em memória
banco_de_dados: dict[int, Item] = {
    1: Item(nome="Teclado Mecânico", preco=250.0),
    2: Item(nome="Mouse Sem Fio", preco=120.0),
}

@app.get("/")
def home():
    return {"mensagem": "API online e funcionando!"}

@app.get("/itens")
def listar_itens():
    return banco_de_dados

@app.get("/itens/{item_id}")
def obter_item(item_id: int):
    if item_id not in banco_de_dados:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item não encontrado"
        )
    return banco_de_dados[item_id]

@app.post("/itens", status_code=status.HTTP_201_CREATED)
def criar_item(item: Item):
    novo_id = max(banco_de_dados.keys(), default=0) + 1
    banco_de_dados[novo_id] = item
    return {"id": novo_id, "item": item}