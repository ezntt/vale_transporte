from src.controller.main_controller import MainController
from src.view.entities.recharge_view import RechargeMenu


class RechargeController(MainController):

    def __init__(self):
        super().__init__()
        self.recharge_menu = RechargeMenu()

    def insert_recharge(self):
        self.db.executemany_query(
            self.sql_crud.recharge['insert'],
            self.recharge_menu.request_insert_data()
        )

    def delete_recharge(self):
        self.db.execute_query(
            self.sql_crud.recharge['delete'],
            self.recharge_menu.request_delete_data()
        )

    def update_recharge(self):
        self.db.executemany_query(
            self.sql_crud.recharge['update'],
            self.recharge_menu.request_update_data()
        )

    def show_recharges(self):
        result = self.db.execute_query_no_params(
            self.sql_crud.recharge['list']
        )
        self.view_messages.print_list(result)
