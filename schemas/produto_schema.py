from pydantic import BaseModel

class ProdutoSchema(BaseModel):
    descricaoproduto : str
    caracteristicasproduto : str
    valorunitario : float
    unidade : str
    tipoproduto : int
    
