from datetime import date


class InsertMenu:

    def request_user_data(self):
        num_users = int(input("Quantos usuários deseja adicionar? "))

        many_data_user = []

        for _ in range(num_users):
            id_linha = int(input("Digite o ID da linha: "))
            name = input("Digite o nome do usuário: ")
            year_of_birth = int(input("Digite o ano de nascimento do usuário: "))

            while True:
                try:
                    month_of_birth = int(input("Digite o mês de nascimento do usuário: "))
                    if month_of_birth < 1 or month_of_birth > 12:
                        raise ValueError("Mês inválido. Digite um valor entre 1 e 12.")
                    break
                except ValueError as e:
                    print("Erro:", e)

            while True:
                try:
                    day_of_birth = int(input("Digite o dia de nascimento do usuário: "))
                    if day_of_birth < 1 or day_of_birth > 31:
                        raise ValueError("Dia inválido. Digite um valor entre 1 e 31.")
                    break
                except ValueError as e:
                    print("Erro:", e)

            birthday = date(year_of_birth, month_of_birth, day_of_birth)

            while True:
                try:
                    cpf = input("Digite o CPF do usuário: ")

                    if len(cpf) != 11:
                        raise ValueError("CPF inválido. Deve ter 11 caracteres.")

                    break
                except ValueError as e:
                    print("Erro:", e)

            email = input("Digite o email do usuário: ")
            telefone = input("Digite o telefone do usuário: ")
            rua = input("Digite a rua do usuário: ")
            bairro = input("Digite o bairro do usuário: ")

            many_data_user.append((id_linha, name, birthday, cpf, email, telefone, rua, bairro))

        return many_data_user


    def request_employee_data(self):
        num_employees = int(input("Quantos funcionários deseja adicionar? "))

        many_data_employee = []

        for _ in range(num_employees):

            name = input("Digite o nome do funcionário: ")
            year_of_birth = int(input("Digite o ano de nascimento do funcionário: "))

            while True:

                try:
                    month_of_birth = int(input("Digite o mês de nascimento do funcionário: "))
                    if month_of_birth < 1 or month_of_birth > 12:
                        raise ValueError("Mês inválido. Digite um valor entre 1 e 12.")

                    break

                except ValueError as e:
                    print("Erro:", e)

            while True:

                try:
                    day_of_birth = int(input("Digite o dia de nascimento do funcionário: "))
                    if day_of_birth < 1 or day_of_birth > 31:
                        raise ValueError("Dia inválido. Digite um valor entre 1 e 31.")
                    break

                except ValueError as e:
                    print("Erro:", e)

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
