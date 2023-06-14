from datetime import date
import mysql.connector
from mysql.connector import errorcode
from src.View.insert_menu import InsertMenu
from src.View.menu import MenuView

insert_menu = InsertMenu()
menu = MenuView()

conn = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='vale_transporte')

if conn.is_connected():
    db_info = conn.get_server_info()
    MenuView.print_data("Conectado ao servidor MySQL versão " + str(db_info))
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    MenuView.print_data("Conectado ao banco de dados " +  str(linha))
else:
    conn.close()
    MenuView.print_data("Conexão ao MySQL foi encerrada")

insert_employee_dml = (
    "INSERT INTO Funcionario "
    "(nome, data_nascimento, cpf, salario) "
    "VALUES (%s, %s, %s, %s)"
)

insert_user_dml = (
    "INSERT INTO Usuario "
    "(id_linha, nome, data_nascimento, cpf, email, telefone, rua, bairro) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
)


def insert_employeee():
    many_data_employee = InsertMenu.request_employee_data()
    cursor.executemany(insert_employee_dml, many_data_employee)

def insert_user():
    many_data_user = InsertMenu.request_user_data()
    cursor.executemany(insert_user_dml, many_data_user)

while True:
    print("Escolha uma opção:")
    print("1. Adicionar funcionário")
    print("2. Adicionar usuário")
    print("3. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        insert_employeee()
    elif opcao == "2":
        insert_user()
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")

conn.commit()

cursor.close()
conn.close()
