from abc import ABC, abstractmethod
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.fisica import Fisica

class Funcionario(ABC, Fisica):
    def __init__(self, id: int, cpf: str, rg: str, matricula: str, nome: str, telefone: str, email: str,
                  dataNascimento: str, estado_civil: Estado_civil,sexo: Sexo, setor: Setor, salario: float,
                    endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, dataNascimento, estado_civil, sexo, endereco)
        self.cpf = self.__verificar_cpf
        self.rg = self.__verificar_rg
        self.matricula = self.__verificar_matricula
        self.setor = self.__verificar_setor
        self.salario = self.__verificar_salario

    def __verificar_salario(self, salario):
        if salario < 0:
            raise ValueError("Não pode ser negativa.")
        if not isinstance(salario, float):
            raise TypeError("Deve conter apenas número.")
        return salario
    
    def __verificar_cpf(self, cpf):
        if cpf == "":
            raise ValueError("O que está sendo solicitado está inválido")
        if not isinstance(cpf, str):
            raise TypeError("Valor inválido")
        return cpf
    
    def __verificar_rg(self, rg):
        if rg == "":
            raise ValueError("O que está sendo solicitado está inválido")
        if not isinstance(rg, str):
            raise TypeError("Valor inválido")
        return rg
    
    def __verificar_matricula(self, matricula):
        if matricula == "":
            raise ValueError("O que está sendo solicitado está inválido")
        if not isinstance(matricula, str):
            raise TypeError("Valor inválido")
        return matricula
    
    def __verificar_setor(self, setor):
        if setor == "":
            raise ValueError("O que está sendo solicitado está inválido")
        if not isinstance(setor, str):
            raise TypeError("Valor inválido")
        return setor

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor}"
                f"\nSalario: {self.salario}")