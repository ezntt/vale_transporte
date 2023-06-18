from datetime import date
from src.view.validations_view import ValidationsView


class EmployeeMenu:

    def __init__(self):
        self.validations = ValidationsView()

    def request_insert_data(self):

        data = []

        while True:

            name = input("Digite o primeiro nome do funcionário: ")
            surname = input("Digite o sobrenome do funcionário: ")
            full_name = f"{name} {surname}"

            day_of_birth = self.validations.validate_input(
                f"Digite o dia de nascimento do funcionário {name}: ",
                self.validations.validate_day,
                "Dia inválido. Deve ser entre 1 e 31.",
                is_int=True
            )

            month_of_birth = self.validations.validate_input(
                f"Digite o mês de nascimento do funcionário {name}: ",
                self.validations.validate_month,
                "Mês inválido. Deve ser entre 1 e 12.",
                is_int=True
            )

            year_of_birth = self.validations.validate_input(
                f"Digite o ano de nascimento do funcionário {name}: ",
                self.validations.validate_year_of_birth,
                "Ano inválido. Funcionário deve ter mais de 18 anos.",
                is_int=True
            )

            birthday = date(year_of_birth, month_of_birth, day_of_birth)

            cpf = self.validations.validate_input(
                f"Digite o CPF do funcionário {name}",
                self.validations.validate_cpf,
                "CPF inválido, deve ter 11 caracteres."
            )

            salary = self.validations.validate_input(
                f"Digite o salário do funcionário {name}",
                self.validations.validate_float,
                "Salário inválido"
            )

            data.append((full_name, birthday, cpf, salary))

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
