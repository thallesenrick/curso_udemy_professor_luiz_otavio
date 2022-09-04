"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -30 -15000
float - real/ponto flutuante - -20.8 -45.9
bool - booleano/lógico - True/False 10 = 10
"""

print(type('Luiz'))
print(type(16500))
print(type(-10.8))
print(type(False))

print('Luiz', type('Luiz'))
print(10, type(10))
print(-10.4, type(-10.4))
print(10 == 10, type(10 == 10))
print('L' == 'L', type('L' == 'L'))
print('l' == 'L', type('l' == 'L'))
print(bool())

print('Luiz', type('Luiz'), bool('Luiz'))
print('10', type('10'), type(int('10')))
# print('luiz', int('luis')) dá erro

print('Thalles', type('Thalles'))
print(21, type(21))
print(1.76, type(1.76))
print(21 > 18, type(21 > 18))

