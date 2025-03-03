from SQLite_db.base import BaseSqlite


class SqliteTabela(BaseSqlite):

    def entrada(self):

        self.ativar_with()

        """   
            ENTRADA      
        """

        query = """CREATE TABLE if not exists titulo_entrada(

            ID_titulo INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT 

            )"""

        self.withdb.execute(query)

    def subentrada(self):

        self.ativar_with()
        """
            subentrada
        """
        query = """CREATE TABLE if not exists subentrada(

            ID_subentrada INTEGER PRIMARY KEY AUTOINCREMENT,

            id_entrada INT,
            id_produto INT,
            quantidade INT,
            valor_unitario REAL

            )"""

        self.withdb.execute(query)

    def criar_tabelas(self):

        self.entrada()
        self.subentrada()
