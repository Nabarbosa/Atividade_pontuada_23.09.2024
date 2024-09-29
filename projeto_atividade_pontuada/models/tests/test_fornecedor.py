import pytest

from projeto_atividade_pontuada.models.fornecedor import Fornecedor
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(333, "Valeria", "(71)90000-1111", "dorvaleria@gmail.com", "123.654", "15", "Café",
                            Endereco("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", Unidade_federativa.SAO_PAULO))
    return fornecedor

def test_fornecedor_id_valido(fornecedor_valido):
    assert fornecedor_valido.id == 333

def test_fornecedor_nome_valido(fornecedor_valido):
    assert fornecedor_valido.nome == "Valeria"

def test_fornecedor_telefone_valido(fornecedor_valido):
    assert fornecedor_valido.telefone == "(71)90000-1111"

def test_fornecedor_email_valido(fornecedor_valido):
    assert fornecedor_valido.email == "dorvaleria@gmail.com"

def test_fornecedor_cnpj_valido(fornecedor_valido):
    assert fornecedor_valido.cnpj == "123.654"

def test_fornecedor_inscricao_estadual_valido(fornecedor_valido):
    assert fornecedor_valido.inscricao_estadual == "15"

def test_cliente_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Café"

def test_endereco_fornecedor_logradouro_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.logradouro == "Rua Salgueiro"

def test_endereco_fornecedor_numero_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.numero == "14"

def test_endereco_fornecedor_complemento_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.complemento == "N/D"

def test_endereco_fornecedor_cep_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cep == "178.147.123"

def test_endereco_fornecedor_cidade_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.cidade == "São Paulo"

def test_endereco_fornecedor_uf_valido(fornecedor_valido):
    assert fornecedor_valido.endereco.uf == Unidade_federativa.SAO_PAULO

def test_advogado_oab_vazio_retorna_mensagem_excecao(fornecedor_valido):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Fornecedor(333, "Valeria", "(71)90000-1111", "dorvaleria@gmail.com", "123.654", "15", "",
                            Endereco("Rua Salgueiro", "14", "N/D", "178.147.123", "São Paulo", Unidade_federativa.SAO_PAULO))