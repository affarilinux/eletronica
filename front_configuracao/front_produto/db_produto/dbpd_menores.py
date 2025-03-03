from SQLite_db.base import BaseSqlite


class DbPdMenores(BaseSqlite):

    def mnpd_apagar_linha(self, id_valor):

        self.ativar_banco()

        query = """DELETE FROM PRODUTO WHERE ID_produto = ?"""
        self.cursorsq.execute(
            query, (id_valor,))  # Usa tupla para evitar SQL Injection

        self.commit_banco()
        self.sair_banco()
