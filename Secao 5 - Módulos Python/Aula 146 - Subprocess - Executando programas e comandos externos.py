import subprocess

# Windows - ping 127.0.0.1

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

# Algum erro que possa acontecer, na maioria das vezes será None
# print(proc.stderr)

# Saida do comando
saida = proc.stdout
print(saida)

# Será 0 se o comando for executado com sucesso
# print(proc.returncode)

# Os argumentos enviados em proc
# print(proc.args)