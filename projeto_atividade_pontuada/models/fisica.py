from abc import ABC, abstractmethod
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.pessoa import Pessoa
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil


class Fisica(ABC, Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, dataNascimento: str, estado_civil: Estado_civil, sexo: Sexo, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.dataNascimento = dataNascimento
        self.estado_civil = estado_civil
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nData de nascimento: {self.dataNascimento}"
                f"\nEstado Civil: {self.estado_civil.texto}"
                f"\nSexo: {self.sexo.texto} / {self.sexo.caracter}")
    