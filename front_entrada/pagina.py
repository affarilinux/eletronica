from flet import (FloatingActionButton, Icons, ListView,
                  ExpansionPanelList, Colors, ExpansionPanel, ListTile,
                  Text, Column, Row, IconButton)

import flet as ft
import json

from front_entrada.alertdialog_titulo import AlertDialogTitulo
from front_entrada.alertdialog_editartitulo import AlertDialogEditarTitulo
from front_entrada.db.db_pagina import DbPagina
from front_entrada.menores import EntradaMenores


class PaginaEntrada:
    def __init__(self):
        self.fab = None  # Defina o atributo fab aqui

    def entrada_widget_mais(self):

        from front_exe import Pagina

        self.fab = FloatingActionButton(
            icon=Icons.ADD,
            foreground_color="#FFFF00",
            on_click=lambda e: AlertDialogTitulo()
        )

        Pagina.PAGE.floating_action_button = self.fab
        Pagina.PAGE.update()

    def entrada_listview(self):

        from front_exe import Pagina

        def handle_scroll(e: ft.ControlEvent):
            # Converte a string JSON em um dicionário
            data = json.loads(e.data)

            vars = data.get('dir')

            if vars != None:

                # Atualiza o botão flutuante
                if vars == 'forward':
                    self.fab.visible = True

                elif vars == 'reverse':
                    self.fab.visible = False
            Pagina.PAGE.update()

        # Criando a ListView
        self.painel_list = ListView(
            expand=1, spacing=10, padding=20, auto_scroll=True, on_scroll=handle_scroll)

        # Criando o ExpansionPanelList
        panel = ExpansionPanelList(
            expand_icon_color=Colors.AMBER,
            elevation=8,
            divider_color=Colors.AMBER,
            controls=[]
        )

        colors = [
            Colors.GREEN_500,
            Colors.BLUE_800,
            Colors.RED_800,
        ]

        # Obtendo dados do banco de dados e invertendo a ordem
        dados = DbPagina().select_pagina()[::-1]

        for i, (id, dado) in enumerate(dados):

            exp = ExpansionPanel(
                bgcolor=colors[i % len(colors)],
                header=ListTile(title=Text(f"{dado}")),
            )

            exp.content = Column(
                controls=[
                    Row(
                        controls=[
                            IconButton(
                                Icons.DELETE,
                                tooltip="Deletar",
                                data=(exp, id, dado),
                                on_click=lambda e: (
                                    EntradaMenores().menor_apagar_titulo(
                                        e.control.data[1],
                                        e.control.data[2]
                                    )
                                )),
                            IconButton(
                                Icons.EDIT,
                                tooltip="Editar",
                                data=(exp, id),
                                on_click=lambda e: (
                                    AlertDialogEditarTitulo(e.control.data[1]))
                            ),
                        ]
                    ),
                ],
                alignment="start",
            )

            panel.controls.append(exp)
        # Adicionando o ExpansionPanelList dentro da ListView uma única vez
        self.painel_list.controls.append(panel)

        # Adicionando a ListView à página
        Pagina.PAGE.add(self.painel_list)

        # Atualizando a página
        Pagina.PAGE.update()

    def entrada_criar_pagina(self):

        self.entrada_widget_mais()
        self.entrada_listview()

    def entrada_atualizar_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.controls.clear()
        Pagina.PAGE.update()

        self.entrada_criar_pagina()
