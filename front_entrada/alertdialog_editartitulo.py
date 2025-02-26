
from flet import (Text, TextField, AlertDialog, MainAxisAlignment,
                  TextButton)

from front_entrada.db.db_alertdialog_editartitulo import DbAlertDialogEditarTitulo
from menores import frontMenores


class AlertDialogEditarTitulo:

    def __init__(self, id_titulo):

        from front_exe import Pagina

        def editar_texto(e):

            if text_field.value != "":
                DbAlertDialogEditarTitulo().update_uptitulo(id_titulo, text_field.value)

                var_sqlite_max = DbAlertDialogEditarTitulo().select_titulo(id_titulo)

                if var_sqlite_max[0][0] == text_field.value:

                    frontMenores().ativar_snackbar("Salvo com sucesso")

                    from front_entrada.pagina import PaginaEntrada

                    PaginaEntrada().entrada_atualizar_pagina()

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
