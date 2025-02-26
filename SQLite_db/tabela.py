from SQLite_db.base import BaseSqlite


class SqliteTabela(BaseSqlite):

    def __init__(self) -> None:

        # banco de dados
        self.ativar_with()

        """   
            ENTRADA      
        """

        query = """CREATE TABLE if not exists titulo_entrada(

            ID_titulo INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT 

            )"""

        self.withdb.execute(query)

        """
            subentrada
        """
        query = """CREATE TABLE if not exists subentrada(

            ID_subentrada INTEGER PRIMARY KEY AUTOINCREMENT,

            id_entrada INT,
            id_produto INT,
            quantidade INT,
            valor_unitario REAL,

            )"""

        self.withdb.execute(query)
