from enum import Enum

class Estado_civil(Enum):
    SOLTEIRO = "Solteira"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viuvo"

    def __init__(self, texto:str) -> None:
        self.texto = texto