import datetime
import re

class ValidationsView:
    def validate_input(self, input_message, validation, error_message, is_int=False):
        while True:
            try:
                user_input = int(input(input_message)) if is_int else input(input_message)
                if validation(user_input):
                    raise ValueError(error_message)
                return user_input
            except ValueError as err:
                print("Erro:", err)

    def validate_year_of_birth(self, year):
        current_year = datetime.date.today().year
        return year > current_year - 18

    def validate_month(self, month):
        return month < 1 or month > 12

    def validate_day(self, day):
        return day < 1 or day > 31

    def validate_cpf(self, cpf):
        return len(cpf) != 11

    def validate_float(self, number):
        return not float(number)

    # todo
    def validate_time(self, time):
        time_pattern = re.compile(r'^([01]\d|2[0-3]):([0-5]\d)$')
        return not bool(time_pattern.match(time))