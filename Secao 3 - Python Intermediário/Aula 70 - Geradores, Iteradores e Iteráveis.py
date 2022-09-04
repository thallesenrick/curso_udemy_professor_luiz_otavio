import sys
import time
# lista = [0, 1, 2, 3, 4, 5]
# lista = iter(lista)
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(hasattr(lista, '__next__'))

# def gera():
#     variavel = 'Valor 1'
#     yield variavel
#     variavel = 'Valor 2'
#     yield variavel
#     variavel = 'Valor 3'
#     yield variavel
#
#
# g = gera()
# for v in g:
#     print(v)
l1 = [x for x in range(100000)]
print(type(l1))
l2 = (x for x in range(100000))
print(type(l2))
print(sys.getsizeof(l2))
print(sys.getsizeof(l1))
for v in l2:
    print(v)