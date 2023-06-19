from src.controller.main_controller import MainController
from src.view.entities.line_view import LineMenu


class LineController(MainController):

    def __init__(self):
        super().__init__()
        self.line_menu = LineMenu()

    def insert_line(self):
        self.db.executemany_query(
            self.sql_crud.line['insert'],
            self.line_menu.request_insert_data()
        )

    def delete_line(self):
        pass

    def update_line(self):
        pass
