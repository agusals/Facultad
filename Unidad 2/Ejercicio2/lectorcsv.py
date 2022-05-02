import csv
from viajeromod import ViajeroFrecuente as vf

class Lector:

    def generarLista(listacsv):
        archivo = open("Unidad 2/Ejercicio2/viajeros.csv")
        reader = csv.reader(archivo, delimiter=",", skipinitialspace=True)
    
        for fila in reader:
            #print(fila)
            listacsv.append(vf(int(fila[0]), str(fila[1]), str(fila[2]), str(fila[3]), int(fila[4])))
                
            """for i in range(len(fila)):
              listacsv.append(v())
            for i in range(len(fila)):
                mail = fila[i]
                listacsv[i].crearCuenta(str(mail), False)"""
             
        archivo.close()