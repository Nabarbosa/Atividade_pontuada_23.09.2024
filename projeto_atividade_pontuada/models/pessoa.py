from abc import ABC,abstractmethod
from projeto_atividade_pontuada.models.endereco import Endereco

class Pessoa(ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.id = self.__verificar_id(id)
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __verificar_id(self, id):
        if id < 0:
            raise ValueError("Não pode ser negativa.")
        
        if not isinstance(id, int):
            raise TypeError("Deve conter apenas número.")
        return id
    
    def __str__(self) -> str:
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereço: {self.endereco}")
    

