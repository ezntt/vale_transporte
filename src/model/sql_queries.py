class SQLQueries:
    def __init__(self):
        pass

    consulta_1 = "SELECT f.id_funcionario, f.nome, sum(valor) as total " \
                 "FROM funcionario f " \
                 "INNER JOIN pedido_recarga pr " \
                 "ON f.id_funcionario = pr.id_funcionario " \
                 "GROUP BY f.id_funcionario " \
                 "ORDER BY total DESC "

    consulta_2 = "SELECT l.id_linha, l.nome, COUNT(u.id_uso_cartao) AS total_utilizacoes " \
                 "FROM linha l " \
                 "JOIN catraca c " \
                 "ON l.id_linha = c.id_linha " \
                 "JOIN uso_do_cartao u " \
                 "ON c.id_catraca = u.id_catraca " \
                 "GROUP BY l.id_linha, l.nome " \
                 "ORDER BY total_utilizacoes DESC;"

    consulta_3 = "SELECT u.nome, c.saldo " \
                 "FROM Cartao c " \
                 "RIGHT JOIN usuario u " \
                 "ON c.id_usuario = u.id_usuario"

