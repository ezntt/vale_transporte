from src.model.db_connection import DBConnection
from src.view.insert_menu import InsertMenu
from src.view.view_messages import ViewMessages


class ControllerCrud:
    insert_menu = InsertMenu()
    message = ViewMessages()

    def __init__(self):
        self.cursor = None
        self.db_connection = DBConnection()
        self.conn = self.db_connection.connect()

    insertions = {
        'employee': (
            "INSERT INTO Funcionario"
            "(nome, data_nascimento, cpf, salario)"
            "VALUES (%s, %s, %s, %s)"
        ),
        'user': (
            "INSERT INTO Usuario"
            "(id_linha, nome, data_nascimento, cpf, email, telefone, rua, bairro)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        ),
        'line': (
            "INSERT INTO Linha"
            "(id_linha, nome, primeiro_horario, ultimo_horario)"
            "VALUES (%s, %s, %s, %s)"
        ),
        'card': (
            "INSERT INTO Cartao"
            "(id_usuario, saldo, status, validade, ultima_recarga)"
            "VALUES (%s, %s, %s, %s, %s)"
        )}

    def insert_employee(self):
        many_data_employee = self.insert_menu.request_employee_data()
        self.cursor = self.conn.cursor()
        self.cursor.executemany(self.insertions['employee'], many_data_employee)
        self.conn.commit()

    def insert_user(self):
        many_data_user = self.insert_menu.request_user_data()
        self.cursor = self.conn.cursor()
        self.cursor.executemany(self.insertions['user'], many_data_user)
        self.conn.commit()

    def insert_line(self):
        many_data_line = self.insert_menu.request_line_data()
        self.cursor = self.conn.cursor()
        self.cursor.executemany(self.insertions['line'], many_data_line)
        self.conn.commit()
