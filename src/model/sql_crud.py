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
        ),
        'list': (
            "SELECT id_funcionario, nome FROM funcionario"
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
            "SET id_linha = %s,  nome = %s, data_nascimento = %s, cpf = %s, email = %s, telefone = %s, bairro = %s "
            "WHERE id_usuario = %s"
        ),
        'select': (
            "SELECT * FROM Usuario "
            "WHERE id_usuario = %s"
        ),
        'list': (
            "SELECT id_usuario, nome FROM Usuario"
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
        ),
        'list': (
            "SELECT id_linha, nome, primeiro_horario, ultimo_horario FROM Linha"
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
        ),
        'list': (
            "SELECT c.id_cartao, c.saldo, u.nome "
            "FROM Cartao c "
            "LEFT JOIN Usuario u "  # mostra cartões sem usuário vinculado com o left join
            "ON u.id_usuario = c.id_usuario"
        )
    }

    gate = {
        'insert': (
            "INSERT INTO Catraca "
            "(id_linha, preco_tarifa) "
            "VALUES (%s, %s)"
        ),
        'delete': (
            "DELETE FROM Catraca "
            "WHERE id_catraca = %s"
        ),
        'update': (
            "UPDATE Catraca "
            "SET id_catraca = %s, id_linha = %s, preco_tarifa = %s "
            "WHERE id_catraca = %s"
        ),
        'select': (
            "SELECT * FROM Catraca "
            "WHERE id_catraca = %s"
        ),
        'list': (
            "SELECT id_catraca, preco_tarifa FROM catraca"
        )
    }

    recharge = {
        'insert': (
            "INSERT INTO Pedido_recarga "
            "(id_cartao, id_funcionario, valor, data) "
            "VALUES (%s, %s, %s, %s)"
        ),
        'delete': (
            "DELETE FROM Pedido_recarga "
            "WHERE id_pedido = %s"
        ),
        'update': (
            "UPDATE Pedido_recarga "
            "SET id_cartao = %s, id_funcionario = %s, valor = %s, data = %s "
            "WHERE id_pedido = %s"
        ),
        'select': (
            "SELECT * FROM Pedido_recarga "
            "WHERE id_pedido = %s"
        ),
        'list': (
            "SELECT id_pedido, valor, data FROM pedido_recarga"
        )
    }

    card_use = {
        'insert': (
            "INSERT INTO uso_do_cartao"
            "(id_catraca, id_cartao, data, hora) "
            "VALUES (%s, %s, %s, %s)"
        ),
        'delete': (
            "DELETE FROM uso_do_cartao "
            "WHERE id_uso_cartao = %s"
        ),
        'update': (
            "UPDATE uso_do_cartao "
            "SET id_catraca = %s, id_cartao = %s, data = %s, hora = %s "
            "WHERE id_uso_cartao = %s"
        ),
        'select': (
            "SELECT * FROM uso_do_cartao "
            "WHERE id_uso_cartao = %s"
        ),
        'list': (
            "SELECT id_uso_cartao, data, hora FROM uso_do_cartao"
        )
    }
