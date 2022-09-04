"""
Formatando valores com modificadores - Secao 2 - Python Básico 17

:s - texto (strings)
:d - inteiros (int)
:f - Números de ponto flutuante (float)
:.(número)f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))  # A chave representa o que esta dentro do parêntese!!
print(f'{divisao:.2f}')

nome = 'LUIZ OTAVIO'
print(f'{nome:s}')

num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1150
print(f'{num_4:0>10.2f}')

nome_2 = 'Thalles'
sobrenome = 'Enrick'
sobrenome_2 = 'André'
sobrenome_3 = 'Maciel'
print((50-len(nome_2)) / 2)
print(f'{nome_2:#^50}')

nome_formatado = '{0:@<12} {1:#>12}'.format(nome_2, sobrenome, sobrenome_2, sobrenome_3)
print(nome_formatado)

nome_5 = 'Thalles o Enrickk'
# nome_5 = nome_5.ljust(20, '#')
print(nome_5)
print(nome_5.lower())  # tudo minúsculo
print(nome_5.upper())  # tudo maiúsculo
print(nome_5.title())  # Primeiras letras maiúsculas
