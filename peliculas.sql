DROP DATABASE IF EXISTS PELICULAS;
CREATE DATABASE IF NOT EXISTS PELICULAS;
USE PELICULAS;
CREATE TABLE peliculas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion text NOT NULL,
    duracion VARCHAR(255) NOT NULL,
	clasificacion VARCHAR(255) NOT NULL
);


CREATE TABLE usuarios(
    id_usuario BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(255) NOT NULL,
    nombreCompleto VARCHAR(255) NOT NULL,
    correoElectronico VARCHAR(255) NOT NULL,
    clave VARCHAR(20) NOT NULL,
    perfil VARCHAR(255) NOT NULL
);


CREATE TABLE salas(
    id_sala BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    numeroSala INT NOT NULL,
    capacidad INT NOT NULL
);


INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`) VALUES ('root', '1234', 'admin');