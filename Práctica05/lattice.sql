CREATE VIEW vista1
AS
SELECT SUM(ingreso) as ingreso,fechaID from ingresosMetro group by fechaID;

CREATE VIEW vista2
AS
SELECT SUM(ingreso) as ingreso,lineaID from ingresosMetro group by lineaID;

CREATE VIEW vista3
AS
SELECT SUM(ingreso) as ingreso,tipoIngresoID from ingresosMetro group by tipoIngresoID;

CREATE VIEW vista4
AS
SELECT SUM(ingreso) as ingreso,fechaID,lineaID from ingresosMetro group by fechaID,lineaID;

CREATE VIEW vista5
AS
SELECT SUM(ingreso) as ingreso,fechaID,tipoIngresoID from ingresosMetro group by fechaID,tipoIngresoID;

CREATE VIEW vista6
AS
SELECT SUM(ingreso) as ingreso,lineaID,tipoIngresoID from ingresosMetro group by lineaID,tipoIngresoID;