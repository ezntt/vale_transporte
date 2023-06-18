from src.controller.controller_crud import ControllerCrud


class MenuView:

    controller_crud = ControllerCrud()

    def show_title(self, title):
        print("\n")
        print("="*20)
        print(f"{title.upper()}\n")

    def show_menu(self):
        self.show_title('menu principal')
        while True:
            print("Escolha uma opção:")
            print("1 - Menu do Funcionário")
            print("2 - Menu do Usuário")
            print("3 - Menu do Cartão")
            print("0 - Sair")

            option = input("Opção: ")

            match option:
                case "1":
                    self.show_menu_crud_employee()
                case "2":
                    self.show_menu_crud_user()
                case "3":
                    self.show_menu_crud_card()
                case "0":
                    exit()
                case _:
                    print("Opção inválida. Tente novamente.")

    def show_menu_crud_user(self):
        self.show_title('menu do usuário')
        while True:
            print("Escolha uma opção:")
            print("1 - Adicionar usuário")
            print("2 - Remover usuário")
            print("3 - Alterar usuário")
            print("0 - Voltar")

            option = input("Opção: ")

            match option:
                case "1":
                    self.controller_crud.insert_user()
                case "2":
                    self.controller_crud.remove_user()
                case "3":
                    print("Todo")
                case "0":
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    def show_menu_crud_employee(self):
        self.show_title('menu do funcionário')
        while True:
            print("Escolha uma opção:")
            print("1 - Adicionar funcionário\n"
                  "2 - Acessar menu de linhas de ônibus\n"
                  "3 - Alterar funcionário\n"
                  "4 - Remover funcionário\n"
                  "0 - Voltar para o menu principal")

            option = input("Opção: ")

            match option:
                case "1":
                    self.controller_crud.insert_employee()
                case "2":
                    self.show_menu_crud_lines()
                case "3":
                    print("Todo")
                case "4":
                    print("Todo")
                case "0":
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    def show_menu_crud_lines(self):
        self.show_title('menu de linhas')
        while True:
            print("Escolha uma opção:")
            print("1 - Adicionar linha\n"
                  "2 - Excluir linha\n"
                  "3 - Alterar linha\n"
                  "0 - Voltar para o menu do funcionário")

            option = input("Opção: ")

            match option:
                case "1":
                    self.controller_crud.insert_line()
                case "2":
                    print("todo")
                case "3":
                    print("Todo")
                case "0":
                    break
                case _:
                    print("Opção inválida. Tente novamente.")

    def show_menu_crud_card(self):
        self.show_title('menu do cartão')
        while True:
            print("Escolha uma opção:")
            print("1 - Adicionar cartão\n"
                  "2 - Remover cartão\n"
                  "3 - Alterar dados de um cartão\n"
                  "4 - Mostrar cartões disponíveis\n"
                  "0 - Voltar para o menu principal")

            option = input("Opção: ")

            match option:
                case "1":
                    self.controller_crud.insert_card()
                case "2":
                    self.controller_crud.delete_card()
                case "3":
                    print("Todo")
                case "0":
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
