import csv
import numpy as np
import os
from .CalefactorElectricoMod import calefactorelectrico
from .CalefactorGasMod import calefactorgas

class coleccioncalefactores:

    calefactores=None

    def __init__(self, tamanio):
        
        self.calefactores = np.empty(tamanio, dtype=object)
        calef = None
        i = 0

        with open("Unidad 3/Ejercicio4/calefactor-electrico.csv", "r", encoding="UTF8") as archivo:
            reader = csv.reader(archivo, delimiter=";")

            for fila in reader:
                calef = None
                if i<tamanio:
                    calef = calefactorelectrico(fila[0], fila[1], fila[2], fila[3])
                    self.calefactores[i] = calef
                    i += 1
        
        if i < tamanio:
            with open("Unidad 3/Ejercicio4/calefactor-a-gas.csv", "r", encoding="UTF8") as archivo:
                reader = csv.reader(archivo, delimiter=";")

                for fila in reader:
                    calef = None
                    if i<tamanio:
                        calef = calefactorgas(fila[0], fila[1], fila[2], fila[3], fila[4])
                        self.calefactores[i] = calef
                        i += 1

        print("Coleccion cargada!\n")
        input()

    def printcoso(self):
        for c in self.calefactores:
            try:
                print(c.gettipo())
            
            except:
                print(c)

    def baratogas(self):
        os.system("CLS")
        costo = input("Ingrese costo por m3: ")
        os.system("CLS")
        cantidad = input("Ingrese cantidad a consumir: ")
        os.system("CLS")

        mult = int(costo) * int(cantidad)

        min = 99999999
        marcamin = " "
        modelmin = " "
        calefmin = None

        for calef in self.calefactores:
            if int(calef.getcosto()) < int(min) and calef.gettipo() == "gas":
                min = int(calef.getcosto())
                marcamin = calef.getmarca()
                modelmin = calef.getmodel()
                calefmin = calef

        if min < mult:

            print("Marca: {}  Modelo: {} Tipo: gas\n" .format(marcamin, modelmin))
            print("Costo: {}  Calorías: {}  Matrícula: {}" .format(calefmin.getcosto(), calefmin.getcalorias(), calefmin.getmatricula()))

        input()

    def baratoelec(self):

        os.system("CLS")
        costo = input("Ingrese costo por kW/h: ")
        os.system("CLS")
        cantidad = input("Ingrese cantidad a consumir: ")
        os.system("CLS")

        mult = int(costo) * int(cantidad)

        min = 99999999
        marcamin = " "
        modelmin = " "
        calefmin = None

        for calef in self.calefactores:
            if int(calef.getcosto()) < int(min) and calef.gettipo() == "electrico":
                min = int(calef.getcosto())
                marcamin = calef.getmarca()
                modelmin = calef.getmodel()
                calefmin = calef

        if min < mult:

            print("Marca: {}  Modelo: {}  Tipo: eléctrico\n" .format(marcamin, modelmin))
            print("Costo: {}  Pot. Máxima: {}" .format(calefmin.getcosto(), calefmin.getpotmax()))

        input()



            
                


        
                