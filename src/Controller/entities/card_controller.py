from src.controller.main_controller import MainController
from src.model.sql_crud import SQLCrud
from src.view.entities.card_view import CardMenu


class CardController(MainController):

    def __init__(self):
        super().__init__()
        self.card_menu = CardMenu()
        self.sql_crud = SQLCrud()

    def insert_card(self):
        self.db.executemany_query(
            self.sql_crud.card['insert'],
            self.card_menu.request_insert_data()
        )

    def delete_card(self):

        self.db.executemany_query(
            self.sql_crud.card['delete'],
            self.card_menu.request_delete_data()
        )

    def update_card(self):
        self.db.executemany_query(
            self.sql_crud.card['update'],
            self.card_menu.request_update_data()
        )
