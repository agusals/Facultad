import csv
from Modulos.CamaMod import Cama
from Modulos.MedicamentosMod import Medicamento

class Lector:

    def generarlistacamas(arr):
        archivo = open("Unidad 2/EjercicioIntegrador/camas.csv")
        reader = csv.reader(archivo, delimiter=";", skipinitialspace=True)
        next(reader)
    
        for fila in reader:
            
            arr[int(fila[0])-1] = Cama(int(fila[1]), bool(fila[2]), str(fila[3]), str(fila[4]), str(fila[5]), str(fila[6]))
             
        archivo.close()

    def generarlistamedicamentos(lista):
        archivo = open("Unidad 2/EjercicioIntegrador/medicamentos.csv")
        reader = csv.reader(archivo, delimiter=";", skipinitialspace=True)
        next(reader)
    
        for fila in reader:
            
            lista.append(Medicamento(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), str(fila[4]), int(fila[5]), int(fila[6])))
             
        archivo.close()