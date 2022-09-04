# lista = [
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
#     ('chave3', 'valor3'),
# ]
# d1 = {x.upper(): y.upper()*2 for x, y in lista}
# print(d1)
d1 = {f'chave{x}': x**2 for x in range(5)}
print(d1, type(d1))