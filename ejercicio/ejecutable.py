import csv
with open('ejercicio/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', newline='') as archivo:  
    lineas = csv.reader(archivo,delimiter=";")
    for linea in range(1, len(lineas)):
        print(linea[0])
