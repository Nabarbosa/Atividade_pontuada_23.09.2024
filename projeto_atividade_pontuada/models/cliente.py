from models.fisica import Fisica

class Cliente:
    def __init__(self, protocoloAtendimento: int) -> None:
        self.protocoloAtemdimento = protocoloAtendimento

    def __str__(self) -> str:
        return (f"\nProtocolo atendimento: {self.protocoloAtemdimento}")