
from flet import (Text, TextField, AlertDialog, MainAxisAlignment,
                  TextButton)

from front_configuracao.front_produto.db_produto.db_addpd_editartitulo import (
    DbAddPdEditarTitulo
)

from menores import frontMenores


class AddPdEditarTitulo:

    def __init__(self, id_titulo):

        from front_exe import Pagina

        def editar_texto(e):

            if text_field.value != "":
                DbAddPdEditarTitulo().update_uptitulo(id_titulo, text_field.value)

                var_sqlite_max = DbAddPdEditarTitulo().select_titulo(id_titulo)

                if var_sqlite_max[0][0] == text_field.value:

                    frontMenores().ativar_snackbar("Salvo com sucesso")

                    from front_configuracao.front_produto.pagina import (
                        PaginaProduto
                    )

                    PaginaProduto().produto_update_pagina()

                    Pagina.PAGE.close(dlg_modal_up)

            elif text_field.value == "":

                frontMenores().ativar_snackbar("Digite um título")

        text_field = TextField(
            label="Adicionar Título")

        dlg_modal_up = AlertDialog(
            modal=True,
            title=Text("Editar Título"),
            content=text_field,
            actions=[
                TextButton("Editar", on_click=editar_texto),
                TextButton("Sair",
                           on_click=lambda e: Pagina.PAGE.close(dlg_modal_up)),
            ],
            actions_alignment=MainAxisAlignment.END,

        )

        Pagina.PAGE.open(dlg_modal_up)
