from formato import *


def aumento(valor, porcetagem, format=False):
    r = valor + (valor * porcetagem / 100)
    if format:
        return 
    else:
        return r


def reducao(valor, porcetagem, format=False):
    r = valor - (valor * porcetagem / 100)
    if format:
        return preco.real(r)
    else:
        return r
