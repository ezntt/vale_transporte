from src.view.menu_view import MenuView


class Controller:

    menu = MenuView()

    def start(self):
        self.menu.show_menu()
