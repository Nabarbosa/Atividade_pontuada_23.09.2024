from enum import Enum

class Setor(Enum):
    ENGENHARIA = "Engenharia"
    SAUDE = "Saude"
    JURIDICO = "Juridico"

    def __init__(self, texto: str) -> None:
        self.texto = texto