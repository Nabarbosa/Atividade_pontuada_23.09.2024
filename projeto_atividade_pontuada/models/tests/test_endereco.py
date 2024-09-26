import pytest

from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def endereco_valida():
    endereco = Endereco("Rua A", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA.nome)
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
    assert endereco_valida.uf == Unidade_federativa.BAHIA.nome

def test_endereco_logradouro_vazio_retorna_mensagem_excecao(endereco_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."): 
        Endereco("", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA)
        
def test_endereco_numero_vazio_retorna_mensagem_excecao(endereco_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."): 
        Endereco("Rua A", "", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA)
        
def test_endereco_complemento_vazio_retorna_mensagem_excecao(endereco_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."): 
        Endereco("Rua A", "15", "", "123456", "Cidade A", 
            Unidade_federativa.BAHIA)
        
def test_endereco_cep_vazio_retorna_mensagem_excecao(endereco_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."): 
        Endereco("Rua A", "15", "N/D", "", "Cidade A", 
            Unidade_federativa.BAHIA)
        
def test_endereco_cidade_vazio_retorna_mensagem_excecao(endereco_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."): 
        Endereco("Rua A", "15", "N/D", "123456", "", 
            Unidade_federativa.BAHIA)
        

            
