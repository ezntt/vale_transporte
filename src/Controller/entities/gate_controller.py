from src.controller.main_controller import MainController
from src.view.entities.gate_view import GateMenu


class GateController(MainController):

    def __init__(self):
        super().__init__()
        self.gate_menu = GateMenu()

    def insert_gate(self):
        self.db.executemany_query(
            self.sql_crud.gate['insert'],
            self.gate_menu.request_insert_data()
        )

    def delete_gate(self):
        self.db.execute_query(
            self.sql_crud.gate['delete'],
            self.gate_menu.request_delete_data()
        )

    def update_gate(self):
        self.db.executemany_query(
            self.sql_crud.gate['update'],
            self.gate_menu.request_update_data()
        )

    def show_gates(self):
        result = self.db.execute_query_no_params(
            self.sql_crud.gate['list']
        )
        self.view_messages.print_list(result)