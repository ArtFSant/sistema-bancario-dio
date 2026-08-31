menu = '''

[c] Cadastrar
[r] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = []
quantidade_saque = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

def depositar(saldo, extrato, /):
    print(f'Saldo Atual: R$ {saldo:.2f}')
    depositar = float(input('Quanto Deseja Depositar: R$ '))
    if depositar >= 1:
        saldo += depositar
        print(f'Valor de R$ {depositar:.2f} Depositado!')
        extrato.append(f'Depósito: R$ {depositar:.2f}')
    else:
        print('Insira um valor válido')

def sacar(*, saldo, extrato, quantidade_saque, limite, limite_saques):
    print(f'Saldo Atual: R$ {saldo:.2f}')
    sacar = float(input('Quanto Deseja Sacar: R$ '))
    if quantidade_saque < limite_saques:
        if sacar <= saldo:
            if sacar >= 1:
                saldo -= sacar
                quantidade_saque += 1
                print(f'Valor de R$ {sacar:.2f} Sacado!')
                extrato.append(f'Saque: R$ {sacar:.2f}')
            else:
                print('Insira um valor válido')
        else:
            print('Saldo Insuficiente')
    else:
        print('Limite de saques diários atingido. Tente novamente amanhã')

def extrato(extrato, /, *, saldo):
    print('Extrato:')
    for _ in extrato:
        print(f'{_}')
    print(f'Saldo Atual: R$ {saldo:.2f}')

def cadastrar_usuario(usuarios):
    print('Cadastro:')
    cpf = input('Digite seu CPF: ').strip()
    existente = 0
    for _ in usuarios:
        if _['cpf'] == cpf:
            existente += 1
    if existente > 0:
        print('Usuário já cadastrado!')
    else:
        nome = input('Digite seu nome: ').strip()
        data_nascimento = input('Digite sua data de nascimento: ').strip()
        endereco = input('Digite seu endereço: ').strip()
        print(f'Usuário: {nome}, CPF: {cpf} - Cadastrado!')
        usuarios.append({'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco})

def criar_conta(contas, usuarios, /):
    print('Criar Conta Corrente:')
    cpf = input('Digite seu CPF: ').strip()
    existente = 0
    for _ in usuarios:
        if _['cpf'] == cpf:
            existente += 1
    if existente > 0:
        numero_conta = (len(contas) + 1)
        agencia = '0001'
        contas.append({'cpf': cpf, 'numero_conta': numero_conta, 'agencia': agencia})
        print(f'Conta {numero_conta}, Agência: {agencia} criada para o CPF: {cpf}')
    else:
        print('Usuário não possui conta no sistema!')

while True:
    opcao = input(menu)
    print('')

    match opcao.lower():
        case 'd':
            depositar(saldo, extrato)
        case 's':
            sacar(saldo=saldo, extrato=extrato, limite= limite, limite_saques=LIMITE_SAQUES, quantidade_saque=quantidade_saque)
        case 'e':
            extrato(extrato, saldo=saldo)
        case 'c':
            cadastrar_usuario(usuarios)
        case 'r':
            criar_conta(contas, usuarios)
        case 'q':
            print('Programa Encerrado!')
            break