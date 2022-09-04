import pymysql.cursors
from contextlib import contextmanager

# CRUD - CREATE, READ, UPDATE and DELETE
# Primeiro a se fazer se conectar com o servidor, pode-se forçar um fechamento
# automático da conexão com um contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


# Adicionando uma informação
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()

# Adicionando varias informações
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#               '(%s, %s, %s, %s)'
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 22, 67),
#             ('JOSE', 'FIGUEIREDO', 32, 78),
#         ]
#         cursor.executemany(sql, dados)
#         conexao.commit()

# Excluindo uma informação
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id=%s'
#         cursor.execute(sql, (5,))
#         conexao.commit()

# Excluindo varias informações
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (18, 19, 20))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (20, 23))
#         conexao.commit()

# Atualizar informações
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('JOANA', 4))
        conexao.commit()

# Seleciona os dados da base de dados
# Esse gerenciador está fechando a conexão
with conecta() as conexao:
    # Esse gerenciador está fechando o cursor
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
