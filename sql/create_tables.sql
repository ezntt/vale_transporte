CREATE TABLE Linha (
  id_linha VARCHAR(3) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  primeiro_horario TIME NOT NULL,
  ultimo_horario TIME NOT NULL,
  PRIMARY KEY (id_linha)
) ENGINE=InnoDB;

CREATE TABLE Usuario (
  id_usuario INT(11) NOT NULL AUTO_INCREMENT,
  id_linha VARCHAR(3) NOT NULL,
  nome VARCHAR(50) NOT NULL,
  data_nascimento DATE NOT NULL,
  cpf VARCHAR(11) NOT NULL,
  email VARCHAR(100),
  telefone VARCHAR(11),
  bairro VARCHAR(30),
  PRIMARY KEY (id_usuario),
  FOREIGN KEY (id_linha) REFERENCES Linha(id_linha)
) ENGINE=InnoDB;

CREATE TABLE Catraca (
  id_catraca INT(11) NOT NULL AUTO_INCREMENT,
  id_linha VARCHAR(3) NOT NULL,
  preco_tarifa INT(11) NOT NULL,
  PRIMARY KEY (id_catraca),
  FOREIGN KEY (id_linha) REFERENCES Linha(id_linha)
) ENGINE=InnoDB;

CREATE TABLE Cartao (
  id_cartao INT(11) NOT NULL AUTO_INCREMENT,
  id_usuario INT(11) NOT NULL,
  saldo FLOAT(6, 2) NOT NULL,
  status TINYINT NOT NULL,
  validade DATE,
  ultima_recarga DATE,
  PRIMARY KEY (id_cartao),
  FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
) ENGINE=InnoDB;

CREATE TABLE Funcionario (
  id_funcionario INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  data_nascimento DATE NOT NULL,
  salario FLOAT(7, 2) NOT NULL,
  cpf VARCHAR(11) NOT NULL,
  PRIMARY KEY (id_funcionario)
) ENGINE=InnoDB;

CREATE TABLE Pedido_Recarga (
  id_pedido INT(11) NOT NULL AUTO_INCREMENT,
  id_cartao INT(11) NOT NULL,
  id_funcionario INT(11) NOT NULL,
  valor FLOAT(6, 2) NOT NULL,
  data DATE NOT NULL,
  PRIMARY KEY (id_pedido),
  FOREIGN KEY (id_cartao) REFERENCES Cartao(id_cartao),
  FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
) ENGINE=InnoDB;

CREATE TABLE Uso_Do_Cartao (
  id_uso_cartao INT(11) NOT NULL AUTO_INCREMENT,
  id_catraca INT(11) NOT NULL,
  id_cartao INT(11) NOT NULL,
  data DATE NOT NULL,
  hora TIME NOT NULL,
  PRIMARY KEY (id_uso_cartao),
  FOREIGN KEY (id_cartao) REFERENCES Cartao(id_cartao),
  FOREIGN KEY (id_catraca) REFERENCES Catraca(id_catraca)
) ENGINE=InnoDB;