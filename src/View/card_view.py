import datetime
from datetime import date
from src.View.validations_view import ValidationsView


class CardMenu:

    def __init__(self):
        self.validations = ValidationsView()

    def request_insert_data(self):

        data = []

        user_id = input("Digite o ID do usuário que possuirá o cartão")

        balance = self.validations.validate_input(
                f"Digite o saldo do cartão",
                self.validations.validate_float,
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

    # todo
    def request_delete_data(self):
        card_id = input("Digite o ID do cartão: ")
        data = []
        return data.append(card_id)

    # todo
    def request_view_data(self):
        pass

    # todo
    def request_update_data(self):
        data = []

        user_id = input("Digite o ID do usuário que possuirá o cartão")

        card_id = input("Digite o ID do cartão: ")

        balance = self.validations.validate_input(
            f"Digite o saldo do cartão",
            self.validations.validate_float,
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
