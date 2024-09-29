from projeto_atividade_pontuada.models.fisica import Fisica
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo


class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, dataNascimento: str, estado_civil: Estado_civil, sexo: Sexo, protocoloAtendimento: int, endereco: Endereco) -> None:
        super().__init__(self._verificar_id(id), self._verificar_nome(nome), self._verificar_telefone(telefone), self._verificar_email(email), 
                         self._verificar_data_nascimento(dataNascimento), estado_civil, sexo, endereco)

        self.protocoloAtemdimento = self.__verificar_protocolo_atendimento_cliente(protocoloAtendimento)
        
    def __verificar_protocolo_atendimento_cliente(self, protocoloAtendimento):

        self._verificar_protocolo_tipo_invalido(protocoloAtendimento)
        self._verificar_protocolo_negativo(protocoloAtendimento)

        self.protocoloAtemdimento = protocoloAtendimento
        return self.protocoloAtemdimento
    
    def _verificar_id(self, id):

        self._verificar_id_tipo_invalido(id)
        self._verificar_id_negativa(id)

        self.id = id
        return self.id
    
    def _verificar_nome(self, nome):

        self._verificar_nome_vazio_invalido(nome)

        self.nome = nome
        return self.nome


    def _verificar_id_tipo_invalido(self, id):
        if not isinstance(id, int):
            raise TypeError("O id deve ser um número inteiro.")

    def _verificar_id_negativa(self, id):
        if id <= 0:
            raise ValueError("O id não pode ser negativo.")
        
    def _verificar_nome_vazio_invalido(self, nome):
        if nome == "":
            raise TypeError("O nome não deve estar vazio.")
        return nome
    
    def _verificar_telefone(self, telefone):
        if telefone == "":
            raise TypeError("O telefone não deve estar vazio.")
        return telefone
    
    def _verificar_email(self, email):
        if email == "":
            raise TypeError("O e-mail não deve estar vazio.")
        return email
    
    def _verificar_data_nascimento(self, dataNascimento):
        if dataNascimento == "":
            raise TypeError("A data de nascimento não deve estar vazia.")
        return dataNascimento
    
    def _verificar_protocolo_tipo_invalido(self, protocoloAtendimento):
        if not isinstance(protocoloAtendimento, int):
            raise TypeError("O protocolo de atendimento deve ser um número inteiro.")

    def _verificar_protocolo_negativo(self, protocoloAtendimento):
        if protocoloAtendimento <= 0:
            raise ValueError("O protocolo de atendimento não pode ser negativo.")
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nProtocolo Atendimento: {self.protocoloAtemdimento}")