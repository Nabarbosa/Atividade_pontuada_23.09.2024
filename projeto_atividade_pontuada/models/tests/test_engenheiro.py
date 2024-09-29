import pytest

from projeto_atividade_pontuada.models.engenheiro import Engenheiro
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
    return engenheiro

def test_engenheiro_id_valido(engenheiro_valido):
    assert engenheiro_valido.id == 566

def test_engenheiro_nome_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "Amanda"

def test_advogado_cpf_valido(engenheiro_valido):
    assert engenheiro_valido.cpf == "999.123.781.21"

def test_engenheiro_rg_valido(engenheiro_valido):
    assert engenheiro_valido.rg == "147.666-12"

def test_engenheiro_matricula_valido(engenheiro_valido):
    assert engenheiro_valido.matricula == "031.123456"

def test_engenheiro_telefone_valido(engenheiro_valido):
    assert engenheiro_valido.telefone == "(71)90000-1111"

def test_advogado_email_valido(engenheiro_valido):
    assert engenheiro_valido.email == "engamanda@gmail.com"

def test_engenheiro_data_de_nascimento_valido(engenheiro_valido):
    assert engenheiro_valido.dataNascimento == "03/10/2000"

def test_engenheiro_setor_valido(engenheiro_valido):
    assert engenheiro_valido.setor == Setor.ENGENHARIA

def test_engenheiro_salario_valido(engenheiro_valido):
    assert engenheiro_valido.salario == 5400.0

def test_engenheiro_estado_civil_valido(engenheiro_valido):
    assert engenheiro_valido.estado_civil == Estado_civil.SOLTEIRO

def test_engenheiro_sexo_valido(engenheiro_valido):
    assert engenheiro_valido.sexo == Sexo.FEMININO

def test_endereco_engenheiro_logradouro_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.logradouro == "Rua Flores"

def test_endereco_engenheiro_numero_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.numero == "15"

def test_endereco_engenheiro_complemento_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.complemento == "N/D"

def test_endereco_engenheiro_cep_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cep == "400.356.236"

def test_endereco_engenheiro_cidade_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.cidade == "São Paulo"

def test_endereco_engenheiro_uf_valido(engenheiro_valido):
    assert engenheiro_valido.endereco.uf == Unidade_federativa.SAO_PAULO

def test_engenheiro_crea_valida(engenheiro_valido):
    assert engenheiro_valido.crea == "4523698"

def test_engenheiro_crea_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="O CREA não deve ser vazio."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "")
        
def test_engenheiro_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        Engenheiro(-566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")

def test_engenheiro_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        Engenheiro("566", "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
        
def test_engenheiro_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
     Engenheiro(566, "", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")  

def test_engenheiro_cpf_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CPF não deve estar vazio."):
        Engenheiro(566, "Amanda", "", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
        
def test_engenheiro_rg_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O rg não deve estar vazio."):
        Engenheiro(566, "Amanda", "999.123.781.21", "", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
        
def test_engenheiro_matricula_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A matricula não deve estar vazia."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
        
def test_engenheiro_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
        
def test_engenheiro_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "",
                         "03/10/2000", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
        
def test_engenheiro_data_nascimento_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento não deve estar vazia."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "", Setor.ENGENHARIA, 5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
        

def test_engenheiro_salario_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número real."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, "5400.0", Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")

def test_engenheiro_salario_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O salário não deve ser negativo."):
        Engenheiro(566, "Amanda", "999.123.781.21", "147.666-12", "031.123456", "(71)90000-1111", "engamanda@gmail.com",
                         "03/10/2000", Setor.ENGENHARIA, -5400.0, Estado_civil.SOLTEIRO, Sexo.FEMININO, 
                         Endereco("Rua Flores", "15", "N/D", "400.356.236", "São Paulo", Unidade_federativa.SAO_PAULO), "4523698")
