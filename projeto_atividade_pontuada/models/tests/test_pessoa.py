import pytest
from projeto_atividade_pontuada.models.pessoa import Pessoa
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa(20, "Marta", "789456123", "marta@gmail.com", 
            Endereco("Rua A", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA))
    return pessoa

def test_pessoa_id_valido(pessoa_valida):
    assert pessoa_valida.id == 20

def test_pessoa_nome_valida(pessoa_valida):
    assert pessoa_valida.nome == "Marta"

def test_pessoa_telefone_valida(pessoa_valida):
    assert pessoa_valida.telefone == "789456123"

def test_pessoa_email_valida(pessoa_valida):
    assert pessoa_valida.email == "marta@gmail.com"

def test_pessoa_idade_negativa_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="Não pode ser negativa."):
        Pessoa(-20, "Marta", "789456123", "marta@gmail.com", 
            Endereco("Rua A", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA))
        
def test_pessoa_nome_vazio_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Pessoa(20, "", "789456123", "marta@gmail.com", 
            Endereco("Rua A", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA))

def test_pessoa_telefone_vazio_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Pessoa(20, "Marta", "", "marta@gmail.com", 
            Endereco("Rua A", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA))
        
def test_pessoa_email_vazio_retorna_mensagem_excecao(pessoa_valida):
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Pessoa(20, "Marta", "789456123", "", 
            Endereco("Rua A", "15", "N/D", "123456", "Cidade A", 
            Unidade_federativa.BAHIA))
        
        