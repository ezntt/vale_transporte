
# CREATE TABLES

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

###
### INSERTS
###

## LINHA

INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('100', 'Madrugadao Centro', '2:00', '4:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('101', 'Centro via Hercilio Luz', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('102', 'Centro via Esteves Junior', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('103', 'Centro via Tenente Silveira', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('104', 'Ticen/Itacorubi', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('131', 'Agronomica via Gama DEca', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('132', 'Agronomica via Gama DEca/Hospital Infantil', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('133', 'Agronomica via Mauro Ramos', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('134', 'Beira-mar Norte', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('135', 'Volta ao Morro Carvoeira Norte', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('136', 'Volta ao Morro Carvoeira Sul', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('137', 'Volta ao Morro Pantanal Norte', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('138', 'Volta ao Morro Pantanal Sul', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('160', 'Morro da Cruz', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('161', 'Morro da Penitenciaria', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('162', 'Saco dos Limoes', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('183', 'Corredor Sudoeste', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('153', 'Costeira do Pirajubae', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('187', 'Corrego Grande via Beira-Mar', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('200', 'Madrugadao Norte', '2:00', '4:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('300', 'Madrugadao Leste', '2:00', '4:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('330', 'Lagoa da Conceicao', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('331', 'Santo Antonio', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('332', 'Santo Antonio via Beira-mar', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('460', 'Porto da Lagoa', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('461', 'Tapera Via Tunel', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('467', 'Tapera Via Saco dos Limoes', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('604', 'Madrugadao Continente', '2:00', '4:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('630', 'Jardim Atlantico', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('761', 'Vila Aparecida', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('762', 'Angelo Laporta', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('763', 'Caieira do Saco dos Limoes', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('764', 'Monte Serrat', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('765', 'Morro da Queimada', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('766', 'Morro do 25', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('767', 'Morro do Horacio via Gama DEca', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('768', 'Morro do Horacio via Mauro Ramos', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('769', 'Morro Nova Trento', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('772', 'Chico Mendes', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('231', 'Canasvieiras via Mauro Ramos', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('233', 'Canasvieiras/Trindade', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('120', 'Agronomica Semidireto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('121', 'Mauro Ramos Semidireto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('150', 'Unica Semidireto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('151', 'Centro Administrativo SC Semidireto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('184', 'UDESC Semidireto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('185', 'UFSC Semidireto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('221', 'Canasvieiras Via Mauro Ramos', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('320', 'Lagoa da Conceicao Semidireto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('110', 'Ticen-Titri Direto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('210', 'Canasvieiras Direto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('212', 'Santo Antonio Direto', '6:00', '22:00');

## FUNCIONARIO

INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('100', 'Emílio Quintana de Rodrigues', '2001-10-12', '1441.00', '26528195188');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('101', 'Christian Cordeiro', '1984-05-25', '1641.0', '25477872616');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('102', 'Sofia Camacho Matias', '1977-12-10', '1641.10', '75004509409');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('103', 'Adriano Emanoel Dias Rico', '1952-02-15', '1241.01', '14257129247');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('104', 'Érica Franco Perez', '1982-04-21', '1421.20', '43590385340');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('105', 'Beatriz Keyla de Campos', '1990-12-29', '1754.90', '54065169305');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('106', 'Marciane Renata Chaves do Amazonas', '1967-09-11', '2970.54', '54354314681');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('107', 'Nicolas Tomáz Dominato', '1955-10-28', '2270.54', '16913466404');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('108', 'Camilo Vicente Correia Galvão Moreno', '1987-06-29', '983.34', '86203948276');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('109', 'Kiara Aragão', '1934-02-18', '11243.11', '38747814535');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('110', 'Estêvão Beltrão de Muniz', '1976-09-12', '6835.83', '70301721246');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('111', 'Regina Gislaine Beltrão Soto', '2002-09-12', '1534.12', '42569313840');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('112', 'Catarina Samara Duarte de Albuquerque', '1957-03-06', '1325.20', '92260332340');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('113', 'Emílio Ávila da Cunha', '2003-07-05', '5346.87', '08236456900');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('114', 'Táles Wagner Chaves', '1986-02-20', '2376.21', '51513684272');
INSERT INTO Funcionario (id_funcionario, nome, data_nascimento, salario, cpf)
VALUES ('115', 'Rebeca Faro', '1973-01-18', '1278.23', '47665326439');

#
# USUARIO
#