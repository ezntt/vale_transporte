import mysql
import mysql.connector
from src.View.insert_menu import InsertMenu
from src.View.menu import MenuView


class ControllerCrud:

    insert_menu = InsertMenu()
    menu = MenuView()
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='root',
                                       host='localhost',
                                       database='vale_transporte')
        self.cursor = None
        if self.conn.is_connected():
            db_info = self.conn.get_server_info()
            self.menu.print_data("Conectado ao servidor MySQL versão " + str(db_info))
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT DATABASE();")
            linha = self.cursor.fetchone()
            self.menu.print_data("Conectado ao banco de dados " + str(linha))
        else:
            conn.close()
            self.menu.print_data("Conexão ao MySQL foi encerrada")


    insert_employee_dml = (
        "INSERT INTO Funcionario "
        "(nome, data_nascimento, cpf, salario) "
        "VALUES (%s, %s, %s, %s)"
    )

    insert_user_dml = (
        "INSERT INTO Usuario "
        "(id_linha, nome, data_nascimento, cpf, email, telefone, rua, bairro) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    )


    def insert_employeee(self):
        many_data_employee = self.insert_menu.request_employee_data()
        self.cursor.executemany(self.insert_employee_dml, many_data_employee)
        self.conn.commit()

    def insert_user(self):
        many_data_user = self.insert_menu.request_user_data()
        self.cursor.executemany(self.insert_user_dml, many_data_user)
        self.conn.commit()
