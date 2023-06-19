from src.view.validations_view import ValidationsView


class GateMenu:

    def __init__(self):
        self.validations = ValidationsView()

    def request_insert_data(self):

        data = []

        while True:

            # todo: verificar se a linha existe, caso exista, informe e solicite o ID denovo
            user_id = int(input("Digite o ID da linha: "))

            price = self.validations.validate_input(
                f"Digite o Preco da tarifa",
                self.validations.validate_float,
                "Tarifa inválida"
            )

            data.append((user_id, price))

            add_another = input("Deseja adicionar outra linha? (S/N): ")
            if add_another.upper() != "S":
                break

        return data

    # todo
    def request_delete_data(self):
        gate_id = input("Digite o ID da catraca: ")
        data = []
        return data.append(gate_id)

    # todo
    def request_view_data(self):
        pass

    # todo
    def request_update_data(self):
        data = []
        gate_id = int(input("Digite o ID da catraca: "))
        user_id = int(input("Digite o ID da linha: "))

        price = self.validations.validate_input(
            f"Digite o Preco da tarifa",
            self.validations.validate_float,
            "Tarifa inválida"
        )

        return data.append((user_id, price, gate_id))
