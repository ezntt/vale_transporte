from src.controller.entities.card_use_controller import CardUseController
from src.controller.main_controller import MainController
from src.controller.entities.card_controller import CardController
from src.controller.entities.employee_controller import EmployeeController
from src.controller.entities.line_controller import LineController
from src.controller.entities.user_controller import UserController
from src.controller.entities.gate_controller import GateController
from src.controller.entities.recharge_controller import RechargeController
from src.controller.queries_controller import QueriesController
from src.view.messages_view import ViewMessages


class MenuView:

    def __init__(self):
        self.main_controller = MainController()
        self.user_controller = UserController()
        self.employee_controller = EmployeeController()
        self.line_controller = LineController()
        self.card_controller = CardController()
        self.gate_controller = GateController()
        self.recharge_controller = RechargeController()
        self.card_use_controller = CardUseController()
        self.queries_controller = QueriesController()
        self.view_messages = ViewMessages()

    def show_menu_options(self, title, options, is_main_menu=False):

        self.view_messages.print_data("\n")
        self.view_messages.print_data("=" * 20)
        self.view_messages.print_data(f"{title.upper()}\n")

        while True:
            self.view_messages.print_data("Escolha uma opção:")
            for i, option in enumerate(options):
                self.view_messages.print_data(f"{i + 1} - {option[0]}")
            self.view_messages.print_data("0 - Sair" if is_main_menu else "0 - Voltar")

            selected_option = input("Opção: ")

            if selected_option == "0":
                if is_main_menu:
                    self.main_controller.db.disconnect()
                    exit()
                else:
                    break

            try:
                selected_option_index = int(selected_option) - 1
                selected_option_function = options[selected_option_index][1]
                selected_option_function()
            except (ValueError, IndexError):
                self.view_messages.print_data("Opção inválida. Tente novamente.")

    def show_main_menu(self):
        options = [
            ["Menu do Funcionário", self.show_menu_crud_employee],
            ["Menu do Usuário", self.show_menu_crud_user],
            ["Menu do Cartão", self.show_menu_crud_card],
            ["Menu da Catraca", self.show_menu_crud_gate],
            ["Menu de Consultas", self.show_menu_queries],
        ]
        self.show_menu_options('menu principal', options, is_main_menu=True)

    def show_menu_crud_user(self):
        options = [
            ["Adicionar usuário", self.user_controller.insert_user],
            ["Remover usuário", self.user_controller.delete_user],
            ["Alterar usuário", self.user_controller.update_user],
            ["Listar usuário", self.user_controller.show_users],
            ["Menu do Uso do cartão", self.show_menu_crud_card_use],
        ]
        self.show_menu_options('menu do usuário', options)

    def show_menu_crud_employee(self):
        options = [
            ["Adicionar funcionário", self.employee_controller.insert_employee],
            ["Alterar funcionário", self.employee_controller.update_employee],
            ["Remover funcionário", self.employee_controller.delete_employee],
            ["Listar funcionários", self.employee_controller.show_employees],
            ["Acessar menu de linhas de ônibus", self.show_menu_crud_lines],
            ["Acessar o menu de recargas", self.show_menu_crud_recharge],
        ]
        self.show_menu_options('menu do funcionário', options)

    def show_menu_crud_lines(self):
        options = [
            ["Adicionar linha", self.line_controller.insert_line],
            ["Alterar linha", self.line_controller.update_line],
            ["Remover linha", self.line_controller.delete_line],
            ["Listar linhas", self.line_controller.show_lines],
        ]
        self.show_menu_options('menu de linhas', options)

    def show_menu_crud_card(self):
        options = [
            ["Adicionar cartão", self.card_controller.insert_card],
            ["Remover cartão", self.card_controller.delete_card],
            ["Alterar dados de um cartão", self.card_controller.update_card],
            ["Listar cartoes", self.card_controller.show_cards],
        ]
        self.show_menu_options('menu do cartão', options)

    def show_menu_crud_gate(self):
        options = [
            ["Adicionar Catraca", self.gate_controller.insert_gate],
            ["Remover Catraca", self.gate_controller.delete_gate],
            ["Alterar Catraca", self.gate_controller.update_gate],
            ["Listar Catracas", self.gate_controller.show_gates],
        ]
        self.show_menu_options('menu da catraca', options)

    def show_menu_crud_recharge(self):
        options = [
            ["Adicionar Recarga", self.recharge_controller.insert_recharge],
            ["Remover Recarga", self.recharge_controller.delete_recharge],
            ["Alterar Recarga", self.recharge_controller.update_recharge],
            ["Listar Recargas", self.recharge_controller.show_recharges],
        ]
        self.show_menu_options('menu das recargas', options)

    def show_menu_crud_card_use(self):
        options = [
            ["Usar Cartao", self.card_use_controller.insert_card_use],
            ["Remover Uso Do Cartao", self.card_use_controller.delete_card_use],
            ["Alterar Uso do Cartao", self.card_use_controller.update_card_use],
            ["Listar Uso do Cartao", self.card_use_controller.show_card_use],
        ]
        self.show_menu_options('menu do uso do cartao', options)
        
    def show_menu_queries(self):
        options = [
            ["Funcionarios que mais fizeram recargas", self.queries_controller.show_consulta_1],
            ["Linhas que Mais foram Usadas", self.queries_controller.show_consulta_2],
            ["Todos os usuários e o saldo do cartão deles", self.queries_controller.show_consulta_3],
        ]
        self.show_menu_options('menu das consultas', options)
