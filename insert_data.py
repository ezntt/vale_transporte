from datetime import date
import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='nero349_!A',
                               host='localhost',
                               database='vale_transporte')

if conn.is_connected():
    db_info = conn.get_server_info()
    print("Conectado ao servidor MySQL versão ", db_info)
    cursor = conn.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)
else:
    conn.close()
    print("Conexão ao MySQL foi encerrada")

insert_employee = (
    "INSERT INTO Funcionario "
    "(nome, data_nascimento, cpf, salario) "
    "VALUES (%s, %s, %s, %s)"
)

num_employees = int(input("Quantos funcionários deseja adicionar? "))

many_data_employee = []
for x in range(num_employees):
    nome = input("Digite o nome do funcionário: ")
    ano = int(input("Digite o ano de nascimento do funcionário: "))

    while True:
        try:
            mes = int(input("Digite o mês de nascimento do funcionário: "))
            if mes < 1 or mes > 12:
                raise ValueError("Mês inválido. Digite um valor entre 1 e 12.")
            dia = int(input("Digite o dia de nascimento do funcionário: "))
            if dia < 1 or dia > 31:
                raise ValueError("Dia inválido. Digite um valor entre 1 e 31.")

            data_nascimento = date(ano, mes, dia)
            break
        except ValueError as e:
            print("Erro:", e)

    cpf = input("Digite o CPF do funcionário: ")

    while True:
        try:
            salario = float(input("Digite o salário do funcionário: "))
            break
        except ValueError:
            print("Salário inválido. Digite um valor numérico.")

    data_nascimento = date(ano, mes, dia)
    many_data_employee.append((nome, data_nascimento, cpf, salario))

cursor.executemany(insert_employee, many_data_employee)

conn.commit()

cursor.close()