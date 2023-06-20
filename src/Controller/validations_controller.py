from src.model.db_connection import DBConnection
from src.model.sql_crud import SQLCrud
from src.model.sql_validations import SQLValidations
from src.view.messages_view import ViewMessages


class ValidationsController:

    def __init__(self):
        self.cursor = None
        self.db = DBConnection()
        self.conn = self.db.connect()
        self.sql_crud = SQLCrud()
        self.sql_validations = SQLValidations()
        self.message = ViewMessages()

    def validate_line_id(self, line_id):
        query = self.sql_crud.line['select']
        self.db.execute_query(query, (line_id,))
        row = self.db.cursor.fetchone()
        if row is None:
            return False
        else:
            return True

    #todo
    def is_table_empty(self, table):
        return True
        # query = self.sql_validations.check_empty_table
        # self.db.execute_query(query, [table])
        # count = self.db.cursor.fetchone()[0]
        # is_empty = (count == 0)
        # self.db.cursor.close()
        # return is_empty
