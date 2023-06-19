class SQLCrud:
    def __init__(self):
        pass

    employee = {
        'insert': (
            "INSERT INTO Funcionario "
            "(nome, data_nascimento, cpf, salario) "
            "VALUES (%s, %s, %s, %s)"
        ),
        'delete': (
            "DELETE FROM Funcionario "
            "WHERE id_funcionario = %s"
        ),
        'update': (
            "UPDATE Funcionario "
            "SET nome = %s, data_nascimento = %s, cpf = %s, salario = %s "
            "WHERE id_funcionario = %s"
        ),
        'select': (
            "SELECT * FROM Funcionario "
            "WHERE id_funcionario = %s"
        )
    }

    user = {
        'insert': (
            "INSERT INTO Usuario "
            "(id_linha, nome, data_nascimento, cpf, email, telefone, bairro) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        ),
        'delete': (
            "DELETE FROM Usuario "
            "WHERE id_usuario = %s"
        ),
        'update': (
            "UPDATE Usuario "
            "SET nome = %s, data_nascimento = %s, cpf = %s, email = %s, telefone = %s, bairro = %s "
            "WHERE id_usuario = %s"
        ),
        'select': (
            "SELECT * FROM Usuario "
            "WHERE id_usuario = %s"
        )
    }

    line = {
        'insert': (
            "INSERT INTO Linha "
            "(id_linha, nome, primeiro_horario, ultimo_horario) "
            "VALUES (%s, %s, %s, %s)"
        ),
        'delete': (
            "DELETE FROM Linha "
            "WHERE id_linha = %s"
        ),
        'update': (
            "UPDATE Linha "
            "SET nome = %s, primeiro_horario = %s, ultimo_horario = %s "
            "WHERE id_linha = %s"
        ),
        'select': (
            "SELECT * FROM Linha "
            "WHERE id_linha = %s"
        )
    }

    card = {
        'insert': (
            "INSERT INTO Cartao "
            "(id_usuario, saldo, status, validade, ultima_recarga) "
            "VALUES (%s, %s, %s, %s, %s)"
        ),
        'delete': (
            "DELETE FROM Cartao "
            "WHERE id_cartao = %s"
        ),
        'update': (
            "UPDATE Cartao "
            "SET id_usuario = %s, saldo = %s, status = %s, validade = %s, ultima_recarga = %s "
            "WHERE id_cartao = %s"
        ),
        'select': (
            "SELECT * FROM Cartao "
            "WHERE id_cartao = %s"
        )
    }

    # todo: utilizar


