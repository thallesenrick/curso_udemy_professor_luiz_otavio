"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Thalles Enrick'  # str
idade = 21  # int
altura = 1.76  # float
e_maior = idade > 18  # int
ano_nascimento = 2000  # int
ano = 2021  # int
peso = 67  # int
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print('Idade atual:', ano - ano_nascimento)
print(idade * altura)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
