from src.Controller.main_controller import MainController
from src.View.user_view import UserMenu


class UserController(MainController):

    def __init__(self):
        super().__init__()
        self.user_menu = UserMenu()

    def insert_user(self):
        self.db.executemany_query(
            self.sql_scripts.user['insert'],
            self.user_menu.request_insert_data()
        )

    def delete_user(self):
        self.db.executemany_query(
            self.sql_scripts.user['delete'],
            self.user_menu.request_delete_data()
        )

    def update_user(self):
        self.db.executemany_query(
            self.sql_scripts.user['update'],
            self.user_menu.request_update_data()
        )
