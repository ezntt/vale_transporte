import mysql.connector


class DBConnection:
    def __init__(self):
        self.host = "localhost"
        self.database = "vale_transporte"
        self.user = "root"
        self.password = "password"  # agora só precisa alterar aqui a senha
        self.conn = None
        self.cursor = None

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

    def executemany_query(self, query, data):
        self.cursor = self.conn.cursor()
        self.cursor.executemany(query, data)
        self.conn.commit()

    def execute_query(self, query, params=None):
        self.cursor = self.conn.cursor()
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.conn.commit()
