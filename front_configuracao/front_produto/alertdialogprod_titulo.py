from flet import (Text, TextField, AlertDialog, MainAxisAlignment,
                  TextButton)

from front_configuracao.front_produto.db_produto.db_addproduto_titulo import (
    DbAddProdutoTitulo
)
from menores import frontMenores  # snackbar


class AddTituloProduto:

    def __init__(self):

        from front_exe import Pagina

        def adicionar_texto(e):

            if text_field.value != "":
                DbAddProdutoTitulo().pd_insert_texto(text_field.value)

                var_sqlite_max = DbAddProdutoTitulo().pd_select_titulo()

                if var_sqlite_max[0][0] == text_field.value:

                    frontMenores().ativar_snackbar("Salvo com sucesso")

                    from front_configuracao.front_produto.pagina import (
                        PaginaProduto
                    )

                    PaginaProduto().produto_update_pagina()

                    Pagina.PAGE.close(dlg_modal)

            elif text_field.value == "":

                frontMenores().ativar_snackbar("Digite um título")

        text_field = TextField(
            label="Adicionar Título")

        dlg_modal = AlertDialog(
            modal=True,
            title=Text("Escreva Título"),
            content=text_field,
            actions=[
                TextButton("Adicionar", on_click=adicionar_texto),
                TextButton("Sair",
                           on_click=lambda e: Pagina.PAGE.close(dlg_modal)),
            ],
            actions_alignment=MainAxisAlignment.END,

        )

        Pagina.PAGE.open(dlg_modal)
