from SQLite_db.base import BaseSqlite


class DbAlertDialogEditarTitulo(BaseSqlite):

    def update_uptitulo(self, id_titulo, titulo):

        self.ativar_banco()

        query = """UPDATE titulo_entrada SET titulo = ? WHERE ID_titulo = ?"""
        self.cursorsq.execute(query, (titulo, id_titulo))

        self.commit_banco()
        self.sair_banco()

    def select_titulo(self, id_titulo):

        self.ativar_banco()

        query = """SELECT titulo FROM titulo_entrada WHERE 
        ID_titulo = ?"""

        self.cursorsq.execute(query, (id_titulo,))
        resultado = self.cursorsq.fetchall()

        self.sair_banco()

        return resultado
