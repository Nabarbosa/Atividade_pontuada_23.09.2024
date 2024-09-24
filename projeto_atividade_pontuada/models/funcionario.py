from abc import ABC, abstractmethod
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.fisica import Fisica

class Funcionario(ABC, Fisica):
    def __init__(self, id: int, cpf: str, rg: str, matricula: str, nome: str, telefone: str, email: str,
                  dataNascimento: str, estado_civil: Estado_civil,sexo: Sexo, setor: Setor, salario: str,
                    endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, dataNascimento, estado_civil, sexo, endereco)
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalario: {self.salario}")