menu = '''

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

while True:
    opcao = input(menu)
    print('')

    match opcao.lower():
        case 'd':
            print(f'Saldo Atual: R$ {saldo:.2f}')
            depositar = float(input('Quanto Deseja Depositar: R$ '))
            if depositar >= 1:
                saldo += depositar
                print(f'Valor de R$ {depositar:.2f} Depositado!')
                extrato.append(f'Depósito: R$ {depositar:.2f}')
            else:
                print('Insira um valor válido')
        case 's':
            print(f'Saldo Atual: R$ {saldo:.2f}')
            sacar = float(input('Quanto Deseja Sacar: R$ '))
            if quantidade_saque < LIMITE_SAQUES:
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
        case 'e':
            print('Extrato:')
            for _ in extrato:
                print(f'{_}')
            print(f'Saldo Atual: R$ {saldo:.2f}')
        case 'q':
            print('Programa Encerrado!')
            break