"""
JSON - JavaScript Object Notation
- É um formato de troca de dados entre sistemas e programas;
- Leve e de facil utilização;
Utilizados por APIs;
"""
from dados import *
import json

# dicionario = json.loads(clientes_json)
# for k, v in dicionario.items():
#     print(k)
#     print(v)

# with open('clientess.json', 'w') as arquivo:
#     json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientess.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(type(dados))