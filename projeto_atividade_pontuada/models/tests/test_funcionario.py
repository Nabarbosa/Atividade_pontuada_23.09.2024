import pytest

from projeto_atividade_pontuada.models.funcionario import Funcionario
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.setor import Setor

@pytest.fixture
def funcionario_valido():
    funcionaro = Funcionario(20, "123456789", "123654","011", "Marta", "956231245", "marta@gmail.com", "24/02/1999", 
                             Estado_civil.CASADO.texto, Sexo.FEMININO.texto, Setor.JURIDICO.texto, 5.000, 
                             Endereco("Rua A", "12", "N/D", "45612389", "Cidade A", Unidade_federativa.BAHIA.nome)
                             )
    return funcionaro

#cpf, rg, matricula, setor, salario

def teste_funcionario_cpf_valido(funcionario_valido):
    assert funcionario_valido.cpf == "123456789"

def test_funcionario_rg_valido(funcionario_valido):
    assert funcionario_valido.rg == "123654"

def test_funcionario_matricula_valido(funcionario_valido):
    assert funcionario_valido.matricula == "011"

def test_funcionario_setor_valido(funcionario_valido):
    assert funcionario_valido.setor == Setor.JURIDICO.texto

def test_funcionario_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 5.000