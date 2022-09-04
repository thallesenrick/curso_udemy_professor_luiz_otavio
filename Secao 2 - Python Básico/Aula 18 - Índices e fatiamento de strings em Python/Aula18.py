"""
Manipulando Strings -  Secao 2 - Python Básico 18
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
"""

# positivos (0,1,2,3,4,5,6,7,8)
texto = 'Python_s2'
print(texto[5])  # Colchete mostra o caractere no exemplo acima: P = 0, y = 1, t = 2.....

# negativos - (9,8,7,6,5,4,3,2,1)
url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[0::3]
print(nova_string)
