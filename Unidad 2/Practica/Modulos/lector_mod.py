import csv
from Modulos.pedidos_mod import pedidos as p
from Modulos.repartidores_mod import repartidores as r

class Lector:

    def generapedidos(arr):
        archivo = open("Modulos/pedidos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)

        for fila in reader:
            print(arr[int(fila[0])-1])
            if arr[int(fila[0])-1] == None:
                arr[int(fila[0])-1] = []
            arr[int(fila[0])-1].append(p(int(fila[1]), str(fila[2]), int(fila[3]), int(fila[4]), str(fila[5])))
             
        archivo.close()

    def generarepartidores(lista):
        archivo = open("Modulos/repartidores.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
    
        for fila in reader:
            
            lista.append(r(int(fila[0]), str(fila[1]), str(fila[2]), int(fila[3]), str(fila[4]), int(fila[5])))
             
        archivo.close()