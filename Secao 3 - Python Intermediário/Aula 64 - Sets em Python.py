# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add(3)
# s1.add((1, 2, 3, 'Luiz'))
# s1.discard(2)
# s1.update('Python')
# print(s1)
# l1 = [1, 2, 3, 1, 4, 5, 8, 3, 7, 9, 1, 0, 'Thalles', 'Enrick', 1, 2, 6, 5, 'Thalles']
# l1 = set(l1)
# l1 = list(l1)
# print(l1)

# Interseção de sets
s1 = {1, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2  # Une excluindo os repetidos
s4 = s1 & s2  # Mostra os itens que se repetem
s5 = s1 - s2  # Mostra os itens que tem na esquerda que não tem na direita
s6 = s1 ^ s2  # Mostra os itens que tem nos sets que sao unicos
print(s3)
print(s4)
print(s5)
print(s6)
