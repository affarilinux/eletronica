from flet import (FloatingActionButton, Icons, ListView,
                  ExpansionPanelList, ExpansionPanel, ListTile,
                  Text, Column, Row, IconButton, ControlEvent,
                  FontWeight, CupertinoFilledButton, padding, Container)


import json

from front_entrada.alertdialog_titulo import AlertDialogTitulo
from front_entrada.alertdialog_editartitulo import AlertDialogEditarTitulo
from front_entrada.db.db_pagina import DbPagina
from front_entrada.alertdialogent_adic_titulo import AddAdicionarTitulo
from front_entrada.menores import EntradaMenores
from menores import frontMenores


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

    def criar_list_row_button(self, exp, id, dado):

        return [
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
            IconButton(
                Icons.PLAYLIST_ADD_OUTLINED,
                tooltip="Editar",
                data=(exp, id),
                on_click=lambda e: (
                    AddAdicionarTitulo())
            ),
        ]

    def subentrada_listview(self):
        # Lista de itens para exibir
        itens = [
            "Fio elétrico vermelho 0,6mm\nQt: 3\nVl/Un: 3,44",
            "Fio elétrico verde 0,6mm\nQt: 3 Un\nVl/Un: 3,44",
            "Fio elétrico amarelo 0,6mm\nQt: 3 Un\nValor: 3,44 Un"
        ]

        return ListView(
            expand=True,
            controls=[
                Container(
                    padding=padding.only(bottom=10),  # Espaçamento inferior
                    content=CupertinoFilledButton(content=Text(item))
                )
                for item in itens  # Itera sobre a lista de itens
            ]
        )

    def entrada_listview(self):

        from front_exe import Pagina

        def handle_scroll(e: ControlEvent):
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
            expand_icon_color="#FFFF00",
            elevation=8,
            divider_color="#FFFF00",
            controls=[]
        )

        # Obtendo dados do banco de dados e invertendo a ordem
        dados = DbPagina().select_pagina()[::-1]

        for i, (id, dado) in enumerate(dados):

            exp = ExpansionPanel(
                bgcolor=(frontMenores().cor_list_view()[
                         i % len(frontMenores().cor_list_view())]),
                header=ListTile(title=Text(f"{dado}")),
                expand=True
            )

            exp.content = Column(
                controls=[
                    self.subentrada_listview(),
                    Row(controls=self.criar_list_row_button(exp, id, dado)),
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

    def entrada_appbar(self):
        """Modifica a AppBar existente para a página Entrada"""
        from front_exe import Pagina
        Pagina.PAGE.appbar.title = Text(
            "ENTRADA",
            size=30,
            color="#FFFF00",
            weight=FontWeight.BOLD)

        Pagina.PAGE.update()

    def entrada_criar_pagina(self):

        self.entrada_widget_mais()
        self.entrada_listview()
        self.entrada_appbar()

    def entrada_atualizar_pagina(self):

        from front_exe import Pagina

        self.entrada_apagar_pagina()
        self.entrada_criar_pagina()

    def entrada_apagar_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None  # Remove o FloatingActionButton
        Pagina.PAGE.controls.clear()
        Pagina.PAGE.update()
