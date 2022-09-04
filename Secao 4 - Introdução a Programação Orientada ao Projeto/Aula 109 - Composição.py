from classes3 import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()


cliente2 = Cliente('Thalles', 21)
cliente2.insere_endereco('Fortaleza', 'CE')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()


cliente3 = Cliente('Maria', 55)
cliente3.insere_endereco('Salvador', 'BA')
cliente3.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

cliente4 = Cliente('João', 19)
cliente4.insere_endereco('São Paulo', 'SP')
print(cliente4.nome)
cliente4.lista_enderecos()
del cliente4
print()

print('#####################################################################')