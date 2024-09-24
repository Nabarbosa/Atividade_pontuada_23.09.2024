from abc import ABC, abstractmethod
from projeto_atividade_pontuada.models.pessoa import Pessoa
from projeto_atividade_pontuada.models.endereco import Endereco

class Juridica(ABC, Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricao_estadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCNPJ: {self.cnpj}"
                f"\nInscrição Estadual: {self.inscricao_estadual}")


