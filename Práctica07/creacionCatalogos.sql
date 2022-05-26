create table anio (
    id int not null IDENTITY,
    anio int not null,
    PRIMARY KEY(id)
);

create table mes(
    id int not null IDENTITY,
    mes varchar(15) not null,
    PRIMARY KEY(id)
);

CREATE TABLE edoCivil(
    id int not null IDENTITY,
    descripcion varchar(25) not null
    PRIMARY KEY(id)
);

INSERT INTO edoCivil VALUES("UNION LIBRE");
INSERT INTO edoCivil VALUES("SEPARADA");
INSERT INTO edoCivil VALUES("VIUDA");
INSERT INTO edoCivil VALUES("CASADA");
INSERT INTO edoCivil VALUES("DIVORCIADA");
INSERT INTO edoCivil VALUES("SOLTERA");
INSERT INTO edoCivil VALUES("DESCONOCIDO");

//En edad quitar los 20 que tienen "NA"

//En desc_derecho cambiar "NA" = "NINGUNO" y "NINGUNO" = "SEGURO POPULAR"

CREATE TABLE derechoHabiente(
    id int not null IDENTITY,
    descripcion varchar(25) not null,
    PRIMARY KEY(id)
)
INSERT INTO derechoHabiente VALUES("IMSS");
INSERT INTO derechoHabiente VALUES("ISSTE");
INSERT INTO derechoHabiente VALUES("SEGURO POPULAR");
INSERT INTO derechoHabiente VALUES("NO ESPECIFICADO");
INSERT INTO derechoHabiente VALUES("OTRA");

//cambiar el na = SIN ACCESO A LA EDUCACION FORMAL

CREATE TABLE educacion(
    id not null IDENTITY,
    descripcion varchar(25) not null,
    PRIMARY KEY(id)
)

INSERT INTO educacion VALUES("PRIMARIA");
INSERT INTO educacion VALUES("SECUNDARIA");
INSERT INTO educacion VALUES("PREPARATORIA");
INSERT INTO educacion VALUES("LICENCIATURA");
INSERT INTO educacion VALUES("MAESTRIA");
INSERT INTO educacion VALUES("DOCTORADO");
INSERT INTO educacion VALUES("SIN ACCESO A LA EDUCACION FORMAL");

//Cambiar NA = "NO ESPECIFICADO"
CREATE TABLE ocupacion(
    id not null IDENTITY,
    descripcion varchar(40) not null,
    primary key(id)
)

INSERT INTO educacion VALUES("TRABAJADORA DEL HOGAR NO REMUNERADA");
INSERT INTO educacion VALUES("EMPLEADA");
INSERT INTO educacion VALUES("NO ESPECIFICADO");
INSERT INTO educacion VALUES("DESEMPLEADA");
INSERT INTO educacion VALUES("ESTUDIANTE");

//Cambiar NA = NINGUNA
CREATE TABLE religion(
    id not null IDENTITY,
    descripcion varchar(20) not null,
    primary key(id)
)


INSERT INTO religion VALUES("MORMONA");
INSERT INTO religion VALUES("JUDIA");
INSERT INTO religion VALUES("CRISTIANA");
INSERT INTO religion VALUES("OTRA");
INSERT INTO religion VALUES("ANGLICANA");
INSERT INTO religion VALUES("BUDISTA");
INSERT INTO religion VALUES("CATOLICA");
INSERT INTO religion VALUES("TESTIGA DE JEHOVA");
INSERT INTO religion VALUES("NINGUNA");
INSERT INTO religion VALUES("MUSULMANA");

//Cambiar NA = NINGUNA
create table parentesco (
    id not null IDENTITY,
    descripcion varchar(50) not null,
    primary key(id)
)
//Cambiar NA = Ninguno

