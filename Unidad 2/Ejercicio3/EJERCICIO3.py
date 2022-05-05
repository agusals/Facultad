import imp
import os
from Lector import Lector as l
from Reg import Registro as r


def menu() -> int:
    print("¿Qué desea hacer?\n")
    print("1_ Consultar cant millas\n")
    print("2_ Acumular millas\n")
    print("3_ Canjear millas\n")
    print("4_ Salir\n")

    
    return int(input())
if __name__ == "__main__":

    os.system("CLS")

    arr = [[""]*24 for _ in range(30)]
    l.generarLista(arr)
    print(arr)

    opcion = menu()
    while opcion != 4:
        os.system("CLS")

        if opcion == 1:
            tempmax = -1
            tempmin = 999999
            hummax = -1
            hummin = 999999
            presmax = -1
            presmin = 999999

            for i in range(30):
                for o in range(24):
                    if arr[i][o] == r():
                        if arr[i][o].gettemp() < tempmin:
                            tempmin = arr[i][o].gettemp()
                        
                        
        if opcion == 2:

        if opcion == 3:

        os.system("CLS")
        opcion = menu()