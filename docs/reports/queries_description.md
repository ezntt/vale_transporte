## Descrição das consultas feitas na aplicação

Os *scripts* DML das consultas podem ser encontrados no arquivo `src/model/sql_queries.py`

### Consultas

#### Funcionários que mais fizeram recargas
Esta consulta tem como objetivo apresentar os funcionários que mais deram retorno financeiro para a empresa,
criando uma tabela em que, em ordem descrescente, apresente o nome dos funcionários e ao lado o quanto que eles já
recarregaram em cartões em dinheiro

**Script:**
```MySQL
SELECT 
    f.id_funcionario,
    f.nome,
    sum(valor) as total
FROM funcionario f
INNER JOIN pedido_recarga pr
    ON f.id_funcionario = pr.id_funcionario
GROUP BY f.id_funcionario
ORDER BY total DESC;
```

**Resultado:**

![first_query_results_table.png](img/first_query_results_table.png)


#### Linhas Mais Utilizadas
Esta consulta tem como objetivo localizar qual linha esta sendo mais utilizada para assim poder localizar
a necessidade de maior circulacao de onibus ou ampliacao dos pontos oferecidos

**Script:**
```MySQL
SELECT 
    l.id_linha,
    l.nome,
    COUNT(u.id_uso_cartao) AS total_utilizacoes 
FROM linha l 
JOIN catraca c
    ON l.id_linha = c.id_linha
JOIN uso_do_cartao u 
    ON c.id_catraca = u.id_catraca
GROUP BY l.id_linha, l.nome 
ORDER BY total_utilizacoes DESC;
```

**Resultado:**

![second_query_results_table.png](img/second_query_results_table.png)

#### Todos Os Usuario e seus saldos
Esta consulta tem como objetivo visualizar todos os usuarios cadastrados no sistemas 
incluindo aqueles que ainda nao possuem um cartao e mostrar o seu saldo
**Script:**
```MySQL
SELECT 
    u.nome,
    c.saldo
FROM Cartao c
RIGHT JOIN usuario u
    ON c.id_usuario = u.id_usuario;
```

**Resultado:**

![third_query_results_table.png](img%2Fthird_query_results_table.png)