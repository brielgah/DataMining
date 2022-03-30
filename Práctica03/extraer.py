import csv
import datetime
import calendar

#Días de la semana
dias = {'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miercoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sabado',
        'Sunday': 'Domingo'}

tipo_ingreso = {'Boletos': 1,
                'Tarjetas': 2,
                'Recargas': 3,
                'QR/Validador': 4}

with open('datos.csv', newline='') as File:  
    reader = csv.reader(File)
    first = True
    for row in reader:
        if not first:
            #FECHA
            dia, mes, ano = row[0].split('/')
            dia, mes, ano= int(dia), int(mes), int(ano)
            fecha = datetime.datetime(ano, mes, dia)
            dia_semana = calendar.day_name[fecha.weekday()]
            fecha = datetime.date(ano, mes, dia)
            
            #TIPO DE INGRESO
            tipo = tipo_ingreso[row[1]]

            for i in range(2,len(row)):
                ingreso = float(row[i]) if row[i] else 0
                linea = i - 1
                query = f"INSERT INTO ingresosMetro values('{fecha}', {tipo}, {linea}, {ingreso}, {dia}, {mes}, {ano}, '{dias[dia_semana]}')"
                print(query)


        first = False
