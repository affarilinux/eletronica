from flet import (AppBar, Colors, Container, Divider, IconButton,
                  Icons, NavigationDrawer, NavigationDrawerDestination)

from SQLite_db.tabela import SqliteTabela


class Pagina:

    PAGE = None


class FrontExe:

    if_drawer = 0

    def __init__(self, page):
        super().__init__()

        Pagina.PAGE = page

        tab = SqliteTabela()

        self.appbar_janela()
        self.adicionar_janela()

    def appbar_janela(self):

        from front_exe import Pagina

        Pagina.PAGE.appbar = AppBar(
            leading=IconButton(
                icon=Icons.FORMAT_LIST_NUMBERED_OUTLINED,
                icon_color="#FFFF00",
                bgcolor="#808080",
                icon_size=20,
                tooltip="Menu",

                on_click=lambda e: Pagina.PAGE.open(
                    Pagina.PAGE.navigation_drawer)
            ),
            leading_width=40,

            actions=[IconButton(
                Icons.MENU, tooltip="Menu", icon_color=Colors.BLACK87)],
            bgcolor=Colors.BLUE,
            center_title=True,
            color=Colors.WHITE,
        )

        Pagina.PAGE.update()

    def create_navigation_drawer(self):

        Pagina.PAGE.navigation_drawer = NavigationDrawer(

            on_change=lambda e: self.drawer_if(e.control.selected_index),

            controls=[

                Container(height=12),

                NavigationDrawerDestination(
                    label="Leitura",
                    icon=Icons.BOOKMARKS_OUTLINED,
                    selected_icon=Icons.MENU_BOOK,
                ),

                Divider(thickness=2),

                NavigationDrawerDestination(
                    icon=Icons.ADD_CIRCLE_OUTLINE,
                    label="Adicionar",
                    selected_icon=Icons.ADD_CIRCLE_OUTLINED,
                ),
                NavigationDrawerDestination(
                    icon=Icons.PHONE_OUTLINED,
                    label="Item 3",
                    selected_icon=Icons.PHONE,
                ),
            ],
        )

        Pagina.PAGE.update()

    def drawer_if(self, n_drawer):

        if n_drawer != FrontExe.if_drawer:

            self.remover_janela()

            FrontExe.if_drawer = n_drawer

            self.adicionar_janela()

    def remover_janela(self):

        match FrontExe.if_drawer:

            case 0:
                """from front_cronograma.pagina import PaginaCronograma

                home = PaginaCronograma()
                home.cronograma_remover_pagina()"""
                pass

            case 1:
                pass

            case 2:
                pass

    def adicionar_janela(self):

        match FrontExe.if_drawer:

            case 0:
                """from front_cronograma.pagina import PaginaCronograma

                adic = PaginaCronograma()
                adic.cronograma_criar_pagina()"""
                pass

            case 1:
                from front_entrada.pagina import PaginaEntrada

                adic1 = PaginaEntrada()
                adic1.entrada_criar_pagina()

            case 2:
                pass
