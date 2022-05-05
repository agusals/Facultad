import imp
import os
from Lector import Lector as l
from Reg import Registro as r
from MaxMin import maximini as mm
from Prom import promedio 
from ListarPorDia import listador

def menu() -> int:
    print("¿Qué desea hacer?\n")
    print("1_ Mostrar para cada variable el día y hora de menor y mayor valor\n")
    print("2_ Indicar la temperatura promedio mensual por cada hora\n")
    print("3_ Listar los valores de las tres variables para cada hora del día dado\n")
    print("4_ Salir\n")

    
    return int(input())

def maximo() -> float:
    maximo: float

if __name__ == "__main__":

    os.system("CLS")

    arr = [["-"]*24 for _ in range(30)]
    l.generarLista(arr)


    opcion = menu()
    while opcion != 4:
        os.system("CLS")

        if opcion == 1:
            pepe = mm()
            valores = pepe.maximo(arr)
            valmin = pepe.minimo(arr)
            print(valores)
            print(valmin)
            input()
                            
        elif opcion == 2:
            pepe = promedio()
            print("Promedio mensual: %.2f" % pepe.tempPromedio(arr))
            input()

        elif opcion == 3:
            dianum = input("Ingrese día: ")
            os.system("CLS")
            pepe = listador()
            pepe.listar(arr, int(dianum))
            input()


        os.system("CLS")
        opcion = menu()
    
    os.system("CLS")
    print("\nPrograma finalizado...\n")