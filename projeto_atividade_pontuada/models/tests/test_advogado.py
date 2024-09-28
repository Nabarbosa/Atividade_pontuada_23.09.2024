import pytest

from projeto_atividade_pontuada.models.advogado import Advogado
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.enums.sexo import Sexo

@pytest.fixture
def advogado_valido():
    advogado = Advogado(211, "João", "456.123.785.21", "147.258-12", "031.145245", "(71)90000-1111", "adivajoao@gmail.com",
                         "12/07/1982", Setor.JURIDICO, 7200, Estado_civil.CASADO, Sexo.MASCULINO, 
                         Endereco("Rua S. José", "54", "N/D", "400.156.236", "Salvador", Unidade_federativa.BAHIA), "BA 123456")
    return advogado

def test_advogado_id_valido(advogado_valido):
    assert advogado_valido.id == 211

def test_advogado_nome_valido(advogado_valido):
    assert advogado_valido.nome == "João"

def test_advogado_cpf_valido(advogado_valido):
    assert advogado_valido.cpf == "456.123.785.21"

def test_advogado_rg_valido(advogado_valido):
    assert advogado_valido.rg == "147.258-12"

def test_advogado_matricula_valido(advogado_valido):
    assert advogado_valido.matricula == "031.145245"

def test_advogado_telefone_valido(advogado_valido):
    assert advogado_valido.telefone == "(71)90000-1111"

def test_advogado_email_valido(advogado_valido):
    assert advogado_valido.email == "adivajoao@gmail.com"

def test_advogado_data_de_nascimento_valido(advogado_valido):
    assert advogado_valido.dataNascimento == "12/07/1982"

def test_advogado_setor_valido(advogado_valido):
    assert advogado_valido.setor == Setor.JURIDICO

def test_advogado_salario_valido(advogado_valido):
    assert advogado_valido.salario == 7200

def test_advogado_estado_civil_valido(advogado_valido):
    assert advogado_valido.estado_civil == Estado_civil.CASADO

def test_advogado_sexo_valido(advogado_valido):
    assert advogado_valido.sexo == Sexo.MASCULINO

def test_endereco_advogado_logradouro_valido(advogado_valido):
    assert advogado_valido.endereco.logradouro == "Rua S. José"

def test_endereco_advogado_numero_valido(advogado_valido):
    assert advogado_valido.endereco.numero == "54"

def test_endereco_advogado_complemento_valido(advogado_valido):
    assert advogado_valido.endereco.complemento == "N/D"

def test_endereco_advogado_cep_valido(advogado_valido):
    assert advogado_valido.endereco.cep == "400.156.236"

def test_endereco_advogado_cidade_valido(advogado_valido):
    assert advogado_valido.endereco.cidade == "Salvador"

def test_endereco_advogado_uf_valido(advogado_valido):
    assert advogado_valido.endereco.uf == Unidade_federativa.BAHIA

def test_advogadoa_OAB_valida(advogado_valido):
    assert advogado_valido.oab == "BA 123456"


