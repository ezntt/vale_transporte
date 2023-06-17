import datetime
from datetime import date


class InsertMenu:

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

    def validate_cpf(self, cpf):
        if len(str(cpf)) != 11:
            return False
        return True

    def request_user_data(self):
        many_data_user = []

        while True:

            name = input("Digite o nome do usuário: ")

            # todo: verificar se a linha existe, caso não exista, informe e solicite o ID denovo
            line_id = int(input("Digite o ID da linha: "))

            day_of_birth = self.validate_input("Digite o dia de nascimento do usuário: ",
                                               self.validate_day_of_birth,
                                               "Dia inválido. Deve ser entre 1 e 31.")

            month_of_birth = self.validate_input("Digite o mês de nascimento do usuário: ",
                                                 self.validate_month_of_birth,
                                                 "Mês inválido. Deve ser entre 1 e 12.")

            year_of_birth = self.validate_input("Digite o ano de nascimento do usuário: ",
                                                self.validate_year_of_birth,
                                                "Ano inválido. Deve ter mais de 18 anos.")

            birthday = date(year_of_birth, month_of_birth, day_of_birth)

            cpf = self.validate_input("Digite o CPF do usuário: ",
                                      self.validate_cpf,
                                      "CPF inválido. Deve ter 11 caracteres.")

            email = input("Digite o email do usuário: ")
            telefone = input("Digite o telefone do usuário: ")
            rua = input("Digite a rua do usuário: ")
            bairro = input("Digite o bairro do usuário: ")

            many_data_user.append((line_id, name, birthday, cpf, email, telefone, rua, bairro))

            add_another = input("Deseja adicionar outro usuário? (S/N): ")
            if add_another.upper() != "S":
                break

        return many_data_user

    def request_employee_data(self):
        many_data_employee = []

        while True:

            name = input("Digite o nome do funcionário: ")

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

            birthday = date(year_of_birth, month_of_birth, day_of_birth)

            while True:
                try:
                    cpf = input("Digite o CPF do funcionário: ")

                    if len(cpf) != 11:
                        raise ValueError("CPF inválido. Deve ter 11 caracteres.")

                    break

                except ValueError as e:
                    print("Erro: ", e)

            while True:
                try:
                    salario = float(input("Digite o salário do funcionário: "))
                    break
                except ValueError:
                    print("Salário inválido. Digite um valor numérico.")

            many_data_employee.append((name, birthday, cpf, salario))
            return many_data_employee

    def request_line_data(self):
        many_data_line = []

        while True:

            # todo: verificar se a linha existe, caso exista, informe e solicite o ID denovo
            line_id = int(input("Digite o ID da linha: "))

            name = input("Digite o nome da linha: ")

            first_hour = input(f"Digite o primeiro horário de atividade da linha {line_id} (hh:mm): ")
            last_hour = input(f"Digite o último horário de atividade da linha {line_id} (hh:mm): ")

            many_data_line.append((line_id, name, first_hour, last_hour))

            add_another = input("Deseja adicionar outra linha? (S/N): ")
            if add_another.upper() != "S":
                break

        return many_data_line
