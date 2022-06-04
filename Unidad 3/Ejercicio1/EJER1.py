import os
from Modulos.ManejaFacultadesMod import manejafacultades

def menu():

    print("¿Qué desea hacer?\n")
    print("1_ Ingresar cod facultad para mostrar nombre y duracion de las carreras\n")
    print("2_ Ingresar nombre de carrera para mostrar codigo de facultad y carrera y el nombre y localidad de la facultad donde se ubica\n")
    print("3_ Salir\n")

    return int(input())


if __name__ == "__main__":

    manejafacultades()

    opcion = menu()
    while opcion != 3:
        os.system("CLS")

        if opcion == 1:
            manejafacultades.opcionuno()

        if opcion == 2:
            manejafacultades.opciondos()

        os.system("CLS")
        opcion = menu()

    os.system("CLS")
    print("\nPrograma finalizado...\n")