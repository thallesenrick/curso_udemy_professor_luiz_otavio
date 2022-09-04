from classes.contapoupanca import ContaPoupanca
from classes.contacorrente import ContaCorrente

cp = ContaPoupanca(41459, 141089, 360)
cp.depositar(100)
cp.sacar(234)
cp.sacar(226)
cp.sacar(1)
print('#############################')
cc = ContaCorrente(agencia=41451, conta=141729, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)
