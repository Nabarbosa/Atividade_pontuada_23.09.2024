from projeto_atividade_pontuada.models.funcionario import Funcionario
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.enums.sexo import Sexo

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, cpf: str, rg: str, matricula: str, telefone: str, email: str, dataNascimento: str, setor: Setor, salario: float, estado_civil: Estado_civil, sexo: Sexo, endereco: Endereco, crm: str) -> None:
        super().__init__(self._verificar_id_medico(id), self._verificar_nome_medico(nome), self._verificar_cpf_medico(cpf),
                          self._verificar_rg_medico(rg), self._verificar_matricula_medico(matricula), self._verificar_telefone_medico(telefone),
                          self._verificar_email_medico(email), self._verificar_data_nascimento_medico(dataNascimento), setor, 
                          self._verificar_salario_medico(salario), estado_civil, sexo, endereco)

        self.crm = self.__verificar_crm_medico(crm)

    def _verificar_id_medico(self, id):

        self._verificar_id_tipo_invalido(id)
        self._verificar_id_negativa(id)

        self.id = id
        return self.id
    
    def _verificar_salario_medico(self, salario):

        self._verificar_salario_tipo_invalido(salario)
        self._verificar_salario_negativo(salario)

        self.salario = salario
        return self.salario
    
    def _verificar_nome_medico(self, nome):

        self._verificar_nome_vazio_invalido(nome)

        self.nome = nome
        return self.nome


    def _verificar_id_tipo_invalido(self, id):
        if not isinstance(id, int):
            raise TypeError("O id deve ser um número inteiro.")

    def _verificar_id_negativa(self, id):
        if id <= 0:
            raise ValueError("O id não pode ser negativo.")
        
    def _verificar_nome_vazio_invalido(self, nome):
        if not nome.strip():
            raise TypeError("O nome não deve estar vazio.")
        return nome
    
    def _verificar_cpf_medico(self, cpf):
        if not cpf.strip():
            raise TypeError("O CPF não deve estar vazio.")
        return cpf
    
    def _verificar_rg_medico(self, rg):
        if not rg.strip():
            raise TypeError("O rg não deve estar vazio.")
        return rg
    
    def _verificar_matricula_medico(self, matricula):
        if not matricula.strip():
            raise TypeError("A matricula não deve estar vazia.")
        return matricula
    
    def _verificar_telefone_medico(self, telefone):
        if not telefone.strip():
            raise TypeError("O telefone não deve estar vazio.")
        return telefone
    
    def _verificar_email_medico(self, email):
        if not email.strip():
            raise TypeError("O e-mail não deve estar vazio.")
        return email
    
    def _verificar_data_nascimento_medico(self, dataNascimento):
        if not dataNascimento.strip():
            raise TypeError("A data de nascimento não deve estar vazia.")
        return dataNascimento
    
    def _verificar_salario_tipo_invalido(self, salario):
        if not isinstance(salario, float):
            raise TypeError("O salário deve ser um número real.")
        
    def _verificar_salario_negativo(self, salario):
        if salario <= 0:
            raise ValueError("O salário não deve ser negativo.")

    def __verificar_crm_medico(self, crm):
        if not crm.strip():
            raise ValueError("O CRM não deve ser vazio.")
        if not isinstance(crm, str):
            raise TypeError("valor inválido.")
        return crm

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}")