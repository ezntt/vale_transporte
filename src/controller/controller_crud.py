from src.model.db_connection import DBConnection
from src.model.sql_scripts import SQLScripts
from src.view.insert_menu import InsertMenu
from src.view.view_messages import ViewMessages


class ControllerCrud:
    sql_scripts = SQLScripts()
    insert_menu = InsertMenu()
    message = ViewMessages()

    def __init__(self):
        self.cursor = None
        self.db = DBConnection()
        self.conn = self.db.connect()

    def insert_employee(self):
        self.execute_query(
            self.sql_scripts.employee['insert'],
            self.insert_menu.request_employee_data()
        )

    def insert_user(self):
        self.execute_query(
            self.sql_scripts.user['insert'],
            self.insert_menu.request_user_data()
        )

    def insert_line(self):
        self.execute_query(
            self.sql_scripts.line['insert'],
            self.insert_menu.request_line_data()
        )

    def insert_card(self):
        self.execute_query(
            self.sql_scripts.card['insert'],
            self.insert_menu.request_card_data()
        )

    # todo: passar esse metodo pra DBConnection
    def execute_query(self, query, data):
        self.cursor = self.conn.cursor()
        self.cursor.executemany(query, data)
        self.conn.commit()
