l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [v for v in l1]
l3 = [v * 2 for v in l1]
l4 = [(v, v2) for v in l1 for v2 in range(3)]
l5 = ['Luiz', 'Mauro', 'Maria']
l6 = [v.replace('a', '@').upper() for v in l5]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
    ('chave22', 'valor22')
)
l7 = [(y, x) for x, y in tupla]
l7 = dict(l7)
l8 = list(range(100))
l9 = [v for v in l8 if v % 3 == 0 if v % 8 == 0]
l10 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l8]
print(l10)