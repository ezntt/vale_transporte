from src.Controller.main_controller import MainController
from src.View.card_view import CardMenu


class CardController(MainController):

    def __init__(self):
        super().__init__()
        self.card_menu = CardMenu()

    def insert_card(self):
        self.db.executemany_query(
            self.sql_scripts.card['insert'],
            self.card_menu.request_insert_data()
        )

    def delete_card(self):

        self.db.executemany_query(
            self.sql_scripts.card['delete'],
            self.card_menu.request_delete_data()
        )

    def update_card(self):
        self.db.executemany_query(
            self.sql_scripts.card['update'],
            self.card_menu.request_update_data()
        )