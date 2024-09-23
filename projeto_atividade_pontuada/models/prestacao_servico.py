from models.juridica import Juridica

class Prestacao_servico:
    def __init__(self, contratoInicio: str, contratoFim: str) -> None:
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (f"Contrato Inicio: {self.contratoInicio}"
                f"Contrato Fim: {self.contratoFim}")