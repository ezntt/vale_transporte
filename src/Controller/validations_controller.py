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

    def is_table_empty(self, table):
        query = self.sql_validations.check_empty_table
        self.db.execute_query(query, (table,))
        is_empty = self.db.cursor.fetchone()
        return is_empty

    # todo: essa porra toda aqui
