from src.model.db_connection import DBConnection
from src.model.sql_crud import SQLCrud
from src.view.messages_view import ViewMessages


class MainController:

    def __init__(self):
        self.cursor = None
        self.db = DBConnection()
        self.conn = self.db.connect()
        self.sql_crud = SQLCrud()
        self.message = ViewMessages()

    def start(self):
        from src.view.menu_view import MenuView  # importei aqui para evitar circular import!
        MenuView().show_main_menu()
