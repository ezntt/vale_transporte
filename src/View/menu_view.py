from src.controller.card_controller import CardController
from src.controller.employee_controller import EmployeeController
from src.controller.line_controller import LineController
from src.controller.main_controller import MainController
from src.controller.user_controller import UserController


class MenuView:

    def __init__(self):
        self.main_controller = MainController()
        self.user_controller = UserController()
        self.employee_controller = EmployeeController()
        self.line_controller = LineController()
        self.card_controller = CardController()

    def show_menu_options(self, title, options, is_main_menu=False):
        
        print("\n")
        print("=" * 20)
        print(f"{title.upper()}\n")

        while True:
            print("Escolha uma opção:")
            for i, option in enumerate(options):
                print(f"{i + 1} - {option[0]}")
            print("0 - Sair" if is_main_menu else "0 - Voltar")

            selected_option = input("Opção: ")

            if selected_option == "0":
                if is_main_menu:
                    self.main_controller.db.disconnect()
                    exit()
                else:
                    break

            try:
                selected_option_index = int(selected_option) - 1
                selected_option_func = options[selected_option_index][1]
                selected_option_func()
            except (ValueError, IndexError):
                print("Opção inválida. Tente novamente.")

    def show_menu(self):
        options = [
            ["Menu do Funcionário", self.show_menu_crud_employee],
            ["Menu do Usuário", self.show_menu_crud_user],
            ["Menu do Cartão", self.show_menu_crud_card],
            ["Menu teste", self.show_menu_crud_lines]
        ]
        self.show_menu_options('menu principal', options, is_main_menu=True)

    def show_menu_crud_user(self):
        options = [
            ["Adicionar usuário", self.user_controller.insert_user],
            ["Remover usuário", self.user_controller.delete_user],
            ["Alterar usuário", self.user_controller.update_user],
        ]
        self.show_menu_options('menu do usuário', options)

    def show_menu_crud_employee(self):
        options = [
            ["Adicionar funcionário", self.employee_controller.insert_employee],
            ["Acessar menu de linhas de ônibus", self.show_menu_crud_lines],
            ["Alterar funcionário", self.employee_controller.update_employee],
            ["Remover funcionário", self.employee_controller.delete_employee],
        ]
        self.show_menu_options('menu do funcionário', options)

    def show_menu_crud_lines(self):
        options = [
            ["Adicionar linha", self.line_controller.insert_line],
            ["Excluir linha", self.line_controller.delete_line],
            ["Alterar linha", self.line_controller.update_line],
        ]
        self.show_menu_options('menu de linhas', options)

    def show_menu_crud_card(self):
        options = [
            ["Adicionar cartão", self.card_controller.insert_card],
            ["Remover cartão", self.card_controller.delete_card],
            ["Alterar dados de um cartão", self.card_controller.update_card],
        ]
        self.show_menu_options('menu do cartão', options)

