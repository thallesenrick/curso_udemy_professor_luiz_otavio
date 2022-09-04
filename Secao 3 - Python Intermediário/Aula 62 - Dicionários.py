# d1 = dict(chave1='Valor 1', chave2='Valor 2')
# d1['nova_chave'] = 'Valor da nova chave'
# print(d1['chave1'])
# d1 = {'str': 'valor',
#       123: 'Outro valor',
#       (1, 2, 3, 4): 'Tupla',
#       'naoexiste': 'Agora existe'}
# for v, k in d1.items():
#     print(k, v)
# clientes = {
#     'cliente1': {
#         'nome': 'Thalles',
#         'sobrenome': 'Enrick'},
#     'cliente2': {
#         'nome': 'André',
#         'sobrenome': 'Maciel'},
#     'cliente3': {
#         'nome': 'Matheus',
#         'sobrenome': 'Uchoa'},
# }
# for k, v in clientes.items():
#     print(f'Exibindo {k}:')
#     for dadosk, dadosv in v.items():
#         print(f'\t{dadosk} = {dadosv}')
import copy
d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['Enrick', 'Andre']}
v = copy.deepcopy(d1)

v[1] = 'Thalles'
v[4][0] = 'Maciel'
d1.pop(1)
v.pop(3)
v.popitem()
print(d1)
print(v)
d1.update(v)
print(d1)