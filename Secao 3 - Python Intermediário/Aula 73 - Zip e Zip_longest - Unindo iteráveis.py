from itertools import zip_longest, count
"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

indice = count()
cidades = ['São Paulo', 'Fortaleza', 'Salvador', 'Rio de Janeiro', 'Florianópolis']
estados = ['SP', 'CE', 'BA', 'RJ']


cidades_estados = zip(indice, estados, cidades)
for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)