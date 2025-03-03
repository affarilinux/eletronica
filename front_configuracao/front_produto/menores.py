from front_configuracao.front_produto.db_produto.dbpd_menores import (
    DbPdMenores
)


class ProdutoMenores:

    def menor_apagar_titulo(self, id_titulo):

        DbPdMenores().mnpd_apagar_linha(id_titulo)

        from front_configuracao.front_produto.pagina import (
            PaginaProduto
        )

        PaginaProduto().produto_update_pagina()
