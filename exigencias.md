1. Descrição do objetivo geral do sistema (1 parágrafo) (0,5 ponto);

2. Uma descrição detalhada do sistema, visando prover as informações necessárias para a fase de modelagem (1 página) (0,5 ponto);

3. Inclusão da modelagem conceitual (no mínimo 6 entidades) (2,0 pontos);

4. Inclusão da modelagem lógica (1,0 pontos);

5. Inclusão do script DDL obtido a partir do item 4 (0,5 ponto);

6. Inclusão de script DML com cadastro de dados para teste. Os dados não devem conter a palavra testes. 
   Deve-se incluir informações reais e precisas do que está sendo modelado. (0,5 ponto)

7. Elaboração e apresentação de 3 (três) consultas que sumarizem as informações do banco de dados envolvendo mais de duas tabelas. (1,0 pontos)

	7.1. Cada consulta deve projetar pelo menos duas colunas.

	7.2. Duas das consultas devem ter uma das colunas com uma função de agregação.

	7.3. A última consulta deve utilizar um Left ou Right Join.

	7.4. Deve-se, ainda, prover uma descrição do objetivo de cada consulta, assim como uma pequena amostra do resultado,
		 ou seja, um conjunto de linhas recuperadas a partir da consulta;

8. Desenvolvimento de uma aplicação que (4,0 pontos):

	a. Se conecte a um Banco de Dados (PostgreSQL ou MySQL) (0,5 ponto);
	
	b. Faça inserções, atualizações e exclusões no Banco de Dados (2,5 pontos).

		a. Devem existir funcionalidades para cada uma destas operações em cada tabela do modelo considerando as dependências entre as mesmas.

		b. Deve ainda existir um módulo principal que permita demonstrar todas as operações, possibilitando que um banco de dados inicialmente vazio,
		   seja carregado e atualizado utilizando inserts, deletes e updates.

	c. Elabore as consultas definidas no item 7 (1,0 ponto).

	a. Deve existir uma forma de realizar cada consulta que irá apresentar como retorno o resultado do SQL executado no Banco de Dados.