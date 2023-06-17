from src.model.db_connection import DBConnection
from src.model.sql_scripts import SQLScripts
from src.view.view_messages import ViewMessages


class ControllerValidations:
    sql_scripts = SQLScripts()
    message = ViewMessages()

    def __init__(self):
        self.cursor = None
        self.db = DBConnection()
        self.conn = self.db.connect()

        # todo: mexer depois nesse código, feito para validações
        # todo: como adicionar um cartão sem ter um usuário cadastrado?
        # todo: verifica se a tabela usuario esta vazia, caso esteja, nao da p cadastrar cartao
        # todo: outras validações podem ser feitas aqui tbm, pensar e ver dai
