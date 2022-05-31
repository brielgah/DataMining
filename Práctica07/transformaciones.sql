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