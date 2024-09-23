from abc import ABC, abstractmethod
from models.pessoa import Pessoa
from models.enums.sexo import Sexo
from models.enums.estado_civil import Estado_civil

class Fisica(ABC):
    def __init__(self, dataNascimento: str, estado_civil: Estado_civil, sexo: Sexo) -> None:
        self.dataNascimento = dataNascimento
        self.estado_civil = estado_civil
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\nData de nascimento: {self.dataNascimento}"
                f"\nEstado Civil: {self.estado_civil.texto}"
                f"\nSexo: {self.sexo.texto} / {self.sexo.caracter}")
    
    