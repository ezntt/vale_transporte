from src.model.db_connection import DBConnection
from src.model.sql_scripts import SQLScripts
from src.view.messages_view import ViewMessages


class MainController:

    def __init__(self):
        self.cursor = None
        self.db = DBConnection()
        self.conn = self.db.connect()
        self.sql_scripts = SQLScripts()
        self.message = ViewMessages()

    def start(self):
        from src.view.menu_view import MenuView  # importei aqui para evitar circular import!
        menu = MenuView()
        menu.show_menu()
