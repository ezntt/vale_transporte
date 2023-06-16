from src.Controller.controller_crud import ControllerCrud


class MenuView:

    controller_crud = ControllerCrud()
    def show_options_menu(self):
        while True:
            print("Escolha uma opção:")
            print("1. Menu do Funcionário")
            print("2. Menu do Usuário")
            print("3. Sair")

            option = input("Opção: ")

            match option:
                case "1":
                    self.show_option_crud_employee()
                case "2":
                    self.show_option_crud_user()
                case _:
                    print("Opção inválida. Tente novamente.")

    def show_option_crud_user(self):
        while True:
            print("Escolha uma opção:")
            print("1. Adicionar usuário")
            print("2. Sair")

            option = input("Opção: ")

            if option == "1":
                self.controller_crud.insert_user()
            elif option == "2":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def show_option_crud_employee(self):
        while True:
            print("Escolha uma opção:")
            print("1. Adicionar funcionário")
            print("2. Acessar menu de linhas de ônibus")
            print("3. Sair")

            option = input("Opção: ")

            if option == "1":
                self.controller_crud.insert_employee()
            elif option == "2":
                self.show_option_crud_lines()
            elif option == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def show_option_crud_lines(self):

        while True:
            print("Escolha uma opção:")
            print("1. Adicionar linha")
            print("2. Excluir linha")
            print("3. Sair")

            option = input("Opção: ")

            if option == "1":
                self.controller_crud.insert_line()
            elif option == "2":
                print("todo")
            elif option == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")