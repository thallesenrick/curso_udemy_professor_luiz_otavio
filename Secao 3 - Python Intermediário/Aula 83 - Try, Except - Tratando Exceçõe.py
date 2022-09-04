try:
    a = {}
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Erro de Índice ou Chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
else:  # é executada se nao tiver erro no código
    print('Seu código foi executado com sucesso')
    print(a)
finally:  # é executada sempre
    print('Finalmente.')
print('Bora continuar...')

while True:
    try:
        a = int(input('Digite um número: '))
        b = int(input('Digite outro número: '))
        c = a / b
    except ZeroDivisionError as erro:
        print('Erro!', erro)
    except ValueError as erro2:
        print('Erro!', erro2)
    else:
        print(f'A divisão de {a} por {b} é {c:.2f}')
    finally:
        resposta = str(input('Deseja continuar? [S/N] ')).upper()
        if resposta == 'N':
            break

print(d)