from __init__ import *
import csv

analyzer = Dato(1)
for i in range(1, 11):
    analyzer.setIndice(i)
    modo = analyzer.getModo()
    datos = analyzer.getDict()
    llaves = sorted(datos.keys())
    fileName = modo + '.csv'
    with open(fileName, 'w') as csvfile:

        fieldnames = [modo, 'Numero']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')

        writer.writeheader()
        for l in llaves:
            writer.writerow({modo: l, 'Numero': datos[l]})
        writer.writerow({'Numero':analyzer.getLongitudDatos()})
