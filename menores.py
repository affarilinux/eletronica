from flet import SnackBar, Text, FontWeight


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
