import os
import numpy as np
import Modulos.LectorMod as lec
import Modulos.CamaMod as c
from Modulos.Listador import Listador as listador


if __name__ == "__main__":

    camas = np.empty([30], dtype=c.Cama)
    med = []

    lec.Lector.generarlistacamas(camas)
    lec.Lector.generarlistamedicamentos(med)

    

    os.system("CLS")
    nya = input("Ingrese nombre y apellido: ")
    os.system("CLS")

    listador.listardatos(med, camas, nya)

    os.system("CLS")
    diag = input("Ingrese diagnostico: ")
    os.system("CLS")

    listador.listarpordiag(med, camas, diag)

    os.system("CLS")
    print("\nPrograma finalizadont...\n")