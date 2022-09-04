from Vendas.calc_precos import aumento, reducao
from Vendas.formato import preco

preco = 49.90
preco_com_aumento = aumento(preco, 15, format=True)
preco_com_reducao = reducao(preco, 15)
print(preco_com_aumento)
print(preco_com_reducao)