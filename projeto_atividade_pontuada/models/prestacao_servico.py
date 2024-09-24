from models.juridica import Juridica
from projeto_atividade_pontuada.models.endereco import Endereco
# Endereco?

class Prestacao_servico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, contratoInicio: str, contratoFim: str, cnpj: str, inscricao_estadual: str, endereco: Endereco, ) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Contrato Inicio: {self.contratoInicio}"
                f"Contrato Fim: {self.contratoFim}")

    
    