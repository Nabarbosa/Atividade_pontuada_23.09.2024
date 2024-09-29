import pytest

from projeto_atividade_pontuada.models.medico import Medico
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.setor import Setor
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture
def medico_valido():
    medico = Medico(455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
    return medico

def test_medico_id_valido(medico_valido):
    assert medico_valido.id == 455

def test_medico_nome_valido(medico_valido):
    assert medico_valido.nome == "Carla"

def test_medico_cpf_valido(medico_valido):
    assert medico_valido.cpf == "888.777.666.55"

def test_medico_rg_valido(medico_valido):
    assert medico_valido.rg == "111.222-33"

def test_medico_matricula_valido(medico_valido):
    assert medico_valido.matricula == "010.123456"

def test_medico_telefone_valido(medico_valido):
    assert medico_valido.telefone == "(71)90000-1111"

def test_medico_email_valido(medico_valido):
    assert medico_valido.email == "medicarla@gmail.com"

def test_medico_data_de_nascimento_valido(medico_valido):
    assert medico_valido.dataNascimento == "14/03/1965"

def test_medico_setor_valido(medico_valido):
    assert medico_valido.setor == Setor.SAUDE

def test_medico_salario_valido(medico_valido):
    assert medico_valido.salario == 6000

def test_medico_estado_civil_valido(medico_valido):
    assert medico_valido.estado_civil == Estado_civil.DIVORCIADO

def test_medico_sexo_valido(medico_valido):
    assert medico_valido.sexo == Sexo.FEMININO

def test_endereco_medico_logradouro_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "Rua Vasco da Gama"

def test_endereco_medico_numero_valido(medico_valido):
    assert medico_valido.endereco.numero == "478"

def test_endereco_medico_complemento_valido(medico_valido):
    assert medico_valido.endereco.complemento == "N/D"

def test_endereco_medico_cep_valido(medico_valido):
    assert medico_valido.endereco.cep == "123.456.789"

def test_endereco_medico_cidade_valido(medico_valido):
    assert medico_valido.endereco.cidade == "Rio de Janeiro"

def test_endereco_medico_uf_valido(medico_valido):
    assert medico_valido.endereco.uf == Unidade_federativa.RIO_DE_JANEIRO

def test_medico_crm_valida(medico_valido):
    assert medico_valido.crm == "147852"

def test_medico_crm_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="O CRM não deve ser vazio."):
        Medico(455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "")
        
def test_medico_id_negativa_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O id não pode ser negativo."):
        Medico(-455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")

def test_medico_id_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O id deve ser um número inteiro."):
        Medico("455", "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
        
def test_medico_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não deve estar vazio."):
     Medico(455, "", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852") 

def test_medico_cpf_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O CPF não deve estar vazio."):
        Medico(455, "Carla", "", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
        
def test_medico_rg_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O rg não deve estar vazio."):
        Medico(455, "Carla", "888.777.666.55", "", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
        
def test_medico_matricula_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A matricula não deve estar vazia."):
        Medico(455, "Carla", "888.777.666.55", "111.222-33", "", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
        
def test_medico_telefone_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O telefone não deve estar vazio."):
        Medico(455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
        
def test_medico_email_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O e-mail não deve estar vazio."):
        Medico(455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "",
                    "14/03/1965", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
        
def test_medico_data_nascimento_vazio_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="A data de nascimento não deve estar vazia."):
        Medico(455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "", Setor.SAUDE, 6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
        

def test_medico_salario_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="O salário deve ser um número real."):
        Medico(455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, "6000.0", Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")

def test_medico_salario_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O salário não deve ser negativo."):
        Medico(455, "Carla", "888.777.666.55", "111.222-33", "010.123456", "(71)90000-1111", "medicarla@gmail.com",
                    "14/03/1965", Setor.SAUDE, -6000.0, Estado_civil.DIVORCIADO, Sexo.FEMININO, 
                    Endereco("Rua Vasco da Gama", "478", "N/D", "123.456.789", "Rio de Janeiro", Unidade_federativa.RIO_DE_JANEIRO), "147852")
