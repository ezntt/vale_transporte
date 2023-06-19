from src.controller.main_controller import MainController
from src.view.employee_view import EmployeeMenu


class EmployeeController(MainController):

    def __init__(self):
        super().__init__()
        self.employee_menu = EmployeeMenu()

    def insert_employee(self):
        self.db.executemany_query(
            self.sql_scripts.employee['insert'],
            self.employee_menu.request_insert_data()
        )

    def delete_employee(self):
        pass

    def update_employee(self):
        pass
