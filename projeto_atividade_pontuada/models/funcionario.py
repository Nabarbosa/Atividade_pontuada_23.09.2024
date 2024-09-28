from abc import ABC, abstractmethod
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.fisica import Fisica

class Funcionario(Fisica):
    def __init__(self, id: int, nome: str, cpf: str, rg: str, matricula: str, telefone: str, email: str, 
                 dataNascimento: str, setor: Setor, salario: float, estado_civil: Estado_civil, sexo: Sexo, endereco: Endereco) -> None:
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