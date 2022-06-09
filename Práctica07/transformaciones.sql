--- MODIFICACION DATOS
update datos set desc_derechohab = 'NO ESPECIFICADO' where desc_derechohab = 'NA' OR desc_derechohab = 'NINGUNO'; --50383
update datos set nivel_edu= 'SIN ACCESO A LA EDUCACIÓN' where nivel_edu = 'NA'; ---806
update datos set ocupacion = 'NO ESPECIFICADO' where ocupacion = 'NO ESPECIFICADO'; ---13317
update datos set religion = 'NINGUNA' where religion = 'NA';---4710
update datos set parentesco = 'NINGUNA' where parentesco = 'NA';---46659
update datos set naborto = '0' where naborto = 'NA';---1378
update datos set npartos = '0' where npartos = 'NA';---994
update datos set ncesarea = '0' where ncesarea = 'NA';---1397
update datos set nile = '0' where nile = 'NA';---11595
update datos set c_num = '0' where c_num = 'NA';---30697
update datos set s_complica = 'NO' where s_complica = 'NA';---24301
update datos set c_dolor = 'NO' where c_dolor = 'NA';---35336
update datos set panticoncep = 'NINGUNO' where panticoncep = 'NA';---36861
update datos set anticonceptivo = 'NINGUNO' where anticonceptivo = 'NA';---8723
update datos set consejeria = 'NO' where consejeria = 'NA';---4447
update datos set motiles = 'OTRA' where motiles = 'NA';---90
update datos set nhijos = '0' where nhijos = 'NA'; ---12011
update datos set alc_o_municipio = 'TLAJOMULCO DE ZUNIGA
' where alc_o_municipio = 'TLAJOMULCO DE ZUÑIGA';---15
update datos set procile_simplificada = 'ASPIRACION ENDOUTERINA (MANUAL O ELECTRICA)' where procile_simplificada = 'ASPIRACIÓN ENDOUTERINA (MANUAL O ELÉCTRICA)'; ---8252
update datosNuevos2 set tanalgesico = 'NO' where tanalgesico='NA' and c_dolor = 'NO';
update datosNuevos2 set tanalgesico = 'NO' where tanalgesico='NA';
--- ELIMINACION DATOS
delete from datos where clues_hospital = 'DFSSA003966';
delete from datos where edad = 'NA';
delete from datos where alc_o_municipio = 'NA';
delete from datos where fingreso = 'NA';
delete from datos where menarca = 'NA';
delete from datos where gesta = 'NA';
delete from datos where entidad = 'NA';
delete from datos where npartos = '1 hijo muerto';
delete from datos where npartos = '3 hijos vivos 1 obito';
delete from datos where npartos = 'LAPE Emabrazo Ectipico';
delete from datos where p_semgest = 'NA';
delete from datos where resultado_ile = 'OTRO';
delete from datos where clues_hospital = 'NA';
delete from datos where menarca = '??';
delete from datos where menarca = '163';
delete from datos where menarca = 'T';
delete from datos where menarca = '99';
delete from datos where menarca = '1218';
delete from datos where menarca = '¿?';
delete from datos where menarca = '121';
delete from datos where menarca = 'NE';
delete from datos where menarca = '0';
delete from datos where menarca = '8.3';
delete from datos where menarca = '05 AÑOS';
delete from datos where menarca = '147';
delete from datos where menarca = '121';
delete from datos where menarca = '123';
delete from datos where menarca = '1';
delete from datos where menarca = '2';
delete from datos where menarca = '3';
delete from datos where menarca = '88';
delete from datos where menarca = '6';
delete from datos where menarca = '4';
delete from datos where menarca = '5';
delete from datos where fsexual = '2' or fsexual = '128' or fsexual = '3' or fsexual = '4' or fsexual = '116' or fsexual = '115' or fsexual = '5' or fsexual = '1' or fsexual = '-1' or fsexual = '0' or fsexual = 'NA'
delete from datos where procile_simplificada = 'NA';


select count(*) from datosNuevos where c_fecha = 'NA';---25220
select count(*) from datosNuevos where h_fingreso = 'NA';---63192
select count(*) from datosNuevos where h_fegreso = 'NA'; ---75012
select count(*) from datosNuevos where fecha_cierre = 'NA';---72396
select count(*) from datosNuevos where consejeria = 'NA';---0
select count(*) from datosNuevos where p_consent = 'NA';---56398
select count(*) from datosNuevos where s_complica = 'NA';---0