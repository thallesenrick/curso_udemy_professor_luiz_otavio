import os
from uteis import formata_tamanho

caminho_procura = r'C:\Users\andre\Documents\modulo 1'
termo_procura = input('Digite um termo: ')
contador = 0


for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                contador += 1

                print(f'Ficheiro correspondente: {arquivo}')
                print(f'Caminho: {caminho_completo}')
                print(f'Nome: {nome_arquivo}')
                print(f'Extensão: {extensao_arquivo}')
                print(f'Tamanho: {tamanho_arquivo}')
                print(f'Tamanho formatado: {formata_tamanho(tamanho_arquivo)}\n')

            except PermissionError as e:
                print('ERROR: Sem permissão de acesso!')
            except FileNotFoundError as e:
                print('ERROR: Arquivo não encontrado!')
            except Exception as e:
                print(f'ERROR: {e} ')

print(f'{contador} arquivo(s) encontrado(s)')