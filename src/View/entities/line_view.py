from src.view.validations_view import ValidationsView


class LineMenu:

    def __init__(self):
        self.validations_view = ValidationsView()

    def request_insert_data(self):

        data = []

        while True:

            # todo: verificar se a linha existe, caso exista, informe e solicite o ID denovo
            line_id = int(input("Digite o ID da linha: "))

            name = input("Digite o nome da linha: ")

            first_hour = self.validations_view.validate_input(
                f"Digite o primeiro horário de atividade da linha {line_id} (hh:mm): ",
                self.validations_view.validate_time,
                "Horário inválido. Deve seguir o padrão (hh:mm)"
            )

            last_hour = self.validations_view.validate_input(
                f"Digite o último horário de atividade da linha {line_id} (hh:mm): ",
                self.validations_view.validate_time,
                "Horário inválido. Deve seguir o padrão (hh:mm)"
            )

            data.append((line_id, name, first_hour, last_hour))

            add_another = input("Deseja adicionar outra linha? (S/N): ")
            if add_another.upper() != "S":
                break

        return data

    def request_delete_data(self):
        line_id = input("Digite o ID da Linha que deseja remover: ")

        return (line_id,)

    def list_data(self):
        pass

    def request_update_data(self):

        data = []

        # todo: verificar se a linha existe, caso exista, informe e solicite o ID denovo
        line_id = int(input("Digite o ID da linha: "))

        name = input("Digite o nome da linha: ")

        first_hour = self.validations_view.validate_input(
                f"Digite o primeiro horário de atividade da linha {line_id} (hh:mm): ",
                self.validations_view.validate_time,
                "Horário inválido. Deve seguir o padrão (hh:mm)"
            )

        last_hour = self.validations_view.validate_input(
                f"Digite o último horário de atividade da linha {line_id} (hh:mm): ",
                self.validations_view.validate_time,
                "Horário inválido. Deve seguir o padrão (hh:mm)"
            )

        data.append((line_id, name, first_hour, last_hour))

        return data
