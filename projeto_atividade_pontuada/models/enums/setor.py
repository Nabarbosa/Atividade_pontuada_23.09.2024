from enum import Enum

class Setor(Enum):
    ENGENHARIA = "Engenharia"
    SAUDE = "Saude"
    JURIDICO = "Juridico"

    def __init__(self, texto_setor: str) -> None:
        self.texto = texto_setor