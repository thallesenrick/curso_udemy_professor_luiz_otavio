"""
Split, Join, Enumerate em Python
* Split - dividir uma string
* Join - Juntar uma lista
* Enumerate - Enumerar elementos da lista # iteráveis
"""

string_1 = 'O Brasil é penta.'
lista = string_1.split()

for indice, valor in enumerate(lista):
    print(indice, valor)

numeros = ['Luiz', 'João', 'Maria']
for indice, valor in enumerate(numeros):
    print(indice, valor)