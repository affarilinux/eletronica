
from flet import (Text, TextField, AlertDialog, MainAxisAlignment,
                  TextButton, Column, Container, AutoComplete,
                  )

from front_entrada.db.db_alertdialog_titulo import DbAlertDialogTitulo
from menores import frontMenores

from front_entrada.db.db_alertdialogent_adic_titulo import DbAddadicionartitulo


class AddAdicionarTitulo:

    def __init__(self):

        from front_exe import Pagina

        def adicionar_texto(e):

            if auto_complete.value != "" and text_field1.value != "":
                DbAlertDialogTitulo().insert_texto(text_field.value)

                var_sqlite_max = DbAlertDialogTitulo().select_titulo()

                if var_sqlite_max[0][0] == text_field.value:

                    frontMenores().ativar_snackbar("Salvo com sucesso")

                    from front_entrada.pagina import PaginaEntrada

                    PaginaEntrada().entrada_atualizar_pagina()

                    Pagina.PAGE.close(dlg_modal)

            elif auto_complete.value == "" or text_field1.value == "":

                frontMenores().ativar_snackbar("Digite um título")

        def on_select(e):
            auto_complete.suggestions = DbAddadicionartitulo(
            ).dbent_select_filtrar_dados(auto_complete.value)
            Pagina.PAGE.update()

        auto_complete = AutoComplete(
            suggestions=DbAddadicionartitulo().dbent_select_filtrar_dados(""),
            on_select=on_select
        )

        text_field1 = TextField(
            label="Adicionar Quantidade"
        )

        text_field2 = TextField(
            label="Adicionar valor unidade"
        )

        coluna_add = Column(controls=[
            auto_complete,
            text_field1,
            text_field2

        ], tight=True)  # tight remove espaços extras.

        dlg_modal = AlertDialog(
            modal=True,
            title=Text("Escreva Título"),
            content=Container(content=coluna_add),
            actions=[
                TextButton("Adicionar", on_click=adicionar_texto),
                TextButton("Sair",
                           on_click=lambda e: Pagina.PAGE.close(dlg_modal)),
            ],
            actions_alignment=MainAxisAlignment.END,
        )

        Pagina.PAGE.open(dlg_modal)
