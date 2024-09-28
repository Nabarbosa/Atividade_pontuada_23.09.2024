import pytest

from projeto_atividade_pontuada.models.prestacao_servico import Prestacao_servico
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def prestacao_servico_valido():
    prestacao_servico = Prestacao_servico(333, "Valeria", "(71)90000-1111", "dorvaleria@gmail.com", "20/04/2000", "20/04/2030", "123.654", "15",
                            Endereco("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", Unidade_federativa.SAO_PAULO))
    return prestacao_servico

def test_prestacao_servico_id_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.id == 333

def test_prestacao_servico_nome_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.nome == "Valeria"

def test_prestacao_servico_telefone_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.telefone == "(71)90000-1111"

def test_prestacao_servico_email_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.email == "dorvaleria@gmail.com"

def test_prestacao_servico_contrato_inicio_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.contratoInicio == "20/04/2000"

def test_prestacao_servico_contrato_Fim_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.contratoFim == "20/04/2030"

def test_prestacao_servico_cnpj_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.cnpj == "123.654"

def test_prestacao_servico_inscricao_estadual_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.inscricao_estadual == "15"

def test_endereco_prestacao_servico_logradouro_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.logradouro == "Rua Salgueiro"

def test_endereco_prestacao_servico_numero_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.numero == "14"

def test_endereco_prestacao_servico_complemento_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.complemento == "N/D"

def test_endereco_prestacao_servico_cep_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.cep == "178.147.123"

def test_endereco_prestacao_servico_cidade_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.cidade == "São Paulo"

def test_endereco_prestacao_servico_uf_valido(prestacao_servico_valido):
    assert prestacao_servico_valido.endereco.uf == Unidade_federativa.SAO_PAULO