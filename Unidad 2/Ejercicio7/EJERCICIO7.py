import os
from lectorcsv import Lector


if __name__ == "__main__":

    os.system("CLS")

    lista = []

    Lector.generarLista(lista)

    obj = lista[0]
    
    
    print("Comparar cant millas acum del viajero n°{} (son {} millas) con valor ingresado:\n" .format(obj.getNumviajero(), obj.cantidadTotalMillas()))
    i = input("Ingrese valor: ")
    comp = int(i) == obj
    print(" \n ---------")
    if comp:
        print("Los valores son iguales!\n")

    else:
        print("Los valores son diferentes!\n")
    
    input()
    os.system("CLS")

    print("Cantidad de millas acum. iniciales del viajero n°{} es {}\n" .format(lista[0].getNumviajero(), lista[0].cantidadTotalMillas()))
    input("Toque cualquier tecla para sumar 600 millas: ")
    print(" ")
    print("-----------")
    via0 = lista[0]
    via0 = 600 + via0
    print("Cant total de millas acum. de la instancia actual es {}" .format(via0.cantidadTotalMillas()))
    input()
    os.system("CLS")

    print("Cantidad de millas acum. iniciales del viajero n°{} es {}\n" .format(lista[0].getNumviajero(), lista[0].cantidadTotalMillas()))
    input("Toque cualquier tecla para canjear 400 millas: ")
    print(" ")
    print("-----------")
    via0 = lista[0]
    via0 = 400 - via0
    print("Cant total de millas acum. de la instancia actual es {}" .format(via0.cantidadTotalMillas()))
    input()
    os.system("CLS")

    print("\nPrograma finalizado...\n")