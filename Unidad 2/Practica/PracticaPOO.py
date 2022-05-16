import os
import numpy as np
from Modulos.pedidos_mod import pedidos as p
from Modulos.repartidores_mod import repartidores as r
from Modulos.lector_mod import Lector as lec
from Modulos.pedidospendientes_mod import pedidospendientes
from Modulos.listador_mod import listador

def menu():

    print("¿Qué desea hacer?\n")
    print("1_ Obtener pedidos pendientes de entrega\n")
    print("2_ Imprimir listado con pedidos entregados de cada repartidor\n")
    print("3_ Determinar repartidores repetidos\n")
    print("4_ Obtener listado de repartidores ordenado por el importe a cobrar (de mayor a menor)\n")
    print("5_ Salir\n")

    return int(input())

if __name__ == "__main__":
    
    repartidoreslista = []
    pedidosarr = np.empty([6], dtype=p)

    lec.generarepartidores(repartidoreslista)
    lec.generapedidos(pedidosarr)
    
    os.system("CLS")
    opcion = menu()
    while opcion != 5:
        os.system("CLS")

        if opcion == 1:
            pedidospendientes.obtener(pedidosarr)
            input()

        if opcion == 2:
            listador.lista(pedidosarr, repartidoreslista)
            input()

            
        if opcion == 3:
            for ped in pedidosarr[0]:
                print(ped)
            input()

        if opcion == 4:
            pass

        os.system("CLS")
        opcion = menu()
    
    os.system("CLS")
    print("\nPrograma finalizado...\n")

