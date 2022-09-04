from random import randint
numero = str(randint(100000000, 999999999))
novo_cpf = numero                          # Elimina os dois últimos digitos do CPF
reverso = 10                               # Contador reverso
total = 0

# Loop do CPF
for c in range(19):
    if c > 8:                              # Primeiro índice vai de 0 multi 9
        c -= 9                             # São os 9 primeiros digitos do CPF

    total += int(novo_cpf[c]) * reverso    # Valor total da multiplicação

    reverso -= 1                           # Descrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                          # Se o digito for > que 9 o valor é 0
            d = 0
        total = 0                          # Zera o total
        novo_cpf += str(d)                 # Concatena o digito gerado no novo CPF


print(novo_cpf)