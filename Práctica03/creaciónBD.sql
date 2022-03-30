CREATE TABLE tipoIngreso(
    id int NOT NULL IDENTITY,
    descripcion varchar(50) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE lineaMetro(
	id int NOT NULL IDENTITY,
	descripcion varchar(50) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE ingresosMetro(
	fecha date NOT NULL,
	tipoIngreso int NOT NULL,
	linea int NOT NULL,
	ingreso money NOT NULL,
	dia int NOT NULL,
	mes int NOT NULL,
	año int NOT NULL,
	diaSemana varchar(10) NOT NULL,
	FOREIGN KEY(tipoIngreso) REFERENCES tipoIngreso(id),
	FOREIGN KEY(linea) REFERENCES lineaMetro(id),
	PRIMARY KEY(fecha,linea)
);

INSERT INTO tipoIngreso VALUES('Boleto');
INSERT INTO tipoIngreso VALUES('Tarjeta');
INSERT INTO tipoIngreso VALUES('Recarga');
INSERT INTO tipoIngreso VALUES('QR/Validador');

INSERT INTO lineaMetro VALUES('1');
INSERT INTO lineaMetro VALUES('2');
INSERT INTO lineaMetro VALUES('3');
INSERT INTO lineaMetro VALUES('4');
INSERT INTO lineaMetro VALUES('5');
INSERT INTO lineaMetro VALUES('6');
INSERT INTO lineaMetro VALUES('7');
INSERT INTO lineaMetro VALUES('8');
INSERT INTO lineaMetro VALUES('9');
INSERT INTO lineaMetro VALUES('A');
INSERT INTO lineaMetro VALUES('B');
INSERT INTO lineaMetro VALUES('12');
