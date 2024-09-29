from projeto_atividade_pontuada.models.funcionario import Funcionario
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.enums.sexo import Sexo

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, cpf: str, rg: str, matricula: str, telefone: str, email: str, dataNascimento: str, setor: Setor, salario: float, estado_civil: Estado_civil, sexo: Sexo, endereco: Endereco, crm: str) -> None:
        super().__init__(id, nome, cpf, rg, matricula, telefone, email, dataNascimento, setor, salario, estado_civil, sexo, endereco)

        self.crm = self.__verificar_crm_medico(crm)

    def __verificar_crm_medico(self, crm):
        if crm == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(crm, str):
            raise TypeError("valor inválido.")
        return crm

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}")