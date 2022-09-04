"""
* Criar variáveis para nome (str), idade (str)
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

# VARIÁVEIS
nome = 'Juscelino Kub'  # str
idade = '56'  # str
altura = 1.87  # float
peso = 75.60  # float
ano_atual = 2021  # int
imc = peso / altura ** 2  # relação

# RESOLUÇÃO THALLES
print(f'{nome} tem {idade} anos de idade, {altura} de altura e {peso} kg. '
      f'\nNasceu no ano de {ano_atual - int(idade)} e tem o IMC de {imc:.2f}')

print(f'{nome} tem {idade} anos, {altura}de altura e pesa {peso}kg.')
print(f'O IMC de Juscelino é {imc:.2f}.')
print(f'Juscelino nasceu em {ano_atual- int(idade)}.')

# VARIÁVEIS 2 (CURSO)
nome2 = 'Luiz'
idade2 = 32
altura2 = 1.80
peso2 = 80.5
ano_atual2 = 2019
nascimento = ano_atual2 - idade2
imc2 = peso2 / altura2 ** 2

print(f'{nome2} tem {idade2} de idade, {altura2} de altura e {peso2}kg.')
print(f'{nome2} nasceu no ano de {nascimento}')
print(f'{nome2} tem o imc de {imc2:.2f}')
