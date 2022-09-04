from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))
nova_nova_lista = [x for x in lista if x > 5]
print(nova_nova_lista)


def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
    return True


nova_lista_nova = filter(filtra, produtos)
for produto in nova_lista_nova:
    print(produto)


def filtra_idade(pessoas):
    if pessoas['idade'] >= 18:
        return True
    else:
        return False


nova_lista_pessoas = filter(filtra_idade, pessoas)
for pesso in nova_lista_pessoas:
    print(pesso)