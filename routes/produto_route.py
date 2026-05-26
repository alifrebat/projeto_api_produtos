#IMPORTAÇÃO DAS BIBLIOTECAS
from fastapi import APIRouter
from sqlalchemy import Session 

#IMPORTAÇÃO DOS ARQUVIOS DO PROJETO
from database import SessionLocal
from controllers.produto_controller import ProdutoController
from schemas.produto_schema import ProdutoSchema

router = APIRouter(
    prefix = "/produtos",
    tags = ["Produtos"]
)

controller = ProdutoController()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/")
def listar():
    db = next(get_db)
    return controller.listar(db)

@router.post("/")
def cadastrar(produto: ProdutoSchema):
    db = next(get_db)
    return controller.cadastrar(db, produto)

@router.delete("/{id}")
def excluir(id: int):
    db = next(get_db)
    return controller.excluir(db, id)

@router.put("/{id}")
def alterar(id, produto: ProdutoSchema):
    db = next(get_db)
    return controller.alterar(db, id, produto)

