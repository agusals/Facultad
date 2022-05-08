import os
from lectorcsv import Lector 



if __name__ == "__main__":

    os.system("CLS")

    lista = []

    Lector.generarLista(lista)

    mayor = -9999

    for via in lista:
        if via > mayor:
            mayor = via.cantidadTotalMillas()
        
    print("Mayor cant millas es: {}" .format(mayor))
    input()
    os.system("CLS")

    print("Cantidad de millas acum. iniciales del viajero n°{} es {}\n" .format(lista[0].getNumviajero(), lista[0].cantidadTotalMillas()))
    input("Toque cualquier tecla para sumar 600 millas: ")
    print(" ")
    print("-----------")
    via0 = lista[0]
    via0 = via0 + 600
    print("Cant total de millas acum. de la instancia actual es {}" .format(via0.cantidadTotalMillas()))
    input()
    os.system("CLS")

    print("Cantidad de millas acum. iniciales del viajero n°{} es {}\n" .format(lista[0].getNumviajero(), lista[0].cantidadTotalMillas()))
    input("Toque cualquier tecla para canjear 400 millas: ")
    print(" ")
    print("-----------")
    via0 = lista[0]
    via0 = via0 - 400
    print("Cant total de millas acum. de la instancia actual es {}" .format(via0.cantidadTotalMillas()))
    input()
    os.system("CLS")

    print("\nPrograma finalizado...\n")