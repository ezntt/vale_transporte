from src.controller.main_controller import MainController
from src.view.entities.card_use_view import CardUseMenu


class CardUseController(MainController):

    def __init__(self):
        super().__init__()
        self.card_use_menu = CardUseMenu()

    def insert_card_use(self):
        self.db.executemany_query(
            self.sql_crud.card_use['insert'],
            self.card_use_menu.request_insert_data()
        )

    def delete_card_use(self):
        self.db.execute_query(
            self.sql_crud.card_use['delete'],
            self.card_use_menu.request_delete_data()
        )

    def update_card_use(self):
        self.db.executemany_query(
            self.sql_crud.card_use['update'],
            self.card_use_menu.request_update_data()
        )

    def show_card_use(self):
        result = self.db.execute_query_no_params(
            self.sql_crud.card_use['list']
        )
        self.view_messages.print_list(result)
