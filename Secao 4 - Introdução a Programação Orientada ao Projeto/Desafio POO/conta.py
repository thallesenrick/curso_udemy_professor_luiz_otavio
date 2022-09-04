from abc import abstractmethod


class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        if not isinstance(valor, (float, int)):
            raise ValueError('ERROR: O valor de depósito precisa ser numérico!')

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia} '
              f'Conta: {self.conta} '
              f'Saldo: R${self.saldo:.2f}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('ERROR: Saldo em conta insuficiente!')
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=200):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('ERROR: Saldo em conta insuficiente!')
            return

        self.saldo -= valor
        self.detalhes()
