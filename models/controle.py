from models.cliente import Cliente
from datetime import date, datetime
from utils.helper import data_para_str


def pagamento(cliente: Cliente, pagamento: bool) -> None:
    cliente.pagamento = pagamento
    cliente.dia_pagamento = date.today()


def confere_vencimento(cliente: Cliente):
    d1: date = datetime.strptime(data_para_str(cliente.dia_pagamento), '%d/%m/%Y')
    d2: date = datetime.strptime(data_para_str(date.today()), '%d/%m/%Y')
    if abs((d1 - d2).days) > 30:
        cliente.pagamento = False
