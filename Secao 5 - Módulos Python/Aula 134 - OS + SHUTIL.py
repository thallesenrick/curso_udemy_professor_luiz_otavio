import os
import shutil

caminho_original = r'C:\Users\andre\Documents\modulo 1'
caminho_novo = r'C:\Users\andre\Documents\modulo 2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'ERROR: Pasta {caminho_novo} já existe!')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        # Para Mover
        # if '.jpg' in file:
        #     shutil.move(old_file_path, new_file_path)
        #     print(f'Arquivo {file} movido com sucesso')

        # Para Copiar
        # if '.jpg' in file:
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'Arquivo {file} copiado com sucesso')

        # Para Apagar
        if '.jpg' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} apagado com sucesso')