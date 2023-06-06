import mysql.connector
from mysql.connector import errorcode

conn = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              database='vale_transporte')

if conn.is_connected():
    db_info = conn.get_server_info()
    print("Conectado ao servidor MySQL versão ",db_info)
    cursor = conn.cursor()
    cursor.execute("select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ",linha)
else:
    conn.close()
    print("Conexão ao MySQL foi encerrada")
    
tables = {}

tables['Usuario'] = (
    "CREATE TABLE `Usuario` ("
    "  `id_usuario` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `id_linha` VARCHAR(3) NOT NULL,"
    "  `nome` VARCHAR(50) NOT NULL,"
    "  `data_nascimento` DATE NOT NULL,"
    "  `cpf` VARCHAR(11) NOT NULL,"
    "  `email` VARCHAR(100),"
    "  `telefone` VARCHAR(11),"
    "  `rua` VARCHAR(100),"
    "  `bairro` VARCHAR(30),"
    "  PRIMARY KEY (`id_usuario`),"
    "  FOREIGN KEY (`id_linha`) REFERENCES Linha(`id_linha`)"
    ") ENGINE=InnoDB")

tables['Cartao'] = (
    "CREATE TABLE `Cartao` ("
    "  `id_cartao` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `id_usuario` INT(11) NOT NULL,"
    "  `saldo` FLOAT(6, 2) NOT NULL,"
    "  `status` TINYINT NOT NULL,"
    "  `validade` DATE,"
    "  `ultima_recarga` DATE,"
    "  PRIMARY KEY (`id_cartao`),"
    "  FOREIGN KEY (`id_usuario`) REFERENCES Usuario(`id_usuario`)"
    ") ENGINE=InnoDB")

tables['Funcionario'] = (
    "CREATE TABLE `Funcionario` ("
    "  `id_funcionario` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `nome` VARCHAR(50) NOT NULL,"
    "  `data_nascimento` DATE NOT NULL,"
    "  `salario` FLOAT(7, 2) NOT NULL,"
    "  `cpf` VARCHAR(11) NOT NULL,"
    "  PRIMARY KEY (`id_funcionario`)"
    ") ENGINE=InnoDB")

tables['Pedido_Recarga'] = (
    "CREATE TABLE `Pedido_Recarga` ("
    "  `id_pedido` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `id_cartao` INT(11) NOT NULL,"
    "  `id_funcionario` INT(11) NOT NULL,"
    "  `valor` FLOAT(6, 2) NOT NULL,"
	"  `data` DATE NOT NULL,"
    "  PRIMARY KEY (`id_pedido`),"
	"  FOREIGN KEY (`id_cartao`) REFERENCES Cartao(`id_cartao`),"
    "  FOREIGN KEY (`id_funcionario`) REFERENCES Funcionario(`id_funcionario`)"
    ") ENGINE=InnoDB")

tables['Catraca'] = (
    "CREATE TABLE `Catraca` ("
    "  `id_catraca` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `id_linha` VARCHAR(3) NOT NULL,"
    "  `preco_tarifa` INT(11) NOT NULL,"
    "  PRIMARY KEY (`id_catraca`),"
    "  FOREIGN KEY (`id_linha`) REFERENCES Linha(`id_linha`)"
    ") ENGINE=InnoDB")

tables['Uso_Do_Cartao'] = (
    "CREATE TABLE `Uso_Do_Cartao` ("
    "  `id_uso_cartao` INT(11) NOT NULL AUTO_INCREMENT,"
    "  `id_catraca` INT(11) NOT NULL,"
    "  `id_cartao` INT(11) NOT NULL,"
    "  `data` DATE NOT NULL,"
    "  `hora` TIME NOT NULL,"
    "  `local` VARCHAR(50) NOT NULL,"
    "  PRIMARY KEY (`id_uso_cartao`),"
    "  FOREIGN KEY (`id_cartao`) REFERENCES Cartao(`id_cartao`),"
    "  FOREIGN KEY (`id_catraca`) REFERENCES Catraca(`id_catraca`)"
    ") ENGINE=InnoDB")

tables['Linha'] = (
    "CREATE TABLE `Linha` ("
    "  `id_linha` VARCHAR(3) NOT NULL,"
    "  `nome` VARCHAR(50) NOT NULL,"
    "  `primeiro_horario` TIME NOT NULL,"
    "  `ultimo_horario` TIME NOT NULL,"
    "  PRIMARY KEY (`id_linha`)"
    ") ENGINE=InnoDB")

cursor = conn.cursor()

for table_name in tables:

    table_description = tables[table_name]

    try:
        print(f"Criando tabela {table_name}: ", end='')
        cursor.execute(table_description)

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
