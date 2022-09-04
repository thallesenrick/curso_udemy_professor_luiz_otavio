# Exercício 01
while True:
    while True:
        num = input('Digite um número: ').strip()
        if not num.isnumeric():
            print('Por favor, digite um número válido!')
        else:
            num = int(num)
            break
    if num % 2 == 0:
        print(f'{num} um número PAR!')
    else:
        print(f'{num} um número IMPAR!')
    resposta = str(input('Deseja continuar calculando? [S/N] ')).upper()
    if resposta == 'N':
        print('Até mais! Finalizando...')
        break

# Exercício 02
while True:
    while True:
        hora = int(input('Digite um horário: '))
        if 0 <= hora <= 23:
            if hora <= 11:
                print('Bom dia!')
            elif hora <= 17:
                print('Boa tarde!')
            elif hora <= 23:
                print('Boa noite!')
        else:
            print('Digite um horário válido!')
    resposta = str(input('Deseja continuar calculando? [S/N] ')).upper()
    if resposta == 'N':
        print('Até mais! Finalizando...')
        break

# Exercício 03
while True:
    nome = str(input('Digite um nome de usuário: '))
    if len(nome) <= 4:
        print(f'O nome {nome} é curto!')
    elif len(nome) <= 6:
        print(f'O nome {nome} é normal!')
    else:
        print(f'O nome {nome} é muito grande!')