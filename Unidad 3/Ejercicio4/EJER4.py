import os
from Modulos.ColeccionCalefactoresMod import coleccioncalefactores as colcal

if __name__ == "__main__":

    os.system("CLS")

    a = input("Ingrese tamaño del arreglo: ")

    os.system("CLS")

    col = colcal(int(a))

    col.baratogas()

    col.baratoelec()