from src.Controller.controller_crud import ControllerCrud


class MenuView:

    controller_crud = ControllerCrud()
    def show_options_menu(self):
        while True:
            print("Escolha uma opção:")
            print("1. Opcoes funcionário")
            print("2. Opcoes usuário")
            print("3. Sair")

            opcao = input("Opção: ")

            match opcao:
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

            opcao = input("Opção: ")

            if opcao == "1":
                self.controller_crud.insert_user()
            elif opcao == "2":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def show_option_crud_employee(self):
        while True:
            print("Escolha uma opção:")
            print("1. Adicionar funcionário")
            print("2. Sair")

            opcao = input("Opção: ")

            if opcao == "1":
                self.controller_crud.insert_employeee()
            elif opcao == "2":
                break
            else:
                print("Opção inválida. Tente novamente.")
