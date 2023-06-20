import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="vale_transporte"
)

cursor = conn.cursor()

with open('../sql/all_queries.sql', 'r', encoding='utf-8') as file:
    queries = file.read().split(';')

    for query in queries:
        if query.strip():
            cursor.execute(query)

conn.commit()
cursor.close()
conn.close()