INSERT INTO parentesco VALUES("TUTOR O RESPONSABLE LEGAL");
INSERT INTO parentesco VALUES("AMIGA");
INSERT INTO parentesco VALUES("PAREJA");
INSERT INTO parentesco VALUES("RELACION LABORAL");
INSERT INTO parentesco VALUES("PERSONA CERCANA");
INSERT INTO parentesco VALUES("FAMILIAR SIN ESPECIFICAR");
INSERT INTO parentesco VALUES("OTRA");
INSERT INTO parentesco VALUES("EX-PAREJA");
INSERT INTO parentesco VALUES("FAMILIAR MUJER");
INSERT INTO parentesco VALUES("CONOCIDO");
INSERT INTO parentesco VALUES("CONOCIDA");
INSERT INTO parentesco VALUES("EX-PAREJA");
INSERT INTO parentesco VALUES("FAMILIAR HOMBRE");
INSERT INTO parentesco VALUES("PERSONA CERCANA MUJER");
INSERT INTO parentesco VALUES("AMIGO");
INSERT INTO parentesco VALUES("PERSONA CERCANA HOMBRE");
INSERT INTO parentesco VALUES("NINGUNA");

create table estadoResidencia(
    id not null IDENTITY,
    descripcion varchar(50) not null,
    primary key(id)
)

// Cambiar NUEVO LEÓN = NUEVO LEON
// SAN LUIS POTOSÍ = SAN LUIS POTOSI 
// CIUDAD DE MÉXICO = CIUDAD DE MEXICO
// MICHOACÁN = MICHOACAN
// YUCATÁN = YUCATAN
// QUERÉTARO = QUERETARO
// ESTADO DE MÉXICO = ESTADO DE MEXICO

INSERT INTO estadoResidencia VALUES("CHIHUAHUA");
INSERT INTO estadoResidencia VALUES("CHIAPAS");
INSERT INTO estadoResidencia VALUES("TABASCO");
INSERT INTO estadoResidencia VALUES("BAJA CALIFORNIA");
INSERT INTO estadoResidencia VALUES("NUEVO LEÓN");
INSERT INTO estadoResidencia VALUES("HIDALGO");
INSERT INTO estadoResidencia VALUES("ZACATECAS");
INSERT INTO estadoResidencia VALUES("SAN LUIS POTOSÍ");
INSERT INTO estadoResidencia VALUES("TAMAULIPAS");
INSERT INTO estadoResidencia VALUES("CIUDAD DE MÉXICO");
INSERT INTO estadoResidencia VALUES("AGUASCALIENTES");
INSERT INTO estadoResidencia VALUES("TLAXCALA");
INSERT INTO estadoResidencia VALUES("GUERRERO");
INSERT INTO estadoResidencia VALUES("MICHOACÁN");
INSERT INTO estadoResidencia VALUES("PUEBLA");
INSERT INTO estadoResidencia VALUES("NAYARIT");
INSERT INTO estadoResidencia VALUES("SINALOA");
INSERT INTO estadoResidencia VALUES("DURANGO");
INSERT INTO estadoResidencia VALUES("SONORA");
INSERT INTO estadoResidencia VALUES("QUINTANA ROO");
INSERT INTO estadoResidencia VALUES("MORELOS");
INSERT INTO estadoResidencia VALUES("OAXACA");
INSERT INTO estadoResidencia VALUES("JALISCO");
INSERT INTO estadoResidencia VALUES("VERACRUZ");
INSERT INTO estadoResidencia VALUES("CAMPECHE");
INSERT INTO estadoResidencia VALUES("COAHUILA");
INSERT INTO estadoResidencia VALUES("GUANAJUATO");
INSERT INTO estadoResidencia VALUES("YUCATÁN");
INSERT INTO estadoResidencia VALUES("QUERÉTARO");
INSERT INTO estadoResidencia VALUES("COLIMA");
INSERT INTO estadoResidencia VALUES("BAJA CALIFORNIA SUR");
INSERT INTO estadoResidencia VALUES("ESTADO DE MÉXICO");


//Se genera con script
create table municipioResidencia(
    id int not null IDENTITY,
    descripcion varchar(50) not null,
    primary key(id)
)


