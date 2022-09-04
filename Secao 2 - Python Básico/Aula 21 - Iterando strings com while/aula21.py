#        Índices
#        0123456789.......................33
frase = 'o rato roeu multi roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_of_user = input('Qual letra deseja colocar maiúscula: ')

# Iteração = ato de percorrer cada um dos elementos da string ou elemento iterável
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_of_user:
        nova_string += input_of_user.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
