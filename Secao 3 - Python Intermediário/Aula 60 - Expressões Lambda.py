# def func(arg, arg2):
#     return arg * arg2
# var = func(2, 3)
# print(var)
# multi = lambda x, y: x * y
# print(multi(2, 3))
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[1], reverse=True))
lista.sort(key=lambda item: item[1])
print(lista)


