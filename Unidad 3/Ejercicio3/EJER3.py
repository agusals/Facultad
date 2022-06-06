import csv
import numpy as np
import os
from Modulos.ManejaContratoMod import manejacontrato
from Modulos.ManejaEquipoMod import manejaequipo
from Modulos.ManejaJugadorMod import manejajugador


def menu():

    print("¿Qué desea hacer?\n")
    print("1_ Crear contrato para jugador\n")
    print("2_ Consultar jugadores contratados\n")
    print("3_ Consultar contratos que vencen en 6 meses\n")
    print("4_ Obtener importe total de contratos de un equipo\n")
    print("5_ Guardar en un archivo los contratos registrados\n")
    print("6_ Salir\n")

    return int(input())


if __name__ == "__main__":

    djugador1 = manejajugador()
    dequipo1 = manejaequipo()
    dcontrato1 = manejacontrato(djugador1, dequipo1)

    e=dcontrato1.contratos[2].getfechain()
    print(e)
    p=dcontrato1.contratos[1].getjugadordni()
    print("jugador dni: ", p)
    print("jugador coso que buscai: ", djugador1.jugadores[6].getdni())
    print(" ")
    print(dcontrato1.contratos.size)
    input()

    opcion = menu()
    
    while opcion != 6:
        os.system("CLS")

        if opcion == 1:
            dcontrato1.generaContrato(djugador1, dequipo1)

        if opcion == 2:
            dcontrato1.consultaJugadoresContrato()
        
        if opcion == 3:
            dequipo1.consultarContratosVencimiento()
        
        if opcion == 4:
            dequipo1.calcularImporteTotal()

        if opcion == 5:
            dcontrato1.guardarContratos()

        os.system("CLS")
        opcion = menu()

    os.system("CLS")
    print("\nPrograma finalizado...\n")
