from SQLite_db.base import BaseSqlite
from flet import AutoCompleteSuggestion


class DbAddadicionartitulo(BaseSqlite):

    def dbent_select_filtrar_dados(self, texto):

        self.ativar_banco()

        query = """SELECT nome_produto FROM PRODUTO WHERE nome_produto LIKE ?"""

        # remova a virgula do final, e remova o segundo parametro.
        self.cursorsq.execute(query, ('%' + texto + '%',))
        resultados = self.cursorsq.fetchall()

        self.sair_banco()

        # Utilize o valor retornado para ambas as propriedades.
        return [AutoCompleteSuggestion(key=row[0], value=row[0]) for row in resultados]
