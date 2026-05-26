from sqlalchemy import Session

from models.produto_model import Produto

class ProdutoRespository:
    #LISTAR TODOS OS PRODUTOS
    def listar(self, db:Session):
        return db.query(Produto).all()
    
    #LISTAR UM PRODUTO
    def listar_id(self, db: Session, int: id):
        return db.query(Produto).filter(Produto.idprodutos == id).first()
    
    #CADASTRAR UM PRODUTO
    def cadastrar(self, db: Session, produto):
        novo_produto = Produto(
            descricaoproduto = produto.descricaoproduto, 
            caracteristicaproduto = produto.caracteristicaproduto,
            valorunitario = produto.valorunitario,
            unidade = produto.unidade,
            tipoproduto = produto.tipoproduto
        )

        db.add(novo_produto)
        db.commit()
        db.refresh(novo_produto)
        
        return novo_produto

    #EXCLUIR UM PRODUTO
    def excluir (self, db: Session, int: id):
        produto_bd  = self.listar_id(db, id)

        db.delete(produto_bd)
        db.commit()

        return{"Mensagem ": "Produto Excluído com Sucesso!"}
    
    #ALTERAR UM PRODUTO
    def alterar (self, db: Session, int: id, produto):
        produto_db = self.listar_id(db, id)
        
        produto_db.descricaoproduto = produto.descricaoproduto
        produto_db.caracteristicaproduto = produto.caracteristicaproduto
        produto_db.valorunitario = produto.valorunitario
        produto_db.unidade = produto.unidade
        produto_db.tipoproduto = produto.tipoproduto

        db.commit()
        db.refresh(produto_db)

        return produto_db



