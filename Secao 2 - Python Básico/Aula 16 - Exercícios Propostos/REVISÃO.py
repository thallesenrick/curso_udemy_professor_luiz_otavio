"""
1. Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número: ')

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')

else:
    print('Digite um número inteiro')

"""
2. Faça um programa que pergunte multi hora ao usuário e, baseando-se no horário 
descrito, exiba multi saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""

relogio = input('Que horas são agora? ')

if relogio.isdigit():
    relogio = int(relogio)

    if relogio < 0 or relogio > 23:
        print('Digite um horário valido')
    elif relogio <= 11:
        print('Bom dia meu povo')
    elif relogio <= 17:
        print('Boa tarde cambada')
    else:
        print('Boa noite gurizada')
else:
    print('Digite um valor válido')

"""
3. Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

usuario = input('Digite seu nome: ')
tamanho = len(usuario)

if tamanho <= 4:
    print('Nome pequeno ein meu fi')
elif tamanho <= 6:
    print('Nome mais ou menos vai')
else:
    print('Caraio palavrao ein')