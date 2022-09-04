usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')

# ---------------------------------------------------------------------------------------------------------------------
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
# --------------------------------------------------------------------------------------------------------------------
print(len(string1))
print(string1.__len__())

papa1 = input('Digite algo: ')
papa2 = input('Digite mais algo: ')
somadospapas = len(papa1) + len(papa2)
print(f'{somadospapas} é o tanto de caracteres que tu escreveu. ')













