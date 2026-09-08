from abc import ABC, abstracclasstmethod, abstractproperty

menu = '''

[c] Cadastrar
[r] Criar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Saldo Insuficiente!')
            return False
        elif valor > 0:
            self._saldo -= valor
            print('Saque Concluido!')
            return True
        else:
            print('Valor Inválido! Tente Novamente')
            return False

    def depositar(self, valor):
        if valor > 0:
            print('Depósito Realizado com Sucesso!')
            return True
        else:
            print('Valor Inválido!')
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('Limite Excedido!')
            return False
        elif excedeu_saques:
            print('Limite Diário Excedido!')
            return False
        else:
            return super().sacar(valor)

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({'tipo': transacao.__class__.__name__, 'valor': transacao.valor})

class Trasacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstracclasstmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)

        if sucesso:
            conta.historico.adicionar_transacao(self)


'''
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
'''