from dados import produtos, pessoas, lista
from functools import reduce

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos / len(produtos))

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade)
print(soma_idade / len(pessoas))