import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# Função para criar colunas da tabela. Se ja existir pula essa função.
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# Maneiras para inserir registros na tabela sem (SQL INJECTION ou repetição de valores)
# Enviando como tupla.
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))

# Enviando como chave de dicionários.
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'Joãozinho', 'peso': 25}
# )

# Outro método como chave de dicionários.
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id': None, 'nome': 'Daniel', 'peso': 113}
# )

# Comando para executar linha anterior.
# conexao.commit()

# Atualizar dados
# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Joana', 'id': 2}
# )
# conexao.commit()

# Excluir dados
# cursor.execute(
#     'DELETE FROM CLIENTES WHERE id=:id',
#     {'nome': 'Joana', 'id': 2}
# )
# conexao.commit()

# Função para mostrar os valores da tabela, é possivel iterar com o fetchall.
cursor.execute('SELECT nome, peso FROM clientes WHERE peso > :peso',
               {'peso': 70})

# Desempacotando as colunas
for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)


cursor.close()
conexao.close()