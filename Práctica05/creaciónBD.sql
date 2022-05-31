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

CREATE TABLE fecha(
	id int NOT NULL IDENTITY,
	fecha date NOT NULL,
	dia int NOT NULL,
	mes int NOT NULL,
	ano int NOT NULL,
	diaSemana varchar(10) NOT NULL,
	PRIMARY KEY(id),
);

CREATE TABLE ingresosMetro(
	fechaID int NOT NULL,
	tipoIngresoID int NOT NULL,
	lineaID int NOT NULL,
	ingreso money NOT NULL,
	FOREIGN KEY(tipoIngresoID) REFERENCES tipoIngreso(id),
	FOREIGN KEY(lineaID) REFERENCES lineaMetro(id),
	FOREIGN KEY(fechaID) REFERENCES fecha(id),
	PRIMARY KEY(fechaID,lineaID,tipoIngresoID)
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