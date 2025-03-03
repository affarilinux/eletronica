from flet import (Column, Row, ButtonStyle, colors, FilledButton,
                  Text, FontWeight, Icons, IconButton)

from front_exe import Pagina  # Importar Pagina uma vez no início

from front_configuracao.front_produto.pagina import PaginaProduto


class PaginaConfiguracao:
    apagar = 0

    def __init__(self):
        self.coluna = None  # Inicializa como None

    def configuracao_botao(self):

        fille_produto = FilledButton(
            text="Produto",
            expand=True,
            on_click=lambda e: self.configuracao_update_switch(2, 1),
            style=ButtonStyle(
                bgcolor=colors.BLUE,
                color=colors.WHITE,
            ),
        )

        # Adicione outros controles aqui, se necessário
        self.coluna = Column(
            [
                Row(controls=[
                    fille_produto
                ])  # Adicione outros controles aqui
            ],
            spacing=10
        )

        Pagina.PAGE.add(self.coluna)
        Pagina.PAGE.update()

        # Debug

    def configuracao_appbar(self):
        """Modifica a AppBar existente para a página Entrada"""
        from front_exe import Pagina
        Pagina.PAGE.appbar.title = Text(
            "CONFIGURAÇÃO",
            size=30,
            color="#FFFF00",
            weight=FontWeight.BOLD)

        Pagina.PAGE.update()

    def configuracao_appbar_loading_drawer(self):
        """Modifica a AppBar existente para a página Entrada"""
        from front_exe import Pagina
        Pagina.PAGE.appbar.leading = IconButton(
            icon=Icons.FORMAT_LIST_NUMBERED_OUTLINED,
            icon_color="#FFFF00",
            bgcolor="#808080",
            icon_size=20,
            tooltip="Menu",

            on_click=lambda e: Pagina.PAGE.open(
                    Pagina.PAGE.navigation_drawer)
        )

        Pagina.PAGE.update()

    def configuracao_update_switch(self, n_switch, n_index):

        match n_switch:
            case 1:

                self.switch_criar_pagina()

            case 0:

                self.configuracao_apagar_pagina()

            case 2:

                print(PaginaConfiguracao.apagar, n_index)
                self.switch_apagar()

                PaginaConfiguracao.apagar = n_index

                self.switch_criar_pagina()

    def switch_apagar(self):

        match PaginaConfiguracao.apagar:

            case 0:
                self.configuracao_apagar_pagina()
            # Atualiza o estado para indicar que a página foi apagada

            case 1:

                PaginaProduto().produto_apagar_pagina()

    def switch_criar_pagina(self):

        match PaginaConfiguracao.apagar:

            case 0:
                self.configuracao_criar_pagina()
            # Atualiza o estado para indicar que a página foi criada

            case 1:

                PaginaProduto().produto_criar_pagina()

    def configuracao_criar_pagina(self):

        self.configuracao_botao()
        self.configuracao_appbar()

    def configuracao_apagar_pagina(self):
        """Remove todos os controles da página"""
        Pagina.PAGE.controls.clear()
        self.coluna = None  # Limpando referência
        Pagina.PAGE.update()
