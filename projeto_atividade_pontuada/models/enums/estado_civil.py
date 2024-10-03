from enum import Enum

class Estado_civil(Enum):
    SOLTEIRO = "Solteiro"
    CASADO = "Casado"
    SEPARADO = "Separado"
    DIVORCIADO = "Divorciado"
    VIUVO = "Viuvo"

    def __init__(self, texto_estadoCivil:str) -> None:
        self.texto = texto_estadoCivil