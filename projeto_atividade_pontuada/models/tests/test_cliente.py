import pytest

from projeto_atividade_pontuada.models.cliente import Cliente
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def cliente_valido():
    cliente = Cliente(200, "Marcos", "(71)91111-0000", "temarcos@gmail.com", "21/12/1998", Estado_civil.SEPARADO, Sexo.MASCULINO, 
                      145, Endereco("Rua Santos", "468", "N/D", "789.456.123", "Salvador", Unidade_federativa.BAHIA))
    return cliente

def test_cliente_id_valido(cliente_valido):
    assert cliente_valido.id == 200

def test_cliente_nome_valido(cliente_valido):
    assert cliente_valido.nome == "Marcos"

def test_cliente_telefone_valido(cliente_valido):
    assert cliente_valido.telefone == "(71)91111-0000"

def test_advogado_email_valido(cliente_valido):
    assert cliente_valido.email == "temarcos@gmail.com"

def test_engenheiro_data_de_nascimento_valido(cliente_valido):
    assert cliente_valido.dataNascimento == "21/12/1998"

def test_cliente_estado_civil_valido(cliente_valido):
    assert cliente_valido.estado_civil == Estado_civil.SEPARADO

def test_cliente_sexo_valido(cliente_valido):
    assert cliente_valido.sexo == Sexo.MASCULINO

def test_cliente_protocolo_de_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloAtemdimento == 145

def test_endereco_cliente_logradouro_valido(cliente_valido):
    assert cliente_valido.endereco.logradouro == "Rua Santos"

def test_endereco_cliente_numero_valido(cliente_valido):
    assert cliente_valido.endereco.numero == "468"

def test_endereco_cliente_complemento_valido(cliente_valido):
    assert cliente_valido.endereco.complemento == "N/D"

def test_endereco_cliente_cep_valido(cliente_valido):
    assert cliente_valido.endereco.cep == "789.456.123"

def test_endereco_cliente_cidade_valido(cliente_valido):
    assert cliente_valido.endereco.cidade == "Salvador"

def test_endereco_cliente_uf_valido(cliente_valido):
    assert cliente_valido.endereco.uf == Unidade_federativa.BAHIA

def test_protocolo_atendimento_negativa_retorna_mensagem_excecao(cliente_valido):
    with pytest.raises(ValueError, match="Não pode ser negativa."):
        Cliente(200, "Marcos", "(71)91111-0000", "temarcos@gmail.com", "21/12/1998", Estado_civil.SEPARADO, Sexo.MASCULINO, 
                      -145, Endereco("Rua Santos", "468", "N/D", "789.456.123", "Salvador", Unidade_federativa.BAHIA))
