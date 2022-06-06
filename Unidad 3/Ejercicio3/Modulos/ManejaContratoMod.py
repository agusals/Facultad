import csv
import numpy as np
import os
from .ContratoMod import contrato
from .ManejaEquipoMod import manejaequipo
from .ManejaJugadorMod import manejajugador


class manejacontrato:
    contratos=None
    __lista=None


    def __init__(self, jugadores, equipos):

        archivo = open("Unidad 3/Ejercicio3/Contratos.csv")
        reader = csv.reader(archivo, delimiter=";")
        self.__lista = []
        
        

        for fila in reader:

            cont = 0
            salir = False
            jugadorx = None
            equipox= None

            while cont < len(jugadores.jugadores) and salir != True:
                if jugadores.jugadores[cont].getdni() == fila[3]:
                    jugadorx = jugadores.jugadores[cont]
                    salir = True
                cont += 1
            
            salir = False
            cont = 0
            
            while cont < equipos.equipos.size and salir != True:
                if equipos.equipos[cont].getnom() == fila[4]:
                    equipox = equipos.equipos[cont]
                    salir = True
                cont += 1
            
            if jugadorx != None and equipox != None:
                contratox = contrato(fila[0],fila[1],fila[2],jugadorx,equipox)
                self.__lista.append(contratox)
                equipox.setcontrato(contratox)
            else:
                print("No se encontro el jugador y/o el equipo\n")
            
        archivo.close()

        self.contratos = np.array(self.__lista)
        self.__lista = None

    def generaContrato(self, jugadores, equipos):
        
        cont = 0
        salir = False
        jugadorx = None
        equipox= None

        os.system("CLS")
        inpj = input("Ingrese DNI del jugador: ")
        os.system("CLS")
        inpe = input("Ingrese nombre del equipo: ")
        os.system("CLS")
        inpfi = input("Ingrese fecha de inicio del contrato: ")
        os.system("CLS")
        inpend = input("Ingrese fecha de finalizacion del contrato: ")
        os.system("CLS")
        inppm = input("Ingrese pago mensual: ")


        while cont < len(jugadores.jugadores) and salir != True:
            if int(jugadores.jugadores[cont].getdni()) == int(inpj):
                jugadorx = jugadores.jugadores[cont]
                #print("jugador encontrado:", jugadorx.getdni())
                #input()
                salir = True
            cont += 1
        
        salir = False
        cont = 0
            
        while cont < equipos.equipos.size and salir != True:
            if equipos.equipos[cont].getnom() == inpe:
                equipox = equipos.equipos[cont]
                #print("equipo encontrado: ", equipox.getnom())
                #input()
                salir = True
            cont += 1

        contratonew = contrato(inpfi, inpend, inppm, jugadorx, equipox)
        self.contratos = np.append(self.contratos, contratonew)
        equipox.setcontrato(contratonew)

        os.system("CLS")
        print("JUGADOR REGISTRADO!\n")
        #print(self.contratos.size)
        input()

    def consultaJugadoresContrato(self):

        os.system("CLS")
        inpj = input("Ingrese DNI del jugador: ")

        cont = 0
        salir = False

        while cont < self.contratos.size and salir != True:
            if int(self.contratos[cont].getjugadordni()) == int(inpj):
                print("Contrato:\n")
                print("Equipo: {} \nFecha de finalización: {}" .format(self.contratos[cont].getequiponom(), self.contratos[cont].getfechaend()))
                salir = True
            cont += 1
        
        if salir == False:
            print("Jugador no encontrado\n")

        input()

    def guardarContratos(self):

        linea=None

        with open("Unidad 3/Ejercicio3/Contratos.csv", "w", encoding="UTF8", newline="") as archivo:
            writer = csv.writer(archivo, delimiter=";", lineterminator="\n")

            for contrato in self.contratos:

                #fecha in;fecha end;pagomensual;dni;equiponom

                linea = [contrato.getfechain(), contrato.getfechaend(), contrato.getpagomens(), contrato.getjugadordni(), contrato.getequiponom()]

                writer.writerow(linea)
                writer

                linea = None


        print("Contratos guardados!\n")
        input()
                