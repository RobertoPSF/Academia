from time import sleep
from utils.helper import formata_float_para_moeda
from models.controle import pagamento, confere_vencimento
from models.cliente import Cliente
from typing import List


contas: List[Cliente] = []


def main() -> None:
    menu()


def menu() -> None:

    for cliente in contas:
        confere_vencimento(cliente)

    print(f'1 - Cadastrar cliente\n'\
            '2 - Efetuar pagamento\n'\
            '3 - Cancelar cadastro\n'\
            '4 - Mostrar clientes\n'\
            '5 - Sair\n')
        
    op: int = int(input('Operação: '))

    if op == 1:
        criar_conta()
    elif op == 2:
        pagar()
    elif op == 3:
        excluir()
    elif op == 4:
        for cliente in contas:
            print(cliente)
        enter: str = input('Clique enter para retornar ao menu')
        menu()
    elif op == 5:
        print('Até a próxima!')
        sleep(2)
        exit(0)
    else:
        print('Insira uma opção válida.')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente')
    nome: str = input('Nome: ')
    cpf: str = input('CPF: ')
    telefone: str = input('Telefone: ')
    endereco: str = input('Endereço: ')
    data_nascimento: str = input('Data de nascimento: ')
    planos()
    plano: str = input('Informe a opção do plano:')
    cliente: Cliente = Cliente(nome, cpf, telefone, endereco, data_nascimento, plano)
    pagamento(cliente, True)

    contas.append(cliente)

    print('Conta criada com sucesso!')
    sleep(2)
    menu()


def pagar() -> None:
    nome: str = input('Nome: ')
    for cliente in contas:
        if cliente.nome == nome:
            pagamento(cliente, True)


def excluir() -> None:
    try:
        nome: str = input('Nome: ')
        cont: int = 0
        for cliente in contas:
            if cliente.nome == nome:
                print(cliente)
                print('Tem certeza que deseja excluir essa conta ?\n'\
                    '1 - Sim    2 - Não')
                op: int = int(input('Opção: '))
                if op == 1:
                    contas.pop(cont)
                    print('Conta excluída.')
                    sleep(2)
                    menu()
                else:
                    sleep(1)
                    menu()
            cont += 1
    except:
        print('Não existe esse nome na lista.')
        sleep(2)
        menu()    


def planos() -> None:
    print(f'1 - Plano Básico: {formata_float_para_moeda(59.99)}\n'\
        f'2 - Plano Intermediário: {formata_float_para_moeda(79.99)}\n'\
        f'3 - Plano Master: {formata_float_para_moeda(99.99)}\n'\
        f'4 - Plano Fisioculturista: {formata_float_para_moeda(129.99)}\n')


if __name__ == '__main__':
    main()
