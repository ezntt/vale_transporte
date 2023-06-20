from src.controller.main_controller import MainController
from src.view.entities.user_view import UserMenu


class UserController(MainController):

    def __init__(self):
        super().__init__()
        self.user_menu = UserMenu()

    def insert_user(self):
        self.db.executemany_query(
            self.sql_crud.user['insert'],
            self.user_menu.request_insert_data()
        )

    def delete_user(self):
        self.db.execute_query(
            self.sql_crud.user['delete'],
            self.user_menu.request_delete_data()
        )

    def update_user(self):
        self.db.executemany_query(
            self.sql_crud.user['update'],
            self.user_menu.request_update_data()
        )

    def show_users(self):
        result = self.db.execute_query_no_params(
            self.sql_crud.user['list']
        )
        self.view_messages.print_list(result)
