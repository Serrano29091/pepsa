DROP DATABASE IF EXISTS PEPS;
CREATE DATABASE IF NOT EXISTS PEPS;
USE PEPS;
CREATE TABLE películas(
    id_pelicula BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    duracion INT NOT NULL,
	clasificacion INT
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
