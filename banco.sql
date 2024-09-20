create database db_cadeventos;
use db_cadeventos;

create table tb_usuarios(
usu_id int primary key not null auto_increment,
usu_nome varchar(255) not null,
usu_email varchar(255) not null,
usu_senha varchar(200) not null
);

create table tb_eventos(
eve_id int primary key not null auto_increment,
eve_titulo varchar(255) not null,
eve_desc varchar(500)  not null,
eve_usu_id int not null,
foreign key(eve_usu_id) references tb_usuarios(usu_id),
eve_estado varchar(2) not null,
eve_data date not null,
eve_cidade varchar(30) not null,
eve_endereco varchar(255) not null,
eve_hora time not null
);

create table tb_pareve(
par_id int primary key not null auto_increment,
par_usu_id int not null,
foreign key(par_usu_id) references tb_usuarios(usu_id),
par_eve_id int not null,
foreign key(par_eve_id) references tb_eventos(eve_id)
);
