SELECT COUNT(*) as registros from ingresosMetro;
SELECT COUNT(*) as registros,anio from ingresosMetro group by anio;
SELECT SUM(ingreso) as ingresos,temp.descripcion from lineaMetro as temp INNER JOIN ingresosMetro on ingresosMetro.linea = temp.id group by temp.descripcion,ingresosMetro.linea order by ingresosMetro.linea;
SELECT SUM(ingreso) as ingresos,anio from ingresosMetro group by anio order by anio;
SELECT MAX(ingresos) as maximo,anio from (SELECT SUM(ingreso) as ingresos,anio from ingresosMetro group by anio) as temp group by anio order by anio;
SELECT MIN(ingresos) as minimo,anio from (SELECT SUM(ingreso) as ingresos,anio from ingresosMetro group by anio) as temp group by anio order by anio;
SELECT SUM(ingreso) as ingresos,temp.descripcion from tipoIngreso as temp INNER JOIN ingresosMetro on ingresosMetro.tipoIngreso = temp.id group by temp.descripcion,ingresosMetro.tipoIngreso order by ingresosMetro.tipoIngreso;
SELECT SUM(ingreso) as ingresos,diaSemana from ingresosMetro group by diaSemana order by diaSemana;
SELECT SUM(ingreso) as ingresos,diaSemana,anio from ingresosMetro group by diaSemana,anio order by anio;

CREATE VIEW a1 
AS 
(SELECT COUNT(*) as registros from ingresosMetro);
SELECT * FROM a1;

CREATE VIEW a2
AS
SELECT COUNT(*) as registros,anio from ingresosMetro group by anio;
SELECT * FROM a2;

CREATE VIEW b
AS
SELECT SUM(ingreso) as ingresos,temp.descripcion from lineaMetro as temp INNER JOIN ingresosMetro on ingresosMetro.linea = temp.id group by temp.descripcion,ingresosMetro.linea;
SELECT * FROM b order by descripcion;

CREATE VIEW c
AS
SELECT SUM(ingreso) as ingresos,anio from ingresosMetro group by anio;
SELECT * FROM c order by anio;

CREATE VIEW d
AS
SELECT SUM(ingreso) as ingresos,anio from ingresosMetro group by anio;
SELECT * from d;
SELECT anio,ingresos FROM d INNER JOIN (SELECT MAX(ingresos) as maximo from d) as temp ON d.ingresos = temp.maximo; 
SELECT anio,ingresos FROM d INNER JOIN (SELECT MIN(ingresos) as minimo from d) as temp ON d.ingresos = temp.minimo; 

CREATE VIEW e
AS 
SELECT SUM(ingreso) as ingresos,temp.descripcion from tipoIngreso as temp INNER JOIN ingresosMetro on ingresosMetro.tipoIngreso = temp.id group by temp.descripcion,ingresosMetro.tipoIngreso;
SELECT * from e;

CREATE VIEW f
AS
SELECT SUM(ingreso) as ingresos,diaSemana from ingresosMetro group by diaSemana;
SELECT * from f order by diaSemana;

CREATE VIEW g
AS
SELECT SUM(ingreso) as ingresos,diaSemana,anio from ingresosMetro group by diaSemana,anio;
SELECT * from g order by anio;