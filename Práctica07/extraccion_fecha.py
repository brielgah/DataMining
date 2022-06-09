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
    'TRABAJADORA DEL HOGAR NO REMUNERADA' : 8,
    'EMPLEADA' : 9,
    'NO ESPECIFICADO' : 10,
    'DESEMPLEADA' : 11,
    'ESTUDIANTE' : 12
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
    'QUERÉTARO' : 29,
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

anticonceptivo = {
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
    'INYECCION + LIGADURA DE TROMPAS' : 22,
    'INYECCION' : 23
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
    'ASPIRACIÓN ENDOUTERINA (MANUAL O ELÉCTRICA)' : 1,
    'LEGRADO' : 2,
    'MEDICAMENTO' : 3
}

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

with open('datosNuevos.csv', newline='') as File:  
    reader = csv.reader(File)
    first = True
    cnt = 0
    id_fecha = 0
    id_edad = 0
    id_cantidades = 0
    for row in reader:
        print(nth_row)
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
                #print(query)
                id_fecha += 1
                id_fecha_tmp = id_fecha
            else:
                id_fecha_tmp = id_fecha 
                id_fecha = fechas[fecha]
            
            edad = int(row[4])
            if edad not in edades:
                edades[edad] = id_edad
                query = f"INSERT INTO edades VALUES ({edad})"
                id_edad += 1
                id_edad_tmp = id_edad
            else:
                id_edad_tmp = id_edad
                id_edad = edades[edad]
            
            edad = id_edad
            
            menarca = int(float(row[12]))
            if menarca not in edades:
                edades[menarca] = id_edad
                query = f"INSERT INTO edades VALUES ({menarca})"
                id_edad += 1
                id_edad_tmp = id_edad
            else:
                id_edad_tmp = id_edad
                id_edad = edades[menarca]
            
            menarca = id_edad
            
            f_sexual = row[13]
            if f_sexual != 'NA':
                f_sexual = int(f_sexual)
            else:
                f_sexual = 0

            if f_sexual not in edades:
                edades[f_sexual] = id_edad
                query = f"INSERT INTO edades VALUES ({f_sexual})"
                id_edad += 1
                id_edad_tmp = id_edad
            else:
                id_edad_tmp = id_edad
                id_edad = edades[f_sexual]
            
            f_sexual = id_edad

            n_hijos = row[14]
            if n_hijos != 'NA':
                n_hijos = int(n_hijos)
            else:
                n_hijos = 0

            if n_hijos not in cantidades:
                cantidades[n_hijos] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_hijos})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_hijos]
            
            n_hijos = id_cantidades

            gesta = int(row[15])
            if gesta not in cantidades:
                cantidades[gesta] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({gesta})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[gesta]
            
            gesta = id_cantidades

            n_aborto = int(row[16])
            if n_aborto not in cantidades:
                cantidades[n_aborto] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_aborto})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_aborto]
            
            n_aborto = id_cantidades

            n_partos = int(row[17])
            if n_partos not in cantidades:
                cantidades[n_partos] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_partos})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_partos]
            
            n_partos = id_cantidades

            n_cesarea = int(row[18])
            if n_cesarea not in cantidades:
                cantidades[n_cesarea] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({n_cesarea})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[n_cesarea]
            
            n_cesarea = id_cantidades

            nile = int(row[19])
            if nile not in cantidades:
                cantidades[nile] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({nile})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[nile]
            
            nile = id_cantidades

            c_num = int(row[23])
            if c_num not in cantidades:
                cantidades[c_num] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({c_num})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[c_num]
            
            c_num = id_cantidades

            sem_gesta = int(row[27])
            if sem_gesta not in cantidades:
                cantidades[sem_gesta] = id_cantidades
                query = f"INSERT INTO cantidades VALUES ({sem_gesta})"
                id_cantidades += 1
                id_cantidades_tmp = id_cantidades
            else:
                id_cantidades_tmp = id_cantidades
                id_cantidades = cantidades[sem_gesta]
            
            sem_gesta = id_cantidades

            


            id_fecha = id_fecha_tmp
            id_edad = id_edad_tmp
            id_cantidades = id_cantidades_tmp

        first = False
    print(cnt)