create table ILEPrevios(
    id int not null IDENTITY,
    cantidad int not null,
    primary key(id)
)
// cambiar NA = 0
INSERT INTO ILEPrevios VALUES(0);
INSERT INTO ILEPrevios VALUES(1);
INSERT INTO ILEPrevios VALUES(2);
INSERT INTO ILEPrevios VALUES(3);
INSERT INTO ILEPrevios VALUES(4);
INSERT INTO ILEPrevios VALUES(5);
INSERT INTO ILEPrevios VALUES(6);
INSERT INTO ILEPrevios VALUES(7);
INSERT INTO ILEPrevios VALUES(8);
INSERT INTO ILEPrevios VALUES(9);


create table consejeria(
    id int not null IDENTITY,
    descripcion varchar(2) not null,
    primary key(id)
)

INSERT INTO consejeria VALUES('SI');
INSERT INTO consejeria VALUES('NO');

create table anticonceptivo(
    id int not null IDENTITY,
    descripcion vachar(50) not null,
    primary key(id)
)

//cambiar na = ninguno

insert into anticonceptivo values('NINGUNO');
insert into anticonceptivo values('ANILLO VAGINAL');
insert into anticonceptivo values('INYECCION + DIU');
insert into anticonceptivo values('PASTILLA DE EMERGENCIA + PARCHES');
insert into anticonceptivo values('CONDON + INYECCION');
insert into anticonceptivo values('CONDON');
insert into anticonceptivo values('IMPLANTE SUBDERMICO');
insert into anticonceptivo values('PARCHES');
insert into anticonceptivo values('CONDON + PARCHE');
insert into anticonceptivo values('CONDON + DIU');
insert into anticonceptivo values('PASTILLA DE EMERGENCIA + INYECCION');
insert into anticonceptivo values('CONDON + PASTILLA ANTICONCEPTIVA');
insert into anticonceptivo values('CONDON + IMPLANTE');
insert into anticonceptivo values('PASTILLA DE EMERGENCIA');
insert into anticonceptivo values('LIGADURA DE TROMPAS');
insert into anticonceptivo values('DIU');
insert into anticonceptivo values('VASECTOMIA');
insert into anticonceptivo values('CONDON + PASTILLA DE EMERGENCIA');
insert into anticonceptivo values('PASTILLA ANTICONCEPTIVA');
insert into anticonceptivo values('INYECCION + LIGADURA DE TROMPAS');
insert into anticonceptivo values('INYECCION');

create table motivos(
    id int not null IDENTITY,
    descripcion varchar(50) not null,
    primary key(id)
)
// cambiar na = otra
insert into motivos values('SITUACION ECONOMICA')
insert into motivos values('INTERRUPCION VOLUNTARIA')
insert into motivos values('FALLA DEL METODO')
insert into motivos values('SIN APOYO')
insert into motivos values('OTRA')
insert into motivos values('DECISIONES VÍNCULADAS CON LA PAREJA')
insert into motivos values('PROBLEMAS DE SALUD')
insert into motivos values('PROYECTO DE VIDA')
insert into motivos values('VIOLACION')

create table anticonceptivoPost(
    id not null IDENTITY,
    descripcion varchar(50) not null,
    primary key(id)
)
// cambiar na = ninguno
insert into anticonceptivoPost values('NINGUNO')
insert into anticonceptivoPost values('DIU + IMPLANTE')
insert into anticonceptivoPost values('ANILLO VAGINAL')
insert into anticonceptivoPost values('CONDON + PASTILLA DE EMERGENCIA + DIU')
insert into anticonceptivoPost values('CONDON + INYECCION')
insert into anticonceptivoPost values('CONDON')
insert into anticonceptivoPost values('IMPLANTE SUBDERMICO')
insert into anticonceptivoPost values('PARCHE')
insert into anticonceptivoPost values('CONDON + PASTILLA DE EMERGENCIA + INYECCION')
insert into anticonceptivoPost values('CONDON + PARCHE')
insert into anticonceptivoPost values('CONDON + DIU')
insert into anticonceptivoPost values('CONDON + IMPLANTE SUBDERMICO')
insert into anticonceptivoPost values('CONDON + PASTILLA ANTICONCEPTIVA')
insert into anticonceptivoPost values('CONDON + LIGADURA DE TROMPAS')
insert into anticonceptivoPost values('CONDON + IMPLANTE')
insert into anticonceptivoPost values('PASTILLA DE EMERGENCIA')
insert into anticonceptivoPost values('LIGADURA DE TROMPAS')
insert into anticonceptivoPost values('DIU')
insert into anticonceptivoPost values('VASECTOMIA')
insert into anticonceptivoPost values('CONDON + PASTILLA DE EMERGENCIA + IMPLANTE')
insert into anticonceptivoPost values('DIU + IMPLANTE SUBDERMINCO')
insert into anticonceptivoPost values('IMPLANTE SUBDERMICO + PARCHE')
insert into anticonceptivoPost values('CONDON + PASTILLA DE EMERGENCIA')
insert into anticonceptivoPost values('PASTILLA ANTICONCEPTIVA')
insert into anticonceptivoPost values('INYECCION + PARCHE')
insert into anticonceptivoPost values('DIU + PARCHE')
insert into anticonceptivoPost values('INYECCION')

create table complicaciones(
    id int not null IDENTITY,
    descripcion varchar(2) not null,
    primary key(id)
)
// cambiar na = no
insert into complicaciones values('SI');
insert into complicaciones values('NO');

create table dolor(
    id int not null IDENTITY,
    descripcion varchar(2) not null,
    primary key(id)
)
// cambiar na = no
insert into dolor values('SI');
insert into dolor values('NO');

create table resultadoILE(
    id int not null IDENTITY,
    descripcion varchar(15) not null,
    primary key(id)
)
// tiene NA
insert into resultadoILE values('COMPLETO');
insert into resultadoILE values('OTRO');

create table CLUESHospital(
    id int not null IDENTITY,
    desc_derecho varchar(20) not null,
    primary key(id)
);

// eliminar los que tienen na

insert into CLUESHospital values('DFSSA000864');
insert into CLUESHospital values('DFSSA002066');
insert into CLUESHospital values('DFSSA000065');
insert into CLUESHospital values('DFSSA000596');
insert into CLUESHospital values('DFSSA002993');
insert into CLUESHospital values('DFSSA000852');
insert into CLUESHospital values('DFSSA018166');
insert into CLUESHospital values('DFSSA003932');
insert into CLUESHospital values('DFSSA003705');
insert into CLUESHospital values('DFSSA004270');
insert into CLUESHospital values('DFSSA003640');
insert into CLUESHospital values('DFSSA000712');
insert into CLUESHospital values('DFSSA003915');
insert into CLUESHospital values('DFSSA003966');
insert into CLUESHospital values('DFSSA002491');
insert into CLUESHospital values('DFSSA017886');
insert into CLUESHospital values('DFSSA002643');
insert into CLUESHospital values('DFSSA005093');


create table procedimientoILE(
    id int not null IDENTITY,
    descripcion varchar(50) not null,
    primary key(id)
)
//eliminar los que tienen NA

insert into procedimientoILE values('ASPIRACIÓN ENDOUTERINA (MANUAL O ELÉCTRICA)');
insert into procedimientoILE values('LEGRADO');
insert into procedimientoILE values('MEDICAMENTO');

create table procedimientoCompleto(
    id int not null,
    descripcion varchar(50) not null,
    primary key(id, descripcion),
    foreign key(id) references procedimientoILE(id)
)

insert into procedimientoCompleto values(3,'MISOPROSTOL');
insert into procedimientoCompleto values(3,'MISOPROSTOL + MIFEPRISTONA + MISOPROSTOL');
insert into procedimientoCompleto values(3,'MEDICAMENTO');
insert into procedimientoCompleto values(3,'MIFEPRISTONA');
insert into procedimientoCompleto values(3,'MISOPROSTOL + MIFEPRISTONA');
