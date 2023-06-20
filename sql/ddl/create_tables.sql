CREATE TABLE Linha (
  id_linha VARCHAR(3),
  nome VARCHAR(50),
  primeiro_horario TIME,
  ultimo_horario TIME,
  PRIMARY KEY (id_linha)
) ENGINE=InnoDB;

CREATE TABLE Usuario (
  id_usuario INT(11) AUTO_INCREMENT,
  id_linha VARCHAR(3),
  nome VARCHAR(50),
  data_nascimento DATE,
  cpf VARCHAR(11),
  email VARCHAR(100),
  telefone VARCHAR(11),
  bairro VARCHAR(30),
  PRIMARY KEY (id_usuario),
  FOREIGN KEY (id_linha) REFERENCES Linha(id_linha) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE Catraca (
  id_catraca INT(11) AUTO_INCREMENT,
  id_linha VARCHAR(3),
  preco_tarifa INT(11),
  PRIMARY KEY (id_catraca),
  FOREIGN KEY (id_linha) REFERENCES Linha(id_linha) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Cartao (
  id_cartao INT(11) AUTO_INCREMENT,
  id_usuario INT(11),
  saldo FLOAT(6, 2),
  status TINYINT,
  validade DATE,
  ultima_recarga DATE,
  PRIMARY KEY (id_cartao),
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE Funcionario (
  id_funcionario INT(11) AUTO_INCREMENT,
  nome VARCHAR(50),
  data_nascimento DATE,
  salario FLOAT(7, 2),
  cpf VARCHAR(11),
  PRIMARY KEY (id_funcionario)
) ENGINE=InnoDB;

CREATE TABLE Pedido_Recarga (
  id_pedido INT(11) AUTO_INCREMENT,
  id_cartao INT(11),
  id_funcionario INT(11),
  valor FLOAT(6, 2),
  data DATE,
  PRIMARY KEY (id_pedido),
  FOREIGN KEY (id_cartao) REFERENCES Cartao(id_cartao) ON DELETE SET NULL,
  FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario) ON DELETE SET NULL
) ENGINE=InnoDB;

CREATE TABLE Uso_Do_Cartao (
  id_uso_cartao INT(11) AUTO_INCREMENT,
  id_catraca INT(11),
  id_cartao INT(11),
  data DATE,
  hora TIME,
  PRIMARY KEY (id_uso_cartao),
  FOREIGN KEY (id_cartao) REFERENCES Cartao(id_cartao) ON DELETE SET NULL,
  FOREIGN KEY (id_catraca) REFERENCES Catraca(id_catraca) ON DELETE SET NULL
) ENGINE=InnoDB;