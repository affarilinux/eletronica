from SQLite_db.base import BaseSqlite


class DbPagina(BaseSqlite):

    def select_pagina(self):

        self.ativar_banco()

        query = """SELECT ID_titulo,Titulo FROM titulo_entrada """

        self.cursorsq.execute(query)
        resultado = self.cursorsq.fetchall()

        self.sair_banco()

        return resultado

   
