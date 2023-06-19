from src.controller.main_controller import MainController
from src.view.card_view import CardMenu


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
        pass

    def update_card(self):
        pass
