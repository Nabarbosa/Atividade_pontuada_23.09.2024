from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino", "M")
    FEMININO = ("Feminino", "F")

    def __init__(self, texto_sexo: str, caracter: str) -> None:
        self.texto = texto_sexo
        self.caracter = caracter