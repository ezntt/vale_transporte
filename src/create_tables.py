import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='vale_transporte')

if conn.is_connected():
    db_info = conn.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
else:
    conn.close()
    print("Conexão ao MySQL foi encerrada")
    
cursor = conn.cursor()

tables = {}

file_path = "../ddl/create_tables.sql"

with open(file_path, 'r') as ddl_file:

    statements = ddl_file.read().split(';')

    for statement in statements:
        statement = statement.strip()  # remove blankspaces

        if statement.startswith('CREATE TABLE'):
            table_name = statement.split(' ')[2]  # CREATE[0] TABLE[1] table_name[2]
            tables[table_name] = statement

for table_name in tables:

    statement = tables[table_name]

    try:
        print(f"Criando tabela {table_name}: ", end='')
        cursor.execute(statement)

    except mysql.connector.Error as err:
        print(f"Erro: ", end='')
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Tabela já existe.")
        else:
            print(err.msg)
    else:
        print("OK")
        
conn.commit()

cursor.close()
