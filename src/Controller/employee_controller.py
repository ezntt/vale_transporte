from src.Controller.main_controller import MainController
from src.View.employee_view import EmployeeMenu


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
        self.db.executemany_query(
            self.sql_scripts.employee['delete'],
            self.employee_menu.request_delete_data()
        )

    def update_employee(self):
        self.db.executemany_query(
            self.sql_scripts.employee['update'],
            self.employee_menu.request_update_data()
        )
