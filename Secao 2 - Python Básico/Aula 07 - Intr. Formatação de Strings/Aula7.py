
nome = 'Thalles Enrick'  # str
idade = 21  # int
altura = 1.76  # float
e_maior = idade > 18  # int
peso = 67  # int
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))
