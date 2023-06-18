- ~~Descrição do objetivo geral do sistema (1 parágrafo)~~ (0,5 ponto);

- ~~Uma descrição detalhada do sistema, visando prover as informações necessárias para a fase de modelagem (1 página)~~ (0,5 ponto);

- ~~Inclusão da modelagem conceitual (no mínimo 6 entidades)~~ (2,0 pontos);

- ~~Inclusão da modelagem lógica~~ (1,0 pontos);

- ~~Inclusão do script DDL obtido a partir do item 4~~ (0,5 ponto);

- ~~Inclusão de script DML com cadastro de dados para teste. Os dados não devem conter a palavra testes.
   Deve-se incluir informações reais e precisas do que está sendo modelado.~~ (0,5 ponto)
	- ~~DML de Linha~~
	- ~~DML de Usuario~~
	- ~~DML de Funcionario~~
	- ~~DML de Catraca~~
	- ~~DML de Uso_Do_Cartao~~
	- ~~DML de Pedido_Recarga~~

- Elaboração e apresentação de 3 (três) consultas que sumarizem as informações do banco de dados envolvendo mais de duas tabelas. (1,0 pontos)
	- Cada consulta deve projetar pelo menos duas colunas.

	- Duas das consultas devem ter uma das colunas com uma função de agregação.

	- A última consulta deve utilizar um Left ou Right Join.

	- Deve-se, ainda, prover uma descrição do objetivo de cada consulta, assim como uma pequena amostra do resultado,
		 ou seja, um conjunto de linhas recuperadas a partir da consulta;
		 
- Desenvolvimento de uma aplicação que (4,0 pontos):

	- ~~Se conecte a um Banco de Dados (PostgreSQL ou MySQL) (0,5 ponto);~~
	
	- Faça inserções, atualizações e exclusões no Banco de Dados (2,5 pontos).

		- Devem existir funcionalidades para cada uma destas operações em cada tabela do modelo considerando as dependências entre as mesmas.

		- Deve ainda existir um módulo principal que permita demonstrar todas as operações, possibilitando que um banco de dados inicialmente vazio,
		   seja carregado e atualizado utilizando inserts, deletes e updates.

	- Elabore as consultas definidas no item 7 (1,0 ponto).

		- Deve existir uma forma de realizar cada consulta que irá apresentar como retorno o resultado do SQL executado no Banco de Dados.