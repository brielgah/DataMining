from collections import defaultdict
import csv
import datetime
import calendar
from email.policy import default

#Días de la semana
dias = {
    'Monday': 'LUNES',
    'Tuesday': 'MARTES',
    'Wednesday': 'MIERCOLES',
    'Thursday': 'JUEVES',
    'Friday': 'VIERNES',
    'Saturday': 'SABADO',
    'Sunday': 'DOMINGO'
}

estado_civil = {
    'UNION LIBRE' : 1,
    'SEPARADA' : 2,
    'VIUDA' : 3,
    'CASADA' : 4,
    'DIVORCIADA' : 5,
    'SOLTERA' : 6,
    'DESCONOCIDO' : 7
}

derecho_habiente = {
    'IMSS' : 1,
    'ISSSTE' : 2,
    'ISSTE' : 2,
    'SEGURO POPULAR' : 3,
    'NO ESPECIFICADO' : 4,
    'OTRA' : 5
}

educacion = {
    'PRIMARIA' : 1,
    'SECUNDARIA' : 2,
    'PREPARATORIA' : 3,
    'LICENCIATURA' : 4,
    'MAESTRIA' : 5,
    'DOCTORADO' : 6,
    'SIN ACCESO A LA EDUCACION FORMAL' : 7,
}

ocupacion = {
    'TRABAJADORA DEL HOGAR NO REMUNERADA' : 1,
    'EMPLEADA' : 2,
    'NO ESPECIFICADO' : 3,
    'DESEMPLEADA' : 4,
    'ESTUDIANTE' : 5
}

religion = {
    'MORMONA' : 1,
    'JUDIA' : 2,
    'CRISTIANA' : 3,
    'OTRA' : 4, 
    'ANGLICANA' : 5,
    'BUDISTA' : 6,
    'CATOLICA' : 7, 
    'TESTIGA DE JEHOVA' : 8,
    'NINGUNA' : 9,
    'MUSULMANA' : 10
}

paretesco = {
    'TUTOR O RESPONSABLE LEGAL' : 1,
    'AMIGA' : 2,
    'PAREJA' : 3,
    'RELACION LABORAL' : 4, 
    'PERSONA CERCANA' : 5, 
    'FAMILIAR SIN ESPECIFICAR' : 6, 
    'OTRA' : 7,
    'EX-PAREJA' : 8,
    'FAMILIAR MUJER' : 9,
    'CONOCIDO' : 10,
    'CONOCIDA' : 11,
    'EX-PAREJA' : 12, 
    'FAMILIAR HOMBRE' : 13,
    'PERSONA CERCANA MUJER' : 14,
    'AMIGO' : 15,
    'PERSONA CERCANA HOMBRE' : 16,
    'NINGUNA' : 17
}

estado_residencia = {
    'CHIHUAHUA' : 1,
    'CHIAPAS' : 2,
    'TABASCO' : 3,
    'BAJA CALIFORNIA' : 4,
    'NUEVO LEON' : 5,
    'HIDALGO' : 6,
    'ZACATECAS' : 7, 
    'SAN LUIS POTOSI' : 8,
    'TAMAULIPAS' : 9,
    'CIUDAD DE MEXICO' : 10,
    'AGUASCALIENTES' : 11,
    'TLAXCALA' : 12,
    'GUERRERO' : 13, 
    'MICHOACAN' : 14,
    'PUEBLA' : 15,
    'NAYARIT' : 16,
    'SINALOA' : 17,
    'DURANGO' : 18,
    'SONORA' : 19, 
    'QUINTANA ROO' : 20,
    'MORELOS' : 21,
    'OAXACA' : 22,
    'JALISCO' : 23,
    'VERACRUZ' : 24,
    'CAMPECHE' : 25,
    'COAHUILA' : 26,
    'GUANAJUATO' : 27,
    'YUCATAN' : 28,
    'QUERETARO' : 29,
    'COLIMA' : 30,
    'BAJA CALIFORNIA SUR' : 31, 
    'ESTADO DE MEXICO' : 32
}

ile_previo = {
    0 : 1,
    1 : 2,
    2 : 3,
    3 : 4,
    4 : 5,
    5 : 6,
    6 : 7,
    7 : 8,
    8 : 9,
    9 : 10
}

anticonceptivos = {
    'NINGUNO' : 1,
    'ANILLO VAGINAL' : 2,
    'INYECCION + DIU' : 3,
    'PASTILLA DE EMERGENCIA + PARCHES' : 4,
    'CONDON + INYECCION' : 5,
    'CONDON' : 6,
    'IMPLANTE SUBDERMICO' : 7,
    'PARCHES' : 8,
    'CONDON + PARCHE' : 9,
    'CONDON + DIU' : 10,
    'PASTILLA DE EMERGENCIA + INYECCION' : 11,
    'CONDON + PASTILLA ANTICONCEPTIVA' : 12,
    'CONDON + IMPLANTE' : 13,
    'PASTILLA DE EMERGENCIA' : 14,
    'LIGADURA DE TROMPAS' : 15,
    'DIU' : 16,
    'VASECTOMIA' : 17,
    'CONDON + PASTILLA DE EMERGENCIA' : 18,
    'PASTILLA ANTICONCEPTIVA' : 19,
    'INYECCION + LIGADURA DE TROMPAS' : 20,
    'INYECCION' : 21
}

