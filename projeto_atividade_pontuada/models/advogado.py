from projeto_atividade_pontuada.models.funcionario import Funcionario
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.enums.sexo import Sexo

class Advogado(Funcionario):
    def __init__(self, id: int, nome: str, cpf: str, rg: str, matricula: str, telefone: str, email: str, dataNascimento: str, setor: Setor, salario: float, estado_civil: Estado_civil, sexo: Sexo, endereco: Endereco, oab: str) -> None:
        super().__init__(id, nome, cpf, rg, matricula, telefone, email, dataNascimento, setor, salario, estado_civil, sexo, endereco)
        
        self.oab = oab

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nOAB: {self.oab}")