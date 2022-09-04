"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product
pessoas = ['Luiz', 'André', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']
for grupo in enumerate(combinations(pessoas, 4)):
    print(grupo)
print('=' * 40)
for grupo in enumerate(permutations(pessoas, 3)):
    print(grupo)
print('=' * 40)
for grupo in enumerate(product(pessoas, repeat=2)):
    print(grupo)
