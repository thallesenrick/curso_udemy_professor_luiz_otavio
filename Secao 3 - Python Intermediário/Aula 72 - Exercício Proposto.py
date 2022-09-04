carrinho = []
carrinho.append(('Produto 1', 30.35))
carrinho.append(('Produto 2', 20.99))
carrinho.append(('Produto 3', 50.50))
print(carrinho)

total = sum([v[1] for v in carrinho])
print(total)
total = sum([float(y) for x, y in carrinho])
print(total)
