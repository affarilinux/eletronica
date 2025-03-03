from flet import (FloatingActionButton, Icons, Text, FontWeight,
                  IconButton, ControlEvent, ListView, ExpansionPanelList,
                  ExpansionPanel, Column, Row, ListTile)

import json

from front_configuracao.front_produto.alertdialogprod_titulo import (
    AddTituloProduto
)
from front_configuracao.front_produto.db_produto.db_pd_pagina import (
    DbPdPagina
)
from front_configuracao.front_produto.alertdialigpd_editartitulo import (
    AddPdEditarTitulo
)
from front_configuracao.front_produto.menores import ProdutoMenores
from menores import frontMenores


class PaginaProduto:

    def produto_actionbtn(self):

        from front_exe import Pagina

        self.fab = FloatingActionButton(
            icon=Icons.ADD,
            foreground_color="#FFFF00",
            on_click=lambda e: AddTituloProduto()
        )

        Pagina.PAGE.floating_action_button = self.fab
        Pagina.PAGE.update()

    def produto_appbar(self):
        """Modifica a AppBar existente para a página Entrada"""
        from front_exe import Pagina
        from front_configuracao.pagina import PaginaConfiguracao
        Pagina.PAGE.appbar.title = Text(
            "PRODUTO",
            size=30,
            color="#FFFF00",
            weight=FontWeight.BOLD)

        Pagina.PAGE.appbar.leading = IconButton(
            icon=Icons.KEYBOARD_DOUBLE_ARROW_LEFT,
            icon_color="#FFFF00",
            bgcolor="#808080",
            icon_size=20,
            tooltip="Menu",
            on_click=lambda e: (
                PaginaConfiguracao().configuracao_update_switch(2, 0),
                PaginaConfiguracao().configuracao_appbar_loading_drawer())
        )
        Pagina.PAGE.update()

    def criar_list_row_button(self, exp, id, dado):

        return [
            IconButton(
                Icons.DELETE,
                tooltip="Deletar",
                data=(exp, id, dado),
                on_click=lambda e: (
                    ProdutoMenores().menor_apagar_titulo(
                        e.control.data[1],
                    )
                )),

            IconButton(
                Icons.EDIT,
                tooltip="Editar",
                data=(exp, id),
                on_click=lambda e: (
                    AddPdEditarTitulo(e.control.data[1]))
            ),
        ]

    def produto_listview(self):

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
        dados = DbPdPagina().select_pagina()[::-1]

        for i, (id, dado) in enumerate(dados):

            exp = ExpansionPanel(
                bgcolor=(frontMenores().cor_list_view()[
                         i % len(frontMenores().cor_list_view())]),
                header=ListTile(title=Text(f"{dado}")),
            )

            exp.content = Column(
                controls=[
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

    def produto_criar_pagina(self):

        self.produto_actionbtn()
        self.produto_appbar()
        self.produto_listview()

    def produto_update_pagina(self):

        self.produto_apagar_pagina()
        self.produto_criar_pagina()

    def produto_apagar_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None  # Remove o FloatingActionButton
        Pagina.PAGE.controls.clear()
        Pagina.PAGE.update()
