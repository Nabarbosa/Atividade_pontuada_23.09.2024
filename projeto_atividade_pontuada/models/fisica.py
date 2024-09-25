from abc import ABC, abstractmethod
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.pessoa import Pessoa
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil


class Fisica(ABC, Pessoa):
    def __init__(self, id: int, nome: str, telefone: str, email: str, dataNascimento: str, estado_civil: Estado_civil, sexo: Sexo, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.dataNascimento = self.__verificar_dataNascimento(dataNascimento)
        self.estado_civil = self.__verificar_estado_civil(estado_civil)
        self.sexo = self.__verificar_sexo(sexo)

    def __verificar_dataNascimento(self, dataNascimento):
        if dataNascimento == "":
            raise ValueError("O que está sendo solicitado está inválido")
        if not isinstance(dataNascimento, str):
            raise TypeError("Valor inválido")
        return dataNascimento
    
    def __verificar_estado_civil(self, estado_civil):
        if estado_civil == "":
            raise ValueError("O que está sendo solicitado está inválido")
        if not isinstance(estado_civil, str):
            raise TypeError("Valor inválido")
        return estado_civil
    
    def __verificar_sexo(self, sexo):
        if sexo == "":
            raise ValueError("O que está sendo solicitado está inválido")
        if not isinstance(sexo, str):
            raise TypeError("Valor inválido")
        return sexo

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nData de nascimento: {self.dataNascimento}"
                f"\nEstado Civil: {self.estado_civil.texto}"
                f"\nSexo: {self.sexo.texto} / {self.sexo.caracter}")
    