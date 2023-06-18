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
            print("3 - Menu Consultas")
            print("0 - Sair")

            option = input("Opção: ")

            match option:
                case "1":
                    self.show_menu_crud_employee()
                case "2":
                    self.show_menu_crud_user()
                case "3":
                    self.show_menu_consultas()
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
        self.show_title('menu funcionário')
        while True:
            print("Escolha uma opção:")
            print("1 - Adicionar funcionário")
            print("2 - Acessar menu de linhas de ônibus")
            print("3 - Alterar funcionário")
            print("4 - Remover funcionário")
            print("0 - Voltar")

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

        while True:
            print("Escolha uma opção:")
            print("1 - Adicionar linha")
            print("2 - Excluir linha")
            print("3 - Alterar linha")
            print("0 - Voltar")

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
