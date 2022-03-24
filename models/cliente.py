from datetime import date
from utils.helper import str_para_data, data_para_str


class Cliente:
    
    cont: int = 1

    def __init__(self: object, nome: str, cpf: str, telefone: str, endereco, data_nascimento: str, plano: int) -> None:
        self.__id: int = Cliente.cont
        self.__pagamento = False
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__telefone: str = telefone
        self.__endereco: str = endereco
        self.__data_nascimento: date = str_para_data(data_nascimento)
        self.__data_cadastro: date = date.today()
        self.__plano: int = plano
        self.__dia_pagamento: date = data_para_str(date.today())
        Cliente.cont += 1

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def telefone(self: object) -> str:
        return self.__telefone

    @property
    def endereco(self: object) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self: object, endereco: str) -> None:
        self.__endereco = endereco

    @property 
    def data_nascimento(self: object) -> str: 
        return data_para_str(self.__data_nascimento)

    @property 
    def data_cadastro(self: object) -> str:
        return data_para_str(self.__data_cadastro)

    @property
    def plano(self: object) -> int:
        return self.__plano

    @plano.setter
    def plano(self: object, plano: int) -> None:
        self.__plano

    @property
    def pagamento(self: object) -> bool:
        return Cliente.pagamento
    
    @pagamento.setter
    def pagamento(self: object, pagamento: bool) -> None:
        self.__pagamento = pagamento

    @property
    def dia_pagamento(self: object):
        return self.__dia_pagamento

    @dia_pagamento.setter
    def dia_pagamento(self: object, dia_pagamento: date) -> None:
        self.__dia_pagamento = dia_pagamento
    

    def formata_pagamento(self: object) -> str:
        if self.__pagamento == True:
            return f'Entrada liberada'
        else:
            return f'Entrada negada'

    
    def __str__(self: object) -> str:
        return f'Código: {self.__id} -- {self.__nome}\nData de nascimento: {data_para_str(self.__data_nascimento)}\n' \
        f'Data de cadastro: {data_para_str(self.__data_cadastro)}\nPlano {self.__plano}\n{Cliente.formata_pagamento(self)}\n'
