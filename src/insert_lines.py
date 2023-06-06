from datetime import date
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='vale_transporte')

if conn.is_connected():
    db_info = conn.get_server_info()
    print("Conectado ao servidor MySQL versão", db_info)
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados", linha)
else:
    conn.close()
    print("Conexão ao MySQL foi encerrada")

file_path = "../ddl/insert_lines.sql"

with open(file_path, 'r') as ddl_file:

    statements = ddl_file.read().split(';')

    for statement in statements:
        statement = statement.strip()  # remove blankspaces
        
for statement in statements:
    try:
        cursor.execute(statement)
    except mysql.connector.Error as err:
        print(f"Erro: ", end='')
        if err.errno == errorcode.ER_X_DUPLICATE_ENTRY:
            print("Valor já adicionado.")
        else:
            print(err.msg)

conn.commit()

cursor.close()
conn.close()
