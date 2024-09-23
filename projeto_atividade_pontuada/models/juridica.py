from abc import ABC, abstractmethod
from models.pessoa import Pessoa

class Juridica(ABC):
    def __init__(self, cnpj: str, inscricao_estadual: str) -> None:
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual


