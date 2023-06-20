from src.controller.main_controller import MainController
from src.view.entities.card_view import CardMenu


class CardController(MainController):

    def __init__(self):
        super().__init__()
        self.card_menu = CardMenu()

    def insert_card(self):
        self.db.executemany_query(
            self.sql_crud.card['insert'],
            self.card_menu.request_insert_data()
        )

    def delete_card(self):
        self.db.execute_query(
            self.sql_crud.card['delete'],
            self.card_menu.request_delete_data()
        )

    def update_card(self):
        self.db.executemany_query(
            self.sql_crud.card['update'],
            self.card_menu.request_update_data()
        )

    def show_cards(self):
        result = self.db.execute_query_no_params(
            self.sql_crud.card['list']
        )
        self.view_messages.print_list(result)
