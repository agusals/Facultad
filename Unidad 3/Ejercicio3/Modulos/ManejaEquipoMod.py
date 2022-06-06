import csv
from .EquipoMod import equipo
import numpy as np
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

class manejaequipo:
    equipos=None
    __lista=None


    def __init__(self):

        archivo = open("Unidad 3/Ejercicio3/Equipos.csv")
        reader = csv.reader(archivo, delimiter=";")
        self.__lista = []
        next(reader)

        for fila in reader:
            
            self.__lista.append(equipo(fila[0],fila[1]))
            
        archivo.close()

        self.equipos = np.array(self.__lista)
        print(self.equipos[0].getnom())
        self.__lista = None

    def consultarContratosVencimiento(self):

        os.system("CLS")
        inpe = input("Ingrese nombre del equipo: ")

        cont = 0
        salir = False
        contratosfind = None

        while cont < self.equipos.size and salir != True:
            if self.equipos[cont].getnom() == inpe:
                print("Equipo encontrado!\n")
                contratosfind = self.equipos[cont].getcontratos()
                salir = True
            cont += 1
        
        if salir == True:
        
            hoy = datetime.now()
            hoy = hoy.strftime("%d/%m/%Y")
            hoy = datetime.strptime(str(hoy), "%d/%m/%Y")
            seismeses = hoy + relativedelta(months=6)

            band = False

            for contrato in contratosfind:
                fechacontrato = datetime.strptime(contrato.getfechaend(), "%d/%m/%Y") 

                if fechacontrato < seismeses:

                    band = True
                    jugadorx = contrato.getjugador()
                    print(jugadorx)
                
            if band == False:
                print("No hay contratos que vencen en los proximos 6 meses\n")

        else:

            print("Equipo no encontrado\n")

        input()

    def calcularImporteTotal(self):

        os.system("CLS")
        inpe = input("Ingrese nombre del equipo: ")

        cont = 0
        salir = False
        contratosfind = None

        while cont < self.equipos.size and salir != True:
            if self.equipos[cont].getnom() == inpe:
                print("Equipo encontrado!\n")
                contratosfind = self.equipos[cont].getcontratos()
                salir = True
            cont += 1
            
        if salir == True:

            imptotal = 0

            for contrato in contratosfind:
                imptotal += int(contrato.getpagomens())
                
            if imptotal != 0:
                print("Importe total: ${}" .format(imptotal))
            else:
                print("Equipo sin contratos activos\n")

        else:

            print("Equipo no encontrado\n")

        input()

    