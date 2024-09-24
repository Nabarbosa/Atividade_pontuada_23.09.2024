from projeto_atividade_pontuada.models.funcionario import Funcionario
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.enums.sexo import Sexo


class Advogado(Funcionario):
    def __init__(self, sexo: Sexo, estado_civil: Estado_civil, cpf: str, rg: str, matricula: str, setor: Setor, 
                 salario: float, oab: str, endereco: Endereco) -> None:
        super().__init__(cpf, rg, matricula, setor, salario)
        self.oab = oab
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nOAB: {self.oab}"
                f"\nSexo: {self.sexo.texto}"
                f"\nEstado Civil: {self.estado_civil.texto}"
                f"\nEndereço: {self.endereco}")