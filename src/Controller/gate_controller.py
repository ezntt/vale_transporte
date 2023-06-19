from src.Controller.main_controller import MainController
from src.View.gate_view import GateMenu


class GateController(MainController):

    def __init__(self):
        super().__init__()
        self.gate_menu = GateMenu()

    def insert_line(self):
        self.db.executemany_query(
            self.sql_scripts.gate['insert'],
            self.gate_menu.request_insert_data()
        )

    def delete_line(self):
        self.db.executemany_query(
            self.sql_scripts.gate['delete'],
            self.gate_menu.request_delete_data()
        )

    def update_line(self):
        self.db.executemany_query(
            self.sql_scripts.gate['update'],
            self.gate_menu.request_update_data()
        )
