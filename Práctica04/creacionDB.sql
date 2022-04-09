CREATE TABLE catalogoSensores (
	id int NOT NULL IDENTITY,
	siglas varchar(3) NOT NULL,
	nombre varchar(50) NOT NULL,
	municipio varchar(50) NOT NULL,
	estado varchar(40) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE precipitacionPH (
	idDetector int NOT NULL,
	fecha date NOT NULL,
	valor float NOT NULL,
	dia int NOT NULL,
	mes int NOT NULL,
	anio int NOT NULL,
	semana int NOT NULL,
	FOREIGN KEY(idDetector) REFERENCES catalogoSensores(id),
	PRIMARY KEY(idDetector,fecha)
);