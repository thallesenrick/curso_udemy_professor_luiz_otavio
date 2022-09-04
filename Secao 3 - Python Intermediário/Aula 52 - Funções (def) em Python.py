def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(3, 1)
if divide:
    print(divide)
else:
    print('Conta inválida')


def dumb():
    return 'Luiz', 'Otavio'


print(dumb(), type(dumb()))
var = dumb()
print(var, type(var))

# args, kwargs


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3, 4, 5)
# lista = [1, 2, 3, 4, 5]
# ni, n2, *t = lista
# print(ni, n2, n)
# lista = [1, 2, 3, 4, 5]
# print(*lista, sep='_')


def fun(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade nao existe')


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
fun(*lista, *lista2, nome='Thalles', sobrenome='Enrick', idade=40)
variavel = 'valor'


# def func():
#     print(variavel)
#
#
# def func2(arg=None):
#     arg = arg.replace('v', 'c')
#     return arg
#
#
# func()
# outra_variavel = func2(arg=variavel)
# print(outra_variavel)


def funca():
    outra_variavel = 'valor'
    return outra_variavel


def funca2(arg):
    print(arg)


var = funca()
funca2(var)