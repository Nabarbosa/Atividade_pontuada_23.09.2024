import pytest 
from projeto_atividade_pontuada.models.funcionario import Funcionario
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo
from projeto_atividade_pontuada.models.enums.setor import Setor
# from projeto_atividade_pontuada.models.fisica import Fisica
from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

@pytest.fixture 
def funcionario_valido():
    funcionario = Funcionario(20, "027.359.147-21", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
                              Estado_civil.VIUVO, Sexo.FEMININO, Setor.JURIDICO, 5000, Endereco("Rua A", "15", "N/D", "123456", "Cidade A", Unidade_federativa.BAHIA))
    return funcionario

# @pytest.fixture
# def funcionario_fisico_valido():
#     funcionario_fisico = Fisica(20, "027.359.147-21", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
#                               Estado_civil.VIUVO, Sexo.FEMININO, Setor.JURIDICO, 5000, Endereco("Rua A", "15", "N/D", "123456", "Cidade A", Unidade_federativa.BAHIA))
#     return funcionario_fisico

def test_funcionario_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 5000

def test_fncionario_cpf_valido(funcionario_valido):
    assert funcionario_valido.cpf == "027.359.147-21"

def test_funcionario_rg_valido(funcionario_valido):
    assert funcionario_valido.rg == "25.147.987-25"

def test_funcionario_matricula_valido(funcionario_valido):
    assert funcionario_valido.matricula == "4101"

def test_funcionario_setor_valido(funcionario_valido):
    assert funcionario_valido.setor == Setor.JURIDICO

# def test_funcionario_data_de_nascimento_valido(funcionario_valido):
#     assert funcionario_valido.dataNascimento == "08/01/2000"

# def test_funcionario_estado_civil_valido(funcionario_valido):
#     assert funcionario_valido.estado_civil == Estado_civil.VIUVO

# def test_funcionario_sexo_valido(funcionario_valido):
#     assert funcionario_valido.sexo == Sexo.FEMININO

def test_funcionario_salario_negativa_retorna_mensagem_excecao(funcionario_valido):
    with pytest.raises(ValueError, match="Não pode ser negativa."):
        Funcionario(20, "027.359.147-21", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
                    Estado_civil.VIUVO, Sexo.FEMININO, Setor.JURIDICO, -5000, 
                    Endereco("Rua A", "15", "N/D", "123456", "Cidade A", Unidade_federativa.BAHIA))
        
def test_funcionario_cpf_retorna_mensagem_excecao(funcionario_valido):
    with pytest.raises(ValueError, match="Não pode ser vazia."):
        Funcionario(20, "", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
                    Estado_civil.VIUVO, Sexo.FEMININO, Setor.JURIDICO, 5000, 
                    Endereco("Rua A", "15", "N/D", "123456", "Cidade A", Unidade_federativa.BAHIA))
        
def test_funcionario_rg_retorna_mensagem_excecao(funcionario_valido):
    with pytest.raises(ValueError, match="Não pode ser vazia."):
        Funcionario(20, "027.359.147-21", "", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
                    Estado_civil.VIUVO, Sexo.FEMININO, Setor.JURIDICO, 5000, 
                    Endereco("Rua A", "15", "N/D", "123456", "Cidade A", Unidade_federativa.BAHIA))
        
def test_funcionario_setor_retorna_mensagem_excecao(funcionario_valido):
    with pytest.raises(ValueError, match="Não pode ser vazia."):
        Funcionario(20, "027.359.147-21", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
                    Estado_civil.VIUVO, Sexo.FEMININO, 5000, 
                    Endereco("Rua A", "15", "N/D", "123456", "Cidade A", ))
        
# def test_funcionario_data_nascimento_retorna_mensagem_excecao(funcionario_valido):
#     with pytest.raises(ValueError, match="Não pode ser vazia."):
#         Funcionario(20, "027.359.147-21", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "", 
#                     Estado_civil.VIUVO, Sexo.FEMININO, Setor.JURIDICO, 5000, 
#                     Endereco("Rua A", "15", "N/D", "123456", "Cidade A", ))
        
# def test_funcionario_estado_civil_retorna_mensagem_excecao(funcionario_valido):
#     with pytest.raises(ValueError, match="Não pode ser vazia."):
#         Funcionario(20, "027.359.147-21", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
#                     Sexo.FEMININO, Setor.JURIDICO, 5000, 
#                     Endereco("Rua A", "15", "N/D", "123456", "Cidade A", ))
        
# def test_funcionario_sexo_retorna_mensagem_excecao(funcionario_valido):
#     with pytest.raises(ValueError, match="Não pode ser vazia."):
#         Funcionario(20, "027.359.147-21", "25.147.987-25", "4101","Marta", "789456123", "marta@gmail.com", "08/01/2000", 
#                     Estado_civil.VIUVO, Setor.JURIDICO, 5000, 
#                     Endereco("Rua A", "15", "N/D", "123456", "Cidade A", ))
            