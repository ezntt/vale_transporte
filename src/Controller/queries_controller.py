from src.controller.main_controller import MainController
from src.model.sql_queries import SQLQueries


class QueriesController(MainController):

    def __init__(self):
        super().__init__()
        self.sql_queries = SQLQueries()

    def show_consulta_1(self):
        result = self.db.execute_query_no_params(
            self.sql_queries.consulta_1
        )
        self.view_messages.print_list(result)
    
    def show_consulta_2(self):
        result = self.db.execute_query_no_params(
            self.sql_queries.consulta_2
        )
        self.view_messages.print_list(result)

    def show_consulta_3(self):
        result = self.db.execute_query_no_params(
            self.sql_queries.consulta_3
        )
        self.view_messages.print_list(result)
