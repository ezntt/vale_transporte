from src.Controller.main_controller import MainController
from src.View.line_view import LineMenu


class LineController(MainController):

    def __init__(self):
        super().__init__()
        self.line_menu = LineMenu()

    def insert_line(self):
        self.db.executemany_query(
            self.sql_scripts.line['insert'],
            self.line_menu.request_insert_data()
        )

    def delete_line(self):
        pass

    def update_line(self):
        pass
