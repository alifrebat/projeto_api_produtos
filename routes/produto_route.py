# IMPORTAÇÃO DAS BIBLIOTECAS
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# IMPORTAÇÃO DOS ARQUIVOS DO PROJETO
from database import SessionLocal
from controllers.produto_controller import ProdutoController
from schemas.produto_schema import ProdutoSchema

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)

controller = ProdutoController()


# CONEXÃO COM BANCO
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# LISTAR
@router.get("/")
def listar(db: Session = Depends(get_db)):

    return controller.listar(db)


# CADASTRAR
@router.post("/")
def cadastrar(
    produto: ProdutoSchema,
    db: Session = Depends(get_db)
):

    return controller.cadastrar(db, produto)


# EXCLUIR
@router.delete("/{id}")
def excluir(
    id: int,
    db: Session = Depends(get_db)
):

    return controller.excluir(db, id)


# ALTERAR
@router.put("/{id}")
def alterar(
    id: int,
    produto: ProdutoSchema,
    db: Session = Depends(get_db)
):

    return controller.alterar(db, id, produto)