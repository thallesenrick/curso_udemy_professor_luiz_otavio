import random
import string

# Gera um número inteiro entre A e B
inteiro = random.randint(10, 20)
print(inteiro)

# Gera um número aleatório usando a função range()
inteiro2 = random.randrange(900, 1000, 10)
print(inteiro2)

# Gera um número de ponto flutuante entre A e B
flutuante = random.uniform(10, 20)
print(flutuante)

# Gera um número de ponto flutuante entre 0 e 1
flutuante2 = random.random()
print(flutuante2)

# Seleciona aleatóriamente valores de uma lista
lista = ['Thalles', 'Enrick', 'André', 'Maciel', 'Jennie', 'Lisa', 'Rosé', 'Jisoo']
sorteio = random.sample(lista, 2)
sorteio2 = random.choices(lista, k=2)
sorteio3 = random.choice(lista)
print(sorteio)

# Embaralha uma lista
random.shuffle(lista)
print(lista)

# Gerador de senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#{}$%&.()_-/*[]'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))
print(senha)
