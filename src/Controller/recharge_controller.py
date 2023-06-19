from src.controller.main_controller import MainController
from src.view.gate_view import GateMenu
from src.view.recharge_view import RechargeMenu


class RechargeController(MainController):

    def __init__(self):
        super().__init__()
        self.recharge_menu = RechargeMenu()

    def insert_recharge(self):
        self.db.executemany_query(
            self.sql_scripts.recharge['insert'],
            self.recharge_menu.request_insert_data()
        )

    def delete_recharge(self):
        self.db.executemany_query(
            self.sql_scripts.recharge['delete'],
            self.recharge_menu.request_delete_data()
        )

    def update_recharge(self):
        self.db.executemany_query(
            self.sql_scripts.recharge['update'],
            self.recharge_menu.request_update_data()
        )
