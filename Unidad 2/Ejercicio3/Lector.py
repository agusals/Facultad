import csv
from Reg import Registro as r

class Lector:

    def generarLista(arr):
        archivo = open("Unidad 2/Ejercicio3/archivo.txt")
        reader = csv.reader(archivo, delimiter=",", skipinitialspace=True)
    
        for fila in reader:

            arr[int(fila[0])-1][int(fila[1])] = r(int(fila[2]), int(fila[3]), int(fila[4]))
             
        archivo.close()