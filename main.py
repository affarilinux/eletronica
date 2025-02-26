from flet import Page, app

from front_exe import FrontExe


def main(page: Page):

    page.adaptive = True
    page.bgcolor = "#808080"
    page.title = "Eletronica Rural"

    page.update()

    APP_EXE = FrontExe(page)
    APP_EXE.create_navigation_drawer()


if __name__ == "__main__":
    app(target=main)
