# https://docs.python.org/3/library/fuctions.html#open

# Criar e escrever
# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')

# Pra começar a ler do início do arquivo
# file.seek(0, 0)
# print('Lendo linhas: ')
# print(file.read())
# print('##############')

# Para ler linha por linha do arquivo
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print('##############')

# file.seek(0, 0)
# for linha in file:
#     print(linha, end='')
# file.close()

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()

# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())
#
# # Só leitura
# with open('abc.txt', 'r') as file2:
#     print(file2.read())

# with open('abc.txt', 'w+') as file:
#     file.write('Outra linha\n')
#     file.seek(0)
#     print(file.read())

# import os
# os.remove('abc.txt')
import json
d1 = {
    'Pessoa 1': {'nome': 'Thalles', 'idade': 25},
    'Pessoa 2': {'nome': 'Enrick', 'idade': 22},
    'Pessoa 3': {'nome': 'André', 'idade': 18},
    'Pessoa 4': {'nome': 'Maciel', 'idade': 45}
}
d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