anticonceptivo_post = {
    'NINGUNO' : 1,
    'DIU + IMPLANTE' : 2,
    'ANILLO VAGINAL' : 3,
    'CONDON + PASTILLA DE EMERGENCIA + DIU' : 4,
    'CONDON + INYECCION' : 5,
    'CONDON' : 6,
    'IMPLANTE SUBDERMICO' : 7,
    'PARCHE' : 8,
    'CONDON + PASTILLA DE EMERGENCIA + INYECCION' : 9,
    'CONDON + PARCHE' : 10,
    'CONDON + DIU' : 11,
    'CONDON + IMPLANTE SUBDERMICO' : 12,
    'CONDON + PASTILLA ANTICONCEPTIVA' : 13,
    'CONDON + LIGADURA DE TROMPAS' : 14,
    'CONDON + IMPLANTE' : 15,
    'PASTILLA DE EMERGENCIA' : 16,
    'LIGADURA DE TROMPAS' : 17,
    'DIU' : 18,
    'VASECTOMIA' : 19,
    'CONDON + PASTILLA DE EMERGENCIA + IMPLANTE' : 20,
    'DIU + IMPLANTE SUBDERMINCO' : 21,
    'IMPLANTE SUBDERMICO + PARCHE' : 22,
    'CONDON + PASTILLA DE EMERGENCIA' : 23,
    'PASTILLA ANTICONCEPTIVA' : 24,
    'INYECCION + PARCHE' : 25,
    'DIU + PARCHE' : 26,
    'INYECCION' : 27
}

resultadoILE =  {
    'COMPLETO': 1,
    'OTRO': 2
}

cluesHospital = {
    'DFSSA000864' : 1,
    'DFSSA002066' : 2,
    'DFSSA000065' : 3,
    'DFSSA000596' : 4,
    'DFSSA002993' : 5,
    'DFSSA000852' : 6,
    'DFSSA018166' : 7,
    'DFSSA003932' : 8,
    'DFSSA003705' : 9,
    'DFSSA004270' : 10,
    'DFSSA003640' : 11,
    'DFSSA000712' : 12,
    'DFSSA003915' : 13,
    'DFSSA002491' : 14,
    'DFSSA017886' : 15,
    'DFSSA002643' : 16,
    'DFSSA005093' : 17,
}

procedimiento_ILE = {
    'ASPIRACION ENDOUTERINA (MANUAL O ELECTRICA)' : 1,
    'LEGRADO' : 2,
    'MEDICAMENTO' : 3
}

respuestas_binarias = {
    'SI' : 1,
    'NO' : 2,
    'NA' : 3
}

motivos = {
    'SITUACION ECONOMICA' : 1,
    'INTERRUPCION VOLUNTARIA' : 2,
    'FALLA DEL METODO' : 3,
    'SIN APOYO' : 4,
    'OTRA' : 5,
    'DECISIONES VINCULADAS CON LA PAREJA' : 6,
    'PROBLEMAS DE SALUD' : 7,
    'PROYECTO DE VIDA' : 8, 
    'VIOLACION' : 9
}

municipios = {}

cantidades = {}

edades = {}
    
fechas = {}

edos_civiles = {}

edad = 0
menarca = 0
f_sexual = 0

n_hijos = 0
gesta = 0
n_aborto = 0
n_cesarea = 0
n_partos = 0
c_num = 0
p_sem_gest = 0

f_ingreso = 0
c_fecha = 0
fecha_cierre = 0
nile = 0

nth_row = 1

id_edo_civil = 0

with open('datosNuevos2.csv', newline='') as File:  
    reader = csv.reader(File)
    first = True
    cnt = 0
    id_fecha = 1
    id_edad = 1
    id_cantidades = 1
    id_municipios = 1
    for row in reader:
        nth_row+= 1
        if not first:
            #FECHA
            anio = int(row[0])
            dia, mes, _ = row[2].split('/')
            dia, mes = int(dia), int(mes)
            fecha = datetime.datetime(anio, mes, dia)
            dia_semana = calendar.day_name[fecha.weekday()]

            fecha = datetime.date(anio, mes, dia)

            if fecha not in fechas:
                fechas[fecha] = id_fecha
                query = f"INSERT INTO fecha VALUES ('{fecha}', {anio}, {mes}, {dia}, '{dias[dia_semana]}')"
                print(query)
                id_fecha += 1
                id_fecha_tmp = id_fecha
            else:
                id_fecha_tmp = id_fecha 
                id_fecha = fechas[fecha]
            
            fecha = fechas[fecha]

            edad = int(row[4])
            if edad not in edades:
                edades[edad] = id_edad
                query = f"INSERT INTO edades VALUES ({edad})"
                print(query)
                id_edad += 1
                id_edad_tmp = id_edad
            else:
                id_edad_tmp = id_edad
                id_edad = edades[edad]
            
            edad = edades[edad]
            
            menarca = int(float(row[12]))
            if menarca not in edades:
                edades[menarca] = id_edad
                query = f"INSERT INTO edades VALUES ({menarca})"
                print(query)
                id_edad += 1
                id_edad_tmp = id_edad
            else:
                id_edad_tmp = id_edad
                id_edad = edades[menarca]
            
            menarca = edades[menarca]
            
            f_sexual = row[13]
            if f_sexual != 'NA':
                f_sexual = int(f_sexual)
            else:
                f_sexual = 0

            if f_sexual not in edades:
                edades[f_sexual] = id_edad
                query = f"INSERT INTO edades VALUES ({f_sexual})"
                print(query)
                id_edad += 1
                id_edad_tmp = id_edad
            else:
                id_edad_tmp = id_edad
                id_edad = edades[f_sexual]
            
            f_sexual = edades[f_sexual]

            n_hijos = row[14]
            if n_hijos != 'NA':
                n_hijos = int(n_hijos)
            else:
                n_hijos = 0

            if n_hijos not in cantidades:
                cantidades[n_hijos] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_hijos})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_hijos]
            
            n_hijos = cantidades[n_hijos]

            gesta = int(row[15])
            if gesta not in cantidades:
                cantidades[gesta] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({gesta})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[gesta]
            
            gesta =  cantidades[gesta]

            n_aborto = int(row[16])
            if n_aborto not in cantidades:
                cantidades[n_aborto] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_aborto})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_aborto]
            
            n_aborto = cantidades[n_aborto]

            n_partos = int(row[17])
            if n_partos not in cantidades:
                cantidades[n_partos] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_partos})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_partos]
            
            n_partos = cantidades[n_partos]

            n_cesarea = int(row[18])
            if n_cesarea not in cantidades:
                cantidades[n_cesarea] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_cesarea})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_cesarea]
            
            n_cesarea = cantidades[n_cesarea]

            nile = int(row[19])
            if nile not in cantidades:
                cantidades[nile] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({nile})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[nile]
            
            nile = cantidades[nile]

            c_num = int(row[23])
            if c_num not in cantidades:
                cantidades[c_num] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({c_num})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[c_num]
            
            c_num = cantidades[c_num]

            sem_gesta = int(row[27])
            if sem_gesta not in cantidades:
                cantidades[sem_gesta] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({sem_gesta})"
                print(query)
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[sem_gesta]
            
            sem_gesta = cantidades[sem_gesta]


            
            municipio = row[11]
            if municipio not in municipios:
                municipios[municipio] = id_municipios
                query = f"INSERT INTO municipioResidencia VALUES ('{municipio}')"
                print(query)
                id_municipios += 1
                id_municipios_tmp = id_municipios
            else:
                id_municipios_tmp = id_municipios
                id_municipios = municipios[municipio]
            
            municipio = municipios[municipio]

            f_ingreso = fecha 
            edo_civil = estado_civil[row[3]]
            derecho_hab = derecho_habiente[row[5]]
            nivel_edu = educacion[row[6]]
            ocupa = ocupacion[row[7]]
            relig = religion[row[8]]
            paren = paretesco[row[9]]
            entidad = estado_residencia[row[10]]
            consejeria = respuestas_binarias[row[20]]
            anticonceptivo = anticonceptivos[row[21]]
            motivo = motivos[row[24]]
            p_concent = respuestas_binarias[row[28]]
            complica = respuestas_binarias[row[29]]
            dolor = respuestas_binarias[row[30]]
            analgesico = respuestas_binarias[row[31]]
            p_anticonceptivo = anticonceptivo_post[row[32]]
            clues = cluesHospital[row[35]]
            procile = procedimiento_ILE[row[36]]

            query = f"INSERT INTO hechos VALUES ({f_ingreso}, {edo_civil}, {edad}, {derecho_hab}, {nivel_edu}, {ocupa}, {relig}, {paren}, {entidad}, {municipio}, {menarca}, {f_sexual}, {gesta}, {n_aborto}, {n_partos}, {n_cesarea}, {consejeria}, {anticonceptivo}, {c_num}, {motivo}, {sem_gesta}, {p_concent}, {complica}, {dolor}, {analgesico}, {p_anticonceptivo}, {clues}, {procile})"
            print(query)

            id_fecha = id_fecha_tmp
            id_edad = id_edad_tmp
            id_cantidades = id_cantidades_tmp
            id_municipios = id_municipios_tmp

        first = False