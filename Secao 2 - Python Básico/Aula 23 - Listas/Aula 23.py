"""
-> Listas em Python

    Índice(+) 0    1    2    3    4
    Índice(-) 5    4    3    2    1
    lista = ['A', 'B', 'C', 'D', 'E']

    - Produzindo listas mais rapidamente
        -l2 = list(range(0, 100, 8))
    - Nas listas os valores são mutáveis
        - EX: lista = ['A', 'B', 'C', 'D', 'E'] / lista[4] = 'F'
    - fatiamento
        - EX: lista [1::2] - do 1 ao fim pulando de 2 em 2
        - *** lista [:2:-1] - do -1 ate o -2
    - append
        - Insere um valor no final da lista
        - EX: l2 = [4, 5, 6] / l2.append('b') = l2 = [4, 5, 6, 'b']
    - insert
        - Insere em qualquer posição da lista (x = Posição, y = Termo para adicionar)
        - l2 = [4, 5, 6] / l2.insert(1, 'abacate') = l2 = [4, 'abacate', 5, 6]
    - pop
        - Deleta o ultimo elemento da lista
        - l2 = [4, 5, 6] / l2.pop = l2 = [4, 5]
    - del
        - Deleta toda multi lista ou elementos del(l2[1:3]) - Vai excluir elementos 1 e 2
    - clear
        - Limpa multi lista, tornando-multi vazia
    - extend
        - Para unir listas
        - EX: l1 = [1, 2, 3], l2 = [4, 5, 6] / l1.extend(l2) = l1 = [1, 2, 3, 4, 5, 6]
        - *** l1 = [1, 2, 3] / l1.extend('multi') = l1 = [1, 2, 3, 'multi']
    - min
        - Para encontrar o valor mínimo da lista
    - max
        - Para encontrar o valor máximo da lista
    - range
"""

secreto = 'otorrinolaringologista'
digitadas = []
chances = 5

while True:
    if chances == 0:
        print('Você perdeu!!!')
        break
    letra = input('Digite um letra: ')
    if len(letra) > 1:
        print('Ahhh isso nao vale! Digite apenas uma letra!')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'Uhuu! A letra {letra} existe na palavra secreta!')
    else:
        print(f'Affz! A letra {letra} não existe na palavra secreta!')
        chances -= 1
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Que legal! Você ganhou!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    print(f'Você tem {chances} chances.')