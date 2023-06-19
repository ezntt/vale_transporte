from src.controller.main_controller import MainController
from src.view.entities.employee_view import EmployeeMenu


class EmployeeController(MainController):

    def __init__(self):
        super().__init__()
        self.employee_menu = EmployeeMenu()

    def insert_employee(self):
        self.db.executemany_query(
            self.sql_crud.employee['insert'],
            self.employee_menu.request_insert_data()
        )

    def delete_employee(self):
        self.db.execute_query(
            self.sql_crud.employee['delete'],
            self.employee_menu.request_delete_data()
        )

    def update_employee(self):
        self.db.executemany_query(
            self.sql_crud.employee['update'],
            self.employee_menu.request_update_data()
        )

    def list_employee(self):
        self.db.executemany_query(
            self.sql_crud.employee['select'],
            self.employee_menu.request_insert_data()
        )

    def show_employees(self):
        result = self.db.execute_query_no_params(
            self.sql_crud.employee['list']
        )
        self.view_messages.print_list(result)
