import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        consulta = 'SELECT * FROM agenda'
        self.cursor.execute(consulta)

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.conn.close()
        self.cursor.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.inserir('Luiz Otávio', '102321')
    agenda.inserir('Luiz Felipe', '102322')
    agenda.inserir('Ronaldo Luiz', '102323')
    agenda.inserir('R. Luiza', '102324')
    agenda.inserir('R. Luiza meio do caminho', '102325')
    agenda.buscar('luiz')