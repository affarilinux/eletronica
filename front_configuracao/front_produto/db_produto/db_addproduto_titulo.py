from SQLite_db.base import BaseSqlite


class DbAddProdutoTitulo(BaseSqlite):

    def pd_insert_texto(self, e_text):

        self.ativar_banco()

        query = """INSERT INTO PRODUTO(nome_produto) VALUES(?)"""
        self.cursorsq.execute(query, (e_text,))

        self.commit_banco()
        self.sair_banco()

    def pd_select_titulo(self):

        self.ativar_banco()

        query = """SELECT nome_produto FROM PRODUTO WHERE ID_produto = 
        (SELECT MAX(ID_produto) FROM PRODUTO)"""

        self.cursorsq.execute(query)
        resultado = self.cursorsq.fetchall()

        self.sair_banco()

        return resultado

    def pd_select_possui_titulo(self, nome):

        self.ativar_banco()

        query = """SELECT ID_produto FROM PRODUTO WHERE nome_produto = ?"""

        self.cursorsq.execute(query, (nome,))
        resultado = self.cursorsq.fetchall()

        self.sair_banco()

        return resultado
