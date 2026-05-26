from sqlalchemy import Column, Integer, String, DECIMAL

from database import Base

class Produto(Base):
    __tablename__ = "produtos"
    idprodutos = Column(Integer, primary_key=True, index=True)
    descricaoproduto = Column(String(30))
    caracteristicasproduto = Column(String(200))
    valorunitario = Column(DECIMAL(10,2))
    unidade = Column(String(10))
    tipoproduto = Column(Integer)
    

