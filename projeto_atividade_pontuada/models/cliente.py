from projeto_atividade_pontuada.models.fisica import Fisica
from projeto_atividade_pontuada.models.endereco import Endereco
from projeto_atividade_pontuada.models.enums.estado_civil import Estado_civil
from projeto_atividade_pontuada.models.enums.sexo import Sexo


class Cliente(Fisica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, dataNascimento: str, estado_civil: Estado_civil, sexo: Sexo, protocoloAtendimento: int, endereco: Endereco) -> None:
        super().__init__(id, nome, telefone, email, dataNascimento, estado_civil, sexo, endereco)

        self.protocoloAtemdimento = self.__verificar_protocolo_atendimento_cliente(protocoloAtendimento)

    def __verificar_protocolo_atendimento_cliente(self, protocoloAtendimento):
        if protocoloAtendimento < 0:
            raise ValueError("Não pode ser negativa.")
        if not isinstance(protocoloAtendimento, int):
            raise TypeError("Deve conter apenas número.")
        return protocoloAtendimento
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nProtocolo Atendimento: {self.protocoloAtemdimento}")