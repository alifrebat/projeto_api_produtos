from repositories.produto_repository import ProdutoRepository

class ProdutoService:
    #MÉTODO CONSTRUTOR INSTANCIANDO O OBJETO ProdutoRepository
    def __init__(self):
        self.repository = ProdutoRepository()

    #MÉTODO PARA VALIDAR A CONSULTA
    def listar(self, db)    :
        return self.repository.listar(db)
    
    #MÉTODO PARA VALIDAR CADASTRO
    def cadastrar(self, db, produto):
        return self.repository.cadastrar(db, produto)
    
    #MÉTODO PARA VALIDAR A EXCLUSÃO
    def excluir(self, db, id):
        return self.repository.excluir(db, id)
    
    #MÉTODO PARA VALIDAR ALTERAR
    def alterar(self, db, id, produto):
        return self.repository.alterar(db, id, produto)
