class SQLQueries:
    def __init__(self):
        pass

    consulta_1 = "select id_funcionario ,f.nome, sum(valor) as total
from funcionario as f
join pedido_recarga
using (id_funcionario)
group by (id_funcionario)
order by total;"

    consulta_2 = "select * from linha"

    consulta_3 = "SELECT u.nome, c.saldo " \
                 "FROM Cartao c " \
                 "RIGHT JOIN usuario u " \
                 "on c.id_usuario = u.id_usuario"
