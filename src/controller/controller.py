from src.controller.controller_crud import ControllerCrud
from src.view.menu import MenuView


class Controller:

    crud = ControllerCrud()
    menu = MenuView()

    def start(self):

        while True:
            option = self.menu.show_options_menu()

            match option:
                case "1":
                    self.crud.insert_employee()
                case "2":
                    self.crud.insert_user()
                case "3":
                    exit()
