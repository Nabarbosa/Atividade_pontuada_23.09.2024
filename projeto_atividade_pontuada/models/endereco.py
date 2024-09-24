from projeto_atividade_pontuada.models.enums.unidade_federativa import Unidade_federativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: Unidade_federativa) -> None:
        self.logradouro = self.__verificar_logradouro_endereco(logradouro)
        self.numero = self.__verificar_numero_endereco(numero)
        self.complemento = self.__verificar_complemento_endereco(complemento)
        self.cep = self.__verificar_cep_endereco(cep)
        self.cidade = self.__verificar_cidade_endereco(cidade)
        self.uf = uf

    def __verificar_logradouro_endereco(self, logradouro):
        if logradouro == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(logradouro, str):
            raise TypeError("valor inválido.")
        return logradouro
    
    def __verificar_numero_endereco(self, numero):
        if numero == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(numero, str):
            raise TypeError("valor inválido.")
        return numero
    
    def __verificar_complemento_endereco(self, complemento):
        if complemento == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(complemento, str):
            raise TypeError("valor inválido.")
        return complemento
    
    def __verificar_cep_endereco(self, cep):
        if cep == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(cep, str):
            raise TypeError("valor inválido.")
        return cep
    
    def __verificar_cidade_endereco(self, cidade):
        if cidade == "":
            raise ValueError("O que está sendo solicitado está vazio.")
        if not isinstance(cidade, str):
            raise TypeError("valor inválido.")
        return cidade
    

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCEP: {self.cep}"
                f"\nCidade: {self.cidade}"
                f"\nUnidade Federativa: {self.uf.nome} / {self.uf.sigla}")   
        