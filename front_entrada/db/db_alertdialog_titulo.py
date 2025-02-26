
from SQLite_db.base import BaseSqlite


class DbAlertDialogTitulo(BaseSqlite):

    def insert_texto(self, e_text):

        self.ativar_banco()

        query = """INSERT INTO titulo_entrada(titulo) VALUES(?)"""
        self.cursorsq.execute(query, (e_text,))

        self.commit_banco()
        self.sair_banco()

    def select_titulo(self):

        self.ativar_banco()

        query = """SELECT titulo FROM titulo_entrada WHERE ID_titulo = 
        (SELECT MAX(ID_titulo) FROM titulo_entrada)"""

        self.cursorsq.execute(query)
        resultado = self.cursorsq.fetchall()

        self.sair_banco()

        return resultado
