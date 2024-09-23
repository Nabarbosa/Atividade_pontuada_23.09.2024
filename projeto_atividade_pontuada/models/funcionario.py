from abc import ABC, abstractmethod
from models.enums.setor import Setor
from models.fisica import Fisica

class Funcionario(ABC):
    def __init__(self, cpf: str, rg:str, matricula:str, setor: Setor, salario: float) -> None:
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalario: {self.salario}")