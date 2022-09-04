while True:
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    for c in range(19):
        if c > 8:
            c -= 9
        total += int(novo_cpf[c]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
                novo_cpf += str(d)
    if cpf == novo_cpf:
        print('CPF Válido!')
    else:
        print('CPF Inválido!')