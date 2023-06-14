from src.Controller.controller_crud import ControllerCrud
from src.View.menu import MenuView


class Controller:
    crud = ControllerCrud()
    menu = MenuView()

    def Start(self):
        while True:
            opcao = self.menu.show_options()
            match opcao:
                case "1":
                    self.crud.insert_employeee()
                case "2":
                    self.crud.insert_user()
