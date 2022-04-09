CREATE VIEW a1 
AS
select count(*)as registros from precipitacionPH;
select * from a1;

CREATE VIEW a2
AS
SELECT COUNT(*) as registros,anio from precipitacionPH 
group by anio;
select * from a2 order by anio;

create view b
as 
select sum(valor) as precipitacion, semana from precipitacionPH 
group by semana;
select * from b order by semana;

create view b1
as 
select sum(valor) as precipitacion, mes from precipitacionPH 
group by mes;
select * from b1 order by mes;

create view b2
as 
select sum(valor) as precipitacion, anio from precipitacionPH 
group by anio;
select * from b2 order by anio;

create view c
as
select AVG(valor) as precipitacion, siglas as 
detector,nombre,municipio from precipitacionPH 
INNER join catalogoSensores on idDetector = id 
group by nombre,municipio,siglas;
select * from c order by precipitacion desc;