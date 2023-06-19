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

####
####    INSERTIONS
####

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
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('310', 'Santo Antonio Direto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('311', 'Lagoa da Conceicao Direto', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('250', 'Canasvieiras/Daniela via Forte', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('260', 'Cachoeira do Bom Jesus', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('261', 'Capivari (via Graciliano Gomes)', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('262', 'Circular Canasvieiras', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('263', 'Gaivotas', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('264', 'Ingleses', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('265', 'Ponta das Canas', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('266', 'Praia Brava', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('267', 'Rio Vermelho', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('268', 'Sitio de Baixo', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('269', 'Travessao', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('270', 'Vargem Grande', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('274', 'Rio Vermelho Via Muquem', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('275', 'Capivari (via Joao Gualberto Soares)', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('276', 'Balneario Canasvieiras', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('277', 'Balneario Ingleses', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('281', 'Costa do Mocambique', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('283', 'Vargem do Bom Jesus', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('842', 'Canasvieiras/Lagoa', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('940', 'Canasvieiras/ S. Antonio via Jurere', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('941', 'Canasvieiras/ S. Antonio via Ratones', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('840', 'Canasvieiras via Lagoa da Conceicao', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('294', 'Interpraias (Inicio: Santinho - Final: Forte)', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('230', 'Canasvieiras via Gama DEca', '6:00', '22:00');
INSERT INTO Linha (id_linha, nome, primeiro_horario, ultimo_horario)
VALUES ('211', 'Canasvieiras/Trindade - Direto', '6:00', '22:00');

## CATRACAS

INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('600', '100', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('601', '101', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('602', '102', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('603', '103', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('604', '104', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('605', '131', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('606', '132', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('607', '133', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('608', '134', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('609', '135', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('610', '136', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('611', '137', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('612', '138', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('614', '160', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('615', '161', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('616', '162', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('617', '183', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('618', '184', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('619', '185', '5.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('620', '153', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('621', '161', '5.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('622', '162', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('623', '200', '4.50');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('624', '183', '5.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('625', '187', '5.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('626', '331', '5.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('627', '332', '5.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('628', '460', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('629', '461', '6.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('630', '762', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('631', '763', '4.00');
INSERT INTO Catraca (id_catraca, id_linha, preco_tarifa)
VALUES ('632', '764', '4.50');

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

## USUARIO

INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('400', '100', 'Gian Benites', '1997-01-30', '46003403020','Gianbenites@gmail.com', '88521-2095' ,'Centro');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('401', '183', 'Adriano Albano', '1942-07-18', '42280728010','Adrianoalbano1@gmail.com', '81768-9819' ,'Campeche');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('402', '134', 'Ivana Mia Cruz', '1974-05-21', '35449850042','ivanamia@gmail.com', '42368-1441' ,'Centro');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('403', '200', 'Joel Ronaldo', '1962-04-06', '70345207041','joelronaldo@gmail.com', '82196-0729' ,'Daniela');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('404', '300', 'Oliver Galhardo Neto', '1984-10-07', '92494999065','olivergalhardo@gmail.com', '79135-4787' ,'Itacorubi');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('405', '461', 'Ricardo Paes', '1967-03-20', '72333579005','ricardopaes23@gmail.com', '52287-7102' ,'Centro');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('406', '467', 'Alex ávila Neto', '1984-04-23', '28398818026','alexavila@gmail.com', '53716-1032' ,'Saco dos Limoes');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('407', '604', 'Bóris Lira Filho', '1989-08-29', '85610830001','borislira12@gmail.com', '71717-8007' ,'Coqueiros');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('408', '630', 'Bóris Sílvio Dominato', '1960-02-06', '93307089005','borissil@gmail.com', '10027-9357' ,'Sambaqui');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('409', '762', 'Rafael Mário Gusmão', '1980-01-27', '83727808039','rafaelmario2@gmail.com', '62154-7198' ,'Trindade');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('410', '763', 'Jeferson Leopoldo', '1966-10-18', '74336627070','jeferson12@gmail.com', '34318-7289' ,'Saco dos Limoes');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('411', '767', 'Madalena Tatiane', '2004-04-30', '22916983031','madalenatati@gmail.com', '33963-6521' ,'Morro das pedras');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('412', '772', 'Ângelo Camilo Neto', '2003-06-28', '89816313014','angelocamilo@gmail.com', '69663-4641' ,'Jardim atlantico');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('413', '231', 'Sophie Priscila de Ferraz', '1962-09-29', '52184220027','Sophiepri@gmail.com', '18797-0863' ,'Bom abrigo');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('414', '151', 'Ian Matos de Roque', '1986-10-15', '22287116087','IanMatos@gmail.com', '50634-5125' ,'Agronomica');
INSERT INTO Usuario (id_usuario, id_linha, nome, data_nascimento, cpf, email, telefone, bairro)
VALUES ('415', '184', 'Anderson Demilson', '1967-07-24', '60286581035','Andersondemilson@gmail.com', '15068-1275' ,'Carvoeira');

## CARTAO

INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('400', '200', '32.00', '1', '2024-01-16', '2023-06-16');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('401','201', '63.00', '0', '2022-01-01', '2021-12-25');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('402','202', '00.00', '0', '2021-11-14', '2021-09-17');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('403','203', '12.50', '1', '2024-05-14', '2022-03-11');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('404','204', '2.30', '1', '2023-11-22', '2022-08-31');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('405','205', '17.20', '0', '2020-02-15', '2020-02-14');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('406','206', '92.10', '1', '2025-05-11', '2022-11-25');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('407','207', '36.00', '1', '2024-12-27', '2022-09-30');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('408','208', '4.00', '1', '2025-03-01', '2022-09-02');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('409','209', '16.03', '1', '2024-04-13', '2023-04-13');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('410','210', '17.24', '1', '2024-05-14', '2023-05-14');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('411','211', '37.42', '1', '2025-09-25', '2022-09-11');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('412','212', '22.17', '1', '2025-01-23', '2023-03-04');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('413','213', '17.22', '1', '2025-08-29', '2022-12-04');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('414','214', '13.20', '1', '2023-07-28', '2023-06-07');
INSERT INTO Cartao (id_usuario, id_cartao, saldo, status, Validade, ultima_recarga)
VALUES ('415','215', '19.35', '1', '2025-03-19', '2023-01-06');

## PEDIDO DE RECARGA

INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('100', '200', '100', '20.00', '2023-06-16');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('101', '200', '105', '20.00', '2023-05-16');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('102', '200', '106', '15.00', '2023-04-11');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('103', '200', '100', '03.50', '2023-03-06');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('104', '200', '110', '22.75', '2023-03-26');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('105', '201', '111', '22.75', '2021-12-25');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('106', '201', '111', '67.75', '2021-12-20');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('107', '201', '112', '12.75', '2021-10-05');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('108', '201', '100', '2.75', '2021-09-03');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('109', '202', '115', '2.75', '2021-09-17');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('110', '202', '114', '12.50', '2021-08-03');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('111', '202', '103', '122.75', '2021-07-13');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('112', '202', '102', '10.00', '2021-03-27');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('113', '203', '105', '255.50', '2022-03-11');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('114', '204', '106', '15.50', '2022-08-31');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('115', '204', '114', '5.50', '2022-08-15');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('116', '204', '102', '50.20', '2022-04-05');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('117', '205', '106', '32.20', '2020-02-14');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('118', '206', '104', '9.20', '2022-11-25');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('119', '206', '104', '29.20', '2022-11-01');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('120', '207', '100', '129.20', '2022-09-30');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('121', '208', '115', '27.20', '2022-09-02');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('122', '208', '104', '37.40', '2022-08-01');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('123', '208', '111', '19.70', '2022-07-13');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('124', '209', '101', '13.70', '2023-03-03');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('125', '209', '105', '26.60', '2023-02-12');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('126', '209', '106', '15.20', '2023-01-22');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('127', '209', '109', '25.00', '2022-12-25');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('128', '210', '102', '25.00', '2023-05-14');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('129', '210', '107', '33.30', '2023-03-20');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('130', '211', '101', '23.30', '2022-09-11');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('131', '211', '112', '22.10', '2022-07-26');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('132', '212', '101', '12.10', '2023-03-04');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('133', '212', '107', '28.20', '2023-02-18');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('134', '212', '110', '9.50', '2023-01-25');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('135', '213', '100', '19.20', '2022-12-04');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('136', '213', '100', '5.50', '2022-10-22');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('137', '214', '111', '12.80', '2023-06-07');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('138', '214', '115', '56.50', '2023-03-28');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('139', '215', '100', '6.50', '2023-01-06');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('140', '215', '109', '16.00', '2022-11-16');
INSERT INTO Pedido_recarga (id_pedido, id_cartao, id_funcionario, valor, data)
VALUES ('141', '215', '105', '28.90', '2023-09-02');


## USO DO CARTAO

INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('100', '600', '200', '2023-06-17', '6:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('101', '600', '200', '2023-06-17', '18:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('102', '600', '200', '2023-04-17', '6:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('103', '600', '200', '2023-04-17', '18:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('104', '600', '200', '2023-04-14', '6:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('105', '600', '200', '2023-04-13', '18:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('106', '601', '203', '2022-09-13', '18:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('107', '601', '203', '2022-09-13', '6:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('108', '601', '209', '2022-09-13', '8:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('109', '601', '212', '2022-09-13', '12:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('110', '601', '203', '2022-09-13', '12:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('111', '601', '201', '2022-09-13', '8:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('112', '601', '209', '2022-09-13', '18:00');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('113', '601', '200', '2022-09-13', '13:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('114', '602', '215', '2022-08-12', '13:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('115', '602', '214', '2022-08-15', '18:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('116', '602', '215', '2022-08-14', '11:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('117', '603', '215', '2022-08-14', '11:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('118', '603', '212', '2022-07-10', '13:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('119', '605', '201', '2021-01-10', '19:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('120', '605', '202', '2021-01-10', '15:45');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('121', '606', '203', '2022-11-10', '14:50');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('122', '606', '204', '2021-01-13', '14:20');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('123', '606', '205', '2021-01-22', '16:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('124', '607', '209', '2023-03-22', '6:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('125', '607', '208', '2021-03-22', '17:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('126', '607', '211', '2021-01-26', '12:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('127', '608', '211', '2023-04-26', '9:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('128', '609', '213', '2023-02-19', '9:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('129', '609', '212', '2023-02-18', '16:45');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('130', '609', '200', '2022-09-02', '16:25');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('131', '609', '213', '2023-04-26', '9:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('132', '609', '206', '2023-04-26', '19:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('133', '610', '202', '2022-12-13', '19:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('134', '610', '202', '2022-11-15', '06:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('135', '611', '206', '2022-03-02', '8:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('136', '612', '203', '2023-01-02', '9:30');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('137', '612', '211', '2023-11-30', '8:45');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('138', '612', '214', '2023-09-29', '13:27');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('139', '612', '215', '2023-07-12', '12:14');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('140', '612', '214', '2023-10-13', '08:10');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('141', '612', '212', '2023-11-19', '8:15');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('144', '614', '201', '2023-04-12', '5:45');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('145', '614', '211', '2023-01-02', '17:23');
INSERT INTO Uso_do_cartao (id_uso_cartao, id_catraca, id_cartao, data, hora)
VALUES ('146', '614', '211', '2023-01-31', '10:10');
