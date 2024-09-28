from projeto_atividade_pontuada.models.juridica import Juridica
from projeto_atividade_pontuada.models.endereco import Endereco

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricao_estadual: str, produto: str, endereco: Endereco,) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        
        self.produto = produto

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nProduto: {self.produto}")