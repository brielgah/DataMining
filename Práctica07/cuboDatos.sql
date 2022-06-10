CREATE VIEW vista1
AS
SELECT COUNT(*) as cantidad,cluesId from hechos group by cluesId;

CREATE VIEW vista2
AS
SELECT COUNT(*) as cantidad,edadId from hechos group by edadId;

CREATE VIEW vista3
AS
SELECT COUNT(*) as cantidad,fechaId,cluesId from hechos group by fechaId,cluesId;

CREATE VIEW vista4
AS
SELECT COUNT(*) as cantidad,edadId,estadoResidenciaId from hechos group by edadId,estadoResidenciaId;

CREATE VIEW vista5
AS
SELECT COUNT(*) as cantidad,edadId,estadoResidenciaId,municipioResidenciaId from hechos group by edadId,estadoResidenciaId,municipioResidenciaId;

CREATE VIEW vista6
AS
SELECT COUNT(*) as cantidad,religionId,edadSexualId,numeroAbortosId from hechos group by religionId,edadSexualId,numeroAbortosId;

CREATE VIEW vista7
AS
SELECT COUNT(*) as cantidad,estadoResidenciaId,municipioResidenciaId,cluesId from hechos group by estadoResidenciaId,municipioResidenciaId,cluesId;

CREATE VIEW vista8
AS
SELECT COUNT(*) as cantidad,fechaId,edadId,ocupacionId,estadoResidenciaId from hechos group by fechaId,edadId,ocupacionId,estadoResidenciaId;


CREATE VIEW vista9
AS
SELECT COUNT(*) as cantidad,fechaId,ocupacionId,parentescoId,estadoResidenciaId from hechos group by fechaId,ocupacionId,parentescoId,estadoResidenciaId;


CREATE VIEW vista10
AS
SELECT COUNT(*) as cantidad,edoCivilId,estadoResidenciaId from hechos group by edoCivilId,estadoResidenciaId;

CREATE VIEW vista11
AS
SELECT COUNT(*) as cantidad,fechaId,edadId,estadoResidenciaId,municipioResidenciaId,cluesId from hechos group by fechaId,edadId,estadoResidenciaId,municipioResidenciaId,cluesId;
