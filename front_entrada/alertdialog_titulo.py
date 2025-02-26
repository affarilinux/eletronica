from flet import (Text, TextField, AlertDialog, MainAxisAlignment,
                  TextButton)

from front_entrada.db.db_alertdialog_titulo import DbAlertDialogTitulo
from menores import frontMenores


class AlertDialogTitulo:

    def __init__(self):

        from front_exe import Pagina

        def adicionar_texto(e):

            if text_field.value != "":
                DbAlertDialogTitulo().insert_texto(text_field.value)

                var_sqlite_max = DbAlertDialogTitulo().select_titulo()

                if var_sqlite_max[0][0] == text_field.value:

                    frontMenores().ativar_snackbar("Salvo com sucesso")

                    from front_entrada.pagina import PaginaEntrada

                    PaginaEntrada().entrada_atualizar_pagina()

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
