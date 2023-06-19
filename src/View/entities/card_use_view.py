from src.view.validations_view import ValidationsView
import datetime


class CardUseMenu:

    def __init__(self):
        self.validations = ValidationsView()

    def request_insert_data(self):

        data = []

        gate_id = int(input("Digite o ID da Catraca: "))

        card_id = input("Digite o Id do Cartao: ")

        date = datetime.date.today()

        hour = datetime.now.strftime("%H:%M:%S")

        data.append((gate_id, card_id, date, hour))

        return data

    def request_delete_data(self):
        card_use_id = input("Digite o ID do Uso do Cartao que deseja remover: ")

        return (card_use_id,)

    def list_data(self):
        pass

    def request_update_data(self):

        data = []

        recharge_id = input("Digite o ID do Uso Do Cartao: ")

        gate_id = int(input("Digite o ID da Catraca: "))

        card_id = input("Digite o Id do Cartao: ")

        date = datetime.date.today()

        hour = datetime.now.strftime("%H:%M:%S")

        data.append((gate_id, card_id, date, hour, recharge_id))

        return data

