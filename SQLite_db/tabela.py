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
            valor_unitario REAL,

            FOREIGN KEY (id_produto) REFERENCES PRODUTO(ID_produto)

            )"""

        self.withdb.execute(query)

    def produto(self):

        self.ativar_with()
        """
            produto
        """
        query = """CREATE TABLE if not exists PRODUTO(

            ID_produto INTEGER PRIMARY KEY AUTOINCREMENT,

            nome_produto  TEXT

            )"""

        self.withdb.execute(query)

    def criar_tabelas(self):

        # primarias
        self.produto()

        # secundarias- dependentes
        self.entrada()
        self.subentrada()
