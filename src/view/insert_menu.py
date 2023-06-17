import datetime
from datetime import date

from src.model.db_connection import DBConnection


class InsertMenu:

    # validations

    def validate_input(self, input_message, validation, error_message):
        while True:
            try:
                user_input = int(input(input_message))
                if validation(user_input):
                    raise ValueError(error_message)
                return user_input
            except ValueError as err:
                print("Erro:", err)

    def validate_year_of_birth(self, year):
        current_year = datetime.date.today().year
        return year > current_year - 18

    def validate_month_of_birth(self, month):
        return month < 1 or month > 12

    def validate_day_of_birth(self, day):
        return day < 1 or day > 31

    # requests

    def request_user_data(self):
        user_data = []

        while True:

            name = input("Digite o primeiro nome do usuário: ")
            surname = input("Digite o sobrenome do usuário")
            full_name = f"{name} {surname}"

            # todo: verificar se a linha existe, caso não exista, informe e solicite o ID denovo
            line_id = int(input("Digite o ID da linha: "))

            day_of_birth = self.validate_input(f"Digite o dia de nascimento do usuário {name}: ",
                                               self.validate_day_of_birth,
                                               "Dia inválido. Deve ser entre 1 e 31.")
            month_of_birth = self.validate_input(f"Digite o mês de nascimento do usuário {name}: ",
                                                 self.validate_month_of_birth,
                                                 "Mês inválido. Deve ser entre 1 e 12.")
            year_of_birth = self.validate_input(f"Digite o ano de nascimento do usuário {name}: ",
                                                self.validate_year_of_birth,
                                                f"Ano inválido. {name} deve ter mais de 18 anos.")
            birthday = date(year_of_birth, month_of_birth, day_of_birth)

            cpf = input("Digite o CPF do usuário: ")

            email = input(f"Digite o email do usuário {name}: ")
            telefone = input(f"Digite o telefone do usuário {name}: ")
            bairro = input(f"Digite o bairro onde {name} reside: ")

            user_data.append((line_id, full_name, birthday, cpf, email, telefone, bairro))

            add_another = input("Deseja adicionar outro usuário? (S/N): ")
            if add_another.upper() != "S":
                break

        return user_data

    def request_employee_data(self):
        employee_data = []

        while True:

            name = input("Digite o primeiro nome do funcionário: ")
            surname = input("Digite o sobrenome do funcionário")
            full_name = f"{name} {surname}"

            day_of_birth = self.validate_input("Digite o dia de nascimento do funcionário: ",
                                               self.validate_day_of_birth,
                                               "Dia inválido. Deve ser entre 1 e 31.")

            month_of_birth = self.validate_input("Digite o mês de nascimento do funcionário: ",
                                                 self.validate_month_of_birth,
                                                 "Mês inválido. Deve ser entre 1 e 12.")

            year_of_birth = self.validate_input("Digite o ano de nascimento do usuárifuncionário: ",
                                                self.validate_year_of_birth,
                                                "Ano inválido. Funcionário deve ter mais de 18 anos.")

            birthday = date(year_of_birth, month_of_birth, day_of_birth)

            cpf = input("Digite o CPF do funcionário: ")

            while True:
                try:
                    salary = float(input("Digite o salário do funcionário: "))
                    break
                except ValueError:
                    print("Salário inválido. Digite um valor numérico.")

            employee_data.append((full_name, birthday, cpf, salary))
            return employee_data

    def request_line_data(self):
        line_data = []

        while True:

            # todo: verificar se a linha existe, caso exista, informe e solicite o ID denovo
            line_id = int(input("Digite o ID da linha: "))

            name = input("Digite o nome da linha: ")

            first_hour = input(f"Digite o primeiro horário de atividade da linha {line_id} (hh:mm): ")
            last_hour = input(f"Digite o último horário de atividade da linha {line_id} (hh:mm): ")

            line_data.append((line_id, name, first_hour, last_hour))

            add_another = input("Deseja adicionar outra linha? (S/N): ")
            if add_another.upper() != "S":
                break

        return line_data

    def request_card_data(self):

        card_data = []

        user_id = input("Digite o ID do usuário que possuirá o cartão")

        balance = input("Digite o saldo do cartãod")

        # todo: terminar, so estou dando push para atualizar
