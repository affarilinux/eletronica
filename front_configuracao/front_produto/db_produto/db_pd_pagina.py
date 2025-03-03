from SQLite_db.base import BaseSqlite


class DbPdPagina(BaseSqlite):

    def select_pagina(self):

        self.ativar_banco()

        query = """SELECT ID_produto,nome_produto FROM PRODUTO """

        self.cursorsq.execute(query)
        resultado = self.cursorsq.fetchall()

        self.sair_banco()

        return resultado
