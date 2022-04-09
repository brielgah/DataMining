import csv
import datetime
import calendar

archivos = ['2010PPH.csv', '2011PPH.csv', '2012PPH.csv', '2013PPH.csv', '2014PPH.csv', '2015PPH.csv', '2016PPH.csv', '2017PPH.csv', '2018PPH.csv', '2019PPH.csv']
for archivo in archivos:
    with open(archivo, newline='') as File:  
        reader = csv.reader(File)
        first = True
        semana = 1
        for row in reader:
            if not first:#Omitimos la descripción de columna
                dia, mes, ano = row[0].split('/')
                dia, mes, ano= int(dia), int(mes), int(ano)
                fecha = datetime.date(ano, mes, dia)
                for i in range(1,17):#Recorrido de columnas
                    valor = row[i]
                    if valor == '-99':#Si el valor es nulo omitimos ese dato
                        continue
                    #Creación de la query
                    query = f"INSERT INTO precipitacionPH values ({i}, '{fecha}', {valor}, {dia}, {mes}, {ano}, {semana})"
                    print(query)
                semana += 1
            first = False