import mysql
import mysql.connector
from src.View.insert_menu import InsertMenu
from src.View.view_messages import ViewMessages


class ControllerCrud:
    insert_menu = InsertMenu()
    message = ViewMessages()

    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='password',
                                            host='localhost',
                                            database='vale_transporte')
        self.cursor = None
        if self.conn.is_connected():
            db_info = self.conn.get_server_info()
            self.message.print_data("Conectado ao servidor MySQL versão " + str(db_info))
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT DATABASE();")
            linha = self.cursor.fetchone()
            self.message.print_data("Conectado ao banco de dados " + str(linha))
        else:
            self.conn.close()
            self.message.print_data("Conexão ao MySQL foi encerrada")

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
        self.cursor.executemany(self.insertions['employee'], many_data_employee)
        self.conn.commit()

    def insert_user(self):
        many_data_user = self.insert_menu.request_user_data()
        self.cursor.executemany(self.insertions['user'], many_data_user)
        self.conn.commit()

    def insert_line(self):
        many_data_line = self.insert_menu.request_line_data()
        self.cursor.executemany(self.insertions['line'], many_data_line)
        self.conn.commit()

    def insert_card(self):
        many_data_card = self.insert_menu.request_card_data()
        self.cursor.executemany(self.insertions['card'], many_data_card)
        self.conn.commit()
