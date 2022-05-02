import os
from lectorcsv import Lector 
from viajeromod import ViajeroFrecuente as vf


def menu() -> str:
    print("¿Qué desea hacer?\n")
    print("a_ Consultar cant millas\n")
    print("b_ Acumular millas\n")
    print("c_ Canjear millas\n")
    print("d_ Salir\n")

    
    return str(input())

if __name__ == "__main__":

    os.system("CLS")

    listaviajeros = []

    Lector.generarLista(listaviajeros)

    input()
    
    inp = int(input("Ingrese n° de viajero: "))
    viajerocorrecto = vf()
    for viajero in listaviajeros:
        print(viajero)
        if viajero.getNumviajero == inp:
            
            viajerocorrecto = viajero

    input()
    opcion = menu()
    while opcion != 'd':
        os.system("CLS")
        if opcion == 'a':
            print("Millas acumuladas: ", viajerocorrecto.cantidadTotalMillas())
            input()
        if opcion == 'b':
            acum = viajerocorrecto.acumularMillas(int(input("Ingrese millas a acumular: ")))
            print("Millas acumuladas actualizadas = ", acum)
            input()
        if opcion == 'c':
            millas = viajerocorrecto.canjearMillas(int(input("Ingrese millas a canjear: ")))
            print("Millas acumuladas actualizadas = ", millas)
            input()

        os.system("CLS")
        opcion = menu()
    
    os.system("CLS")

    print("Lista cargada con 4 viajeros: ", hex(id(listaviajeros)))