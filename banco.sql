CREATE DATABASE db_cadeventos;
USE db_cadeventos;

CREATE TABLE tb_usuarios(
usu_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
usu_nome VARCHAR(255) NOT NULL,
usu_email VARCHAR(255) NOT NULL,
usu_senha VARCHAR(200) NOT NULL
);

CREATE TABLE tb_eventos(
eve_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
eve_titulo VARCHAR(255) NOT NULL,
eve_desc VARCHAR(500)  NOT NULL,
eve_usu_id INT NOT NULL,
FOREIGN KEY(eve_usu_id) REFERENCES tb_usuarios(usu_id),
eve_estado VARCHAR(2) NOT NULL,
eve_data DATE NOT NULL,
eve_cidade VARCHAR(30) NOT NULL,
eve_endereco VARCHAR(255) NOT NULL,
eve_hora TIME NOT NULL,
eve_org VARCHAR(100) NOT NULL
);

CREATE TABLE tb_pareve(
par_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
par_usu_id INT 	NOT NULL,
FOREIGN KEY(par_usu_id) REFERENCES tb_usuarios(usu_id),
par_eve_id INT NOT NULL,
FOREIGN KEY(par_eve_id) REFERENCES tb_eventos(eve_id)
);