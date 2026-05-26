from services.produto_service import ProdutoService

class ProdutoController:
    #MÉTODOS CONSTRUTOR CRIANDO O OBJETO ProdutoService
    def __init__(self):
        self.service = ProdutoService()
    
    #MÉTODO DE CONTROLE LISTAR
    def listar(self, db):
        return self.service.listar(db)
    
    #MÉTODO DE CONTROLE CADASTRAR
    def cadastrar(self, db, produto):
        return self.service.cadastrar(db, produto)
    
    #MÉTODO DE CONTROLE PARA EXCLUIR
    def excluir(self, db, id):
        return self.service.alterar(db, id)
    
    #MÉTODOS DE CONTROLE PARA ALTERAR
    def alterar(self, db, id, produto):
        return self.service.alterar(db, id, produto)
    