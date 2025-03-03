from SQLite_db.base import BaseSqlite


class DbAddPdEditarTitulo(BaseSqlite):

    def update_uptitulo(self, id_titulo, titulo):

        self.ativar_banco()

        query = """UPDATE PRODUTO SET nome_produto = ? WHERE ID_produto = ?"""
        self.cursorsq.execute(query, (titulo, id_titulo))

        self.commit_banco()
        self.sair_banco()

    def select_titulo(self, id_titulo):

        self.ativar_banco()

        query = """SELECT nome_produto FROM PRODUTO WHERE 
        ID_produto = ?"""

        self.cursorsq.execute(query, (id_titulo,))
        resultado = self.cursorsq.fetchall()

        self.sair_banco()

        return resultado
