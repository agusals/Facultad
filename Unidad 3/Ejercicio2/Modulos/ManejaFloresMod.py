import numpy as np
import csv
from Modulos.FloresMod import flor

class manejaflores:
    flores = None
    __lista = None

    def __init__(self):
        archivo = open("Unidad 3/Ejercicio2/Flores.csv")
        reader = csv.reader(archivo, delimiter=",")
        self.__lista = []

        for fila in reader:
            
            self.__lista.append(flor(fila[0], fila[1], fila[2], fila[3]))
            
        archivo.close()

        self.flores = np.array(self.__lista)
        self.__lista = None


