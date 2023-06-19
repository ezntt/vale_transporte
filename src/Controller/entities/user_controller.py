from src.controller.main_controller import MainController
from src.model.sql_crud import SQLCrud
from src.view.entities.user_view import UserMenu


class UserController(MainController):

    def __init__(self):
        super().__init__()
        self.user_menu = UserMenu()
        self.sql_crud = SQLCrud()


    def insert_user(self):
        self.db.executemany_query(
            self.sql_crud.user['insert'],
            self.user_menu.request_insert_data()
        )

    def delete_user(self):
        self.db.executemany_query(
            self.sql_crud.user['delete'],
            self.user_menu.request_delete_data()
        )

    def update_user(self):
        self.db.executemany_query(
            self.sql_crud.user['update'],
            self.user_menu.request_update_data()
        )
