from projeto_atividade_pontuada.models.juridica import Juridica
from projeto_atividade_pontuada.models.endereco import Endereco
# Endereco?

class Prestacao_servico(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, contratoInicio: str, contratoFim: str, cnpj: str, inscricao_estadual: str, endereco: Endereco, ) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricao_estadual)
        self.contratoInicio = self.__verificar_contrato_inicio(contratoInicio)
        self.contratoFim = self.__verificar_contrato_fim(contratoFim)

    def __verificar_contrato_inicio(self, contratoInicio):
        if contratoInicio == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(contratoInicio, str):
            raise TypeError("valor inválido.")
        return contratoInicio
    
    def __verificar_contrato_fim(self, contratoFim):
        if contratoFim == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(contratoFim, str):
            raise TypeError("valor inválido.")
        return contratoFim

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Contrato Inicio: {self.contratoInicio}"
                f"Contrato Fim: {self.contratoFim}")

    
    