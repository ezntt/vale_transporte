from src.controller.main_controller import MainController
from src.model.sql_crud import SQLCrud
from src.view.entities.line_view import LineMenu


class LineController(MainController):

    def __init__(self):
        super().__init__()
        self.line_menu = LineMenu()
        self.sql_crud = SQLCrud()

    def insert_line(self):
        self.db.executemany_query(
            self.sql_crud.line['insert'],
            self.line_menu.request_insert_data()
        )

    def delete_line(self):
        self.db.executemany_query(
            self.sql_crud.line['delete'],
            self.line_menu.request_delete_data()
        )

    def update_line(self):
        self.db.executemany_query(
            self.sql_crud.line['update'],
            self.line_menu.request_update_data()
        )
