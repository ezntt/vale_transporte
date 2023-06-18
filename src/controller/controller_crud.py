from src.model.db_connection import DBConnection
from src.model.sql_scripts import SQLScripts
from src.view.card_view import CardMenu
from src.view.employee_view import EmployeeMenu
from src.view.line_view import LineMenu
from src.view.user_view import UserMenu
from src.view.messages_view import ViewMessages


class ControllerCrud:
    sql_scripts = SQLScripts()

    employee_menu = EmployeeMenu()
    user_menu = UserMenu()
    line_menu = LineMenu()
    card_menu = CardMenu()

    message = ViewMessages()

    def __init__(self):
        self.cursor = None
        self.db = DBConnection()
        self.conn = self.db.connect()

    def insert_employee(self):
        self.executemany_query(
            self.sql_scripts.employee['insert'],
            self.employee_menu.request_insert_data()
        )

    def insert_user(self):
        self.executemany_query(
            self.sql_scripts.user['insert'],
            self.user_menu.request_insert_data()
            # self.insert_menu.request_user_data()
        )

    def insert_line(self):
        self.executemany_query(
            self.sql_scripts.line['insert'],
            self.line_menu.request_insert_data()
        )

    def insert_card(self):
        self.executemany_query(
            self.sql_scripts.card['insert'],
            self.card_menu.request_insert_data()
        )

    # todo: passar esse metodo pra DBConnection
    def executemany_query(self, query, data):
        self.cursor = self.conn.cursor()
        self.cursor.executemany(query, data)
        self.conn.commit()
