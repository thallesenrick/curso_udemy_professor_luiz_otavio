from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Thalles', 21)
cliente2 = Cliente('Enrick', 34)
cliente3 = Cliente('André', 50)

conta1 = ContaPoupanca(41459, 254136, 0)
conta2 = ContaCorrente(41458, 214328, 0)
conta3 = ContaPoupanca(41455, 237038, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)
if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('ERROR: Cliente não autenticado')

print('----------------------------------')

banco.inserir_clientes(cliente2)
banco.inserir_conta(conta2)
if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('ERROR: Cliente não autenticado')