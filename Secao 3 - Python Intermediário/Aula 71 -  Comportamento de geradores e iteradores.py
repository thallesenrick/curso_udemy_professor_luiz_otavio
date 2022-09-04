# Listas, Tuplas, Strings -> São sequências -> São iteráveis
nome = 'Thalles Enrick'
# for letra in nome:
#     print(letra)
iterador = iter(nome)
gerador = (letra for letra in nome)
print(next(gerador))  # T
print(next(gerador))  # h
print(next(gerador))  # a
print(next(gerador))  # l
print('OLHA O FOR')
for letra in gerador:
    print(letra)
print('OLHA O OUTRO FOR')
for letra in gerador:
    print(letra)
