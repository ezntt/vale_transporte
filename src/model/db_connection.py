import mysql.connector


class DBConnection:
    def __init__(self):
        self.host = "localhost"
        self.database = "vale_transporte"
        self.user = "root"
        self.password = "password"
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(user=self.user,
                                                password=self.password,
                                                host=self.host,
                                                database=self.database)
            return self.conn
        except mysql.connector.Error as e:
            print("Erro ao conectar ao banco de dados:", e)

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print("Conexão fechada.")
