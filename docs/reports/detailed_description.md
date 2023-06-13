# Descrição detalhada do sistema de vale-transporte
```
Alunos: Eduardo Zanetta (20203087)
        Pedro Matiucci (20204505)
        
Professor: Vinícius Ramos
Disciplina: Banco de Dados I (INE5613)
```
## Introdução
Este documento fornece uma descrição detalhada do sistema de vale-transporte, com o propósito de oferecer as informações necessárias para a fase de modelagem.

O sistema permite que os usuários recarreguem seus cartões por meio da assistência de um funcionário, registrando as transações como `Pedido_Recarga`. Os cartões recarregados podem ser utilizados nas catracas dos ônibus, gerando *logs* armazenados em `Uso_Do_Cartao`.

## Entidades e Relacionamentos
O sistema é composto por diversas entidades principais: `Usuario`, `Cartao`, `Funcionario`, `Pedido_Recarga`, `Catraca`, `Uso_Do_Cartao` e `Linha`. A seguir, serão apresentados os relacionamentos entre essas entidades:

#### Relacionamento entre Usuario e Cartao:
- Cada usuário está vinculado a apenas um cartão.
- A tabela "`Cartao`" possui o campo "`id_usuario`" como chave estrangeira para associar o cartão a um usuário.

#### Relacionamento entre `Cartao` e `Pedido_Recarga`:
- Um cartão pode ter várias recargas registradas a ele mesmo.
- A tabela "`Pedido_Recarga`" possui o campo "`id_cartao`" como chave estrangeira para identificar a qual cartão cada recarga pertence.

#### Relacionamento entre `Pedido_Recarga`, `Cartao` e `Funcionario`:    
- Vários pedidos de recarga podem estar associados a um único funcionário e a um único cartão.
- A tabela "`Pedido_Recarga`" possui os campos "`id_cartao`" e "`id_funcionario`" como chaves estranegiras para estabelecer essa associação.

#### Relacionamento entre `Catraca` e `Uso_Do_Cartao`:
- Uma catraca pode registrar vários usos do cartão.
- A tabela "`Uso_Do_Cartao`" possui o campo "`id_catraca`" para identificar a catraca utilizada em cada registro.

#### Relacionamento entre `Uso_Do_Cartao`, `Catraca` e `Cartao`:
- Vários usos do cartão podem estar associados a uma única catraca e a um único cartão.
 - A tabela "`Uso_Do_Cartao`" possui os campos "`id_catraca`" e "`id_cartao`" como chaves estrangeiras para estabelecer essa associação.

## Limitações:
O sistema apresenta algumas limitações que devem ser consideradas:

#### Restrição de utilização por linha cadastrada:
- Um usuário só pode utilizar seu cartão nas catracas das linhas de ônibus cadastradas.
- Essa restrição é definida pelo campo "`id_linha`" presente nas tabelas "`Usuario`" e "`Catraca`".

#### Vínculo obrigatório entre cartão e usuário:
- Cada cartão deve estar vinculado a um usuário específico.
- Essa associação é realizada por meio do campo "`id_usuario`" presente na tabela "`Cartao`".

#### Restrição de um único cartão por usuário:
- Um usuário só pode ter um único cartão vinculado a ele.
- Essa restrição é estabelecida pela relação de um para um entre as tabelas "`Usuario`" e "`Cartao`".

#### Restrição de recarga por funcionário:
- A recarga de um cartão só pode ser realizada por um funcionário.
- Essa associação é estabelecida pelo campo "`id_funcionario`" presente na tabela "`Pedido_Recarga`".

#### Vínculo exclusivo entre catraca e linha:
- Uma catraca só pode estar vinculada a uma única linha de ônibus.
- Essa associação é realizada pelo campo "`id_linha`" presente na tabela "`Catraca`".