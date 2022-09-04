from time import sleep
# num1 = input('Digite um número: ')
# num2 = input('Digite outro número: ')
#
# if num1.isnumeric() and num2.isnumeric():
#     num1 = int(num1)
#     num2 = int(num2)
#     print(num1 + num2)
# else:
#     print('Caracteres inválidos')


while True:
    while True:
        numero1 = input('\033[33mDigite o primeiro número: ')
        if not numero1.isnumeric():
            print('\033[31mCaracter inválido! Digite novamente!')
        else:
            numero1 = int(numero1)
            break
    while True:
        numero2 = input('\033[33mDigite o segundo número: ')
        if not numero2.isnumeric():
            print('\033[31mCaracter inválido! Digite novamente!')
        else:
            numero2 = int(numero2)
            break
    soma = numero1 + numero2
    print('Calculando...')
    sleep(1.5)
    print(f'\033[32mA soma entre {numero1} e {numero2} é igual a {soma}!')
    sleep(1)
    resposta = str(input('\033[33mDeseja continuar calculando? [S/N] ')).upper()
    if resposta == 'N':
        print('Até mais! Finalizando...')
        sleep(1)
        break