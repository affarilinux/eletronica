from flet import SnackBar, Text, FontWeight, Colors


class frontMenores:

    def ativar_snackbar(self, texto):

        from front_exe import Pagina
        self.snackbar = SnackBar(
            Text(texto,
                 color="#4F4F4F",  # Grey
                 size=20,
                 weight=FontWeight.W_900),
        )
        Pagina.PAGE.open(self.snackbar)

        Pagina.PAGE.update()

    def cor_list_view(self):

        return [
            Colors.GREEN_500,
            Colors.BLUE_800,
            Colors.RED_800,
        ]
