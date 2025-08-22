CREATE DATABASE teste;
use teste;
show tables;
create table cliente(
	id int primary key auto_increment,
    nome varchar(60) 
);
show tables;]
INSERT INTO cliente(nome)values('anaclara');
SELECT * FROM cliente;