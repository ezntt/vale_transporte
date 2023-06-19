from datetime import date

from src.controller.validations_controller import ValidationsController
from src.view.validations_view import ValidationsView


class UserMenu:

    def __init__(self):
        self.validations_view = ValidationsView()
        self.validations_controller = ValidationsController()

    def request_insert_data(self):

        data = []

        while True:

            name = input("Digite o primeiro nome do usuário: ")
            surname = input("Digite o sobrenome do usuário")
            full_name = f"{name} {surname}"

            while True:
                # todo: verificar se a linha existe, caso não exista, informe e solicite o ID denovo
                line_id = int(input("Digite o ID da linha: "))

                if self.validations_controller.validate_line_id(line_id):
                    print("linha existe")
                    break
                else:
                    print("linha não existe")

            day_of_birth = self.validations_view.validate_input(
                f"Digite o dia de nascimento do usuário {name}: ",
                self.validations_view.validate_day,
                "Dia inválido. Deve ser entre 1 e 31.",
                is_int=True
            )

            month_of_birth = self.validations_view.validate_input(
                f"Digite o mês de nascimento do usuário {name}: ",
                self.validations_view.validate_month,
                "Mês inválido. Deve ser entre 1 e 12.",
                is_int=True
            )

            year_of_birth = self.validations_view.validate_input(
                f"Digite o ano de nascimento do usuário {name}: ",
                self.validations_view.validate_year_of_birth,
                f"Ano inválido. {name} deve ter mais de 18 anos.",
                is_int=True
            )

            birthday = date(year_of_birth, month_of_birth, day_of_birth)

            cpf = self.validations_view.validate_input(
                f"Digite o CPF do usuário {name}",
                self.validations_view.validate_cpf,
                "CPF inválido, deve ter 11 caracteres."
            )

            email = input(f"Digite o email do usuário {name}: ")
            telefone = input(f"Digite o telefone do usuário {name}: ")
            bairro = input(f"Digite o bairro onde {name} reside: ")

            data.append((line_id, full_name, birthday, cpf, email, telefone, bairro))

            add_another = input("Deseja adicionar outro usuário? (S/N): ")
            if add_another.upper() != "S":
                break

        return data

    # todo
    def request_delete_data(self):
        pass

    # todo
    def request_view_data(self):
        pass

    # todo
    def request_update_data(self):
        pass
