from flet import (FloatingActionButton, Icons, Text, FontWeight,
                  IconButton)


class PaginaProduto:

    def produto_actionbtn(self):

        from front_exe import Pagina

        self.fab = FloatingActionButton(
            icon=Icons.ADD,
            foreground_color="#FFFF00",
            # on_click=lambda e: AlertDialogTitulo()
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

    def produto_criar_pagina(self):

        self.produto_actionbtn()
        self.produto_appbar()

    def produto_apagar_pagina(self):

        from front_exe import Pagina

        Pagina.PAGE.floating_action_button = None  # Remove o FloatingActionButton

        Pagina.PAGE.update()
