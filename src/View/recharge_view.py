from src.view.validations_view import ValidationsView
import datetime


class RechargeMenu:

    def __init__(self):
        self.validations = ValidationsView()

    def request_insert_data(self):

        data = []

        while True:
            card_id = int(input("Digite o ID do Cartao: "))

            employee_id = input("Digite o Id do Funcionario: ")

            value = self.validations.validate_input(
                f"Digite o Valor da recarga",
                self.validations.validate_float,
                "Valor inválida"
            )
            date = datetime.date.today()

            data.append((card_id, employee_id, value, date))

            add_another = input("Deseja Fazer outra recarga? (S/N): ")
            if add_another.upper() != "S":
                break

        return data

    # todo
    def request_delete_data(self):
        recharge_id = input("Digite o ID da recarga: ")
        data = []
        return data.append(recharge_id)

    # todo
    def request_view_data(self):
        pass

    # todo
    def request_update_data(self):

        data = []

        recharge_id = input("Digite o ID da recarga: ")

        card_id = int(input("Digite o ID do Cartao: "))

        employee_id = input("Digite o Id do Funcionario: ")

        value = self.validations.validate_input(
                f"Digite o Valor da recarga",
                self.validations.validate_float,
                "Valor inválida"
            )
        date = datetime.date.today()

        data.append((card_id, employee_id, value, date, recharge_id))
        return data

