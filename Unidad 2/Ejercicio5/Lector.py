import csv
from PlanAhorroMod import PlanAhorro as pah

class Lectorcsv:

    def generarLista(listacsv):
        archivo = open("Unidad 2/Ejercicio5/planes.csv")
        reader = csv.reader(archivo, delimiter=";")
    
        for fila in reader:

            listacsv.append(pah(int(fila[0]), str(fila[1]), str(fila[2]), int(fila[3])))

            if (pah.getcantcuo() and pah.getcantcuopagas()) == 0:
                pah.setcantcuo(int(fila[4]))
                pah.setcantcuopagas(int(fila[5]))
      
        archivo.close()