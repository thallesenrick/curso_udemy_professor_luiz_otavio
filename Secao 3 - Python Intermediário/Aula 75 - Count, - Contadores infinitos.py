"""
count - Itertools
"""
# from types import GeneratorType
# variavel = ((x, y) for x, y in zip('Alo', 'Pai'))
# print(isinstance(variavel, GeneratorType))
# print(list(variavel))
from itertools import count
contador = count(start=1)
# for valor in contador:
#     print(round(valor, 2))
#     if valor >= 10 or valor <= -10:
#         break
lista = ['Thalles', 'Enrick', 'André', 'Maciel']
lista = zip(contador, lista)
print(list(lista))