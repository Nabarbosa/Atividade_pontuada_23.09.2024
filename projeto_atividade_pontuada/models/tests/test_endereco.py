import pytest

from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def endereco_valida():
    endereco = Endereco("Rua A", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA)
    return endereco

def test_endereco_logradouro_valido(endereco_valida):
    assert endereco_valida.logradouro == "Rua A"

def test_endereco_numero_valido(endereco_valida):
    assert endereco_valida.numero == "15"

def test_endereco_complemento_valido(endereco_valida):
    assert endereco_valida.complemento == "N/D"

def test_endereco_cep_valido(endereco_valida):
    assert endereco_valida.cep == "123456"

def test_endereco_cidade_valido(endereco_valida):
    assert endereco_valida.cidade == "Cidade A"

def test_endereco_uf_valido(endereco_valida):
    assert endereco_valida.uf == Unidade_federativa.BAHIA

            
