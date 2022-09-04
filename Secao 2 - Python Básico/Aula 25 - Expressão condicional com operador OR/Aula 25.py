nome = input('Qual o seu nome? ')
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')

# Pode ser substituido por:
print(nome or 'Você não digitou nada!')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Thalles'

variaval = a or b or c or d or e or f or g
print(variaval)
# Printou multi primeira verdadeira que tinha valor => f = 22
