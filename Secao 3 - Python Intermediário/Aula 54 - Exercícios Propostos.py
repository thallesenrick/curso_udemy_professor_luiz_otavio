def saudacao(saud, nome):
    return f'{saud} {nome}!'


s = saudacao('Oi', 'Thalles')
print(s)


def soma(a=0, b=0, c=0):
    return a + b + c


somador = soma(1, 2, 3)
print(somador)


def aumento(a=0, b=0):
    return a + (b/100 * a)


aum = aumento(1000, 10)
print(aum)


def fizzbuzz(a):
    if a % 5 == 0 and a % 3 == 0:
        return f'Fizzbuzz, {a} é divisível por 3 e 5'
    if a % 3 == 0:
        return f'Fizz, {a} é divisível por 3'
    if a % 5 == 0:
        return f'Buzz, {a} é divisível por 5'
    return a


from random import randint

for c in range(0, 100):
    aleatorio = randint(0, 100)
    print(fizzbuzz(aleatorio))