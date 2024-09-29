from projeto_atividade_pontuada.models.juridica import Juridica
from projeto_atividade_pontuada.models.endereco import Endereco

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, cnpj: str, inscricao_estadual: str, produto: str, endereco: Endereco,) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        
        self.produto = self.__verificar_produto_fornecedor(produto)

    def __verificar_produto_fornecedor(self, produto):
        if produto == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(produto, str):
            raise TypeError("valor inválido.")
        return produto

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nProduto: {self.produto}")