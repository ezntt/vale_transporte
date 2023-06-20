import datetime
from datetime import date

from src.controller.validations_controller import ValidationsController
from src.view.validations_view import ValidationsView


class CardMenu:

    def __init__(self):
        self.validations_view = ValidationsView()
        self.validations_controller = ValidationsController()

    def request_insert_data(self):

        is_empty = self.validations_controller.is_table_empty('user')
        if is_empty:

            data = []

            user_id = input("Digite o ID do usuário que possuirá o cartão")

            balance = self.validations_view.validate_input(
                    f"Digite o saldo do cartão",
                    self.validations_view.validate_float,
                    "Saldo inválido"
                )

            today = datetime.date.today()

            # todo: data de validade daqui a 4 anos
            expiration_date = today + datetime.timedelta(days=(365*4)+1)

            # todo: STATUS: status apenas é ativo quando a data atual é anterior do que a de validade
            last_recharge = today  # acabou de ser criado

            # verificar se isso aqui funciona
            status = 0 if today <= expiration_date else 1

            data.append((user_id, balance, status, expiration_date, last_recharge))

            return data

        else:
            print("tabela usuario vazia")

    def request_delete_data(self):
        card_id = input("Digite o ID do cartão que deseja remover: ")
        return (card_id,)

    # todo
    def request_update_data(self):
        data = []

        user_id = input("Digite o ID do usuário que possuirá o cartão")

        card_id = input("Digite o ID do cartão: ")

        balance = self.validations_view.validate_input(
            f"Digite o saldo do cartão",
            self.validations_view.validate_float,
            "Saldo inválido"
        )

        today = datetime.date.today()

        # todo: data de validade daqui a 4 anos
        expiration_date = today + datetime.timedelta(days=(365 * 4) + 1)

        # todo: STATUS: status apenas é ativo quando a data atual é anterior do que a de validade
        last_recharge = today  # acabou de ser criado

        # verificar se isso aqui funciona
        status = 0 if today <= expiration_date else 1

        data.append((user_id, balance, status, expiration_date, last_recharge,card_id))

        return data
