import csv
import os
from Modulos.FacultadMod import facultad
from Modulos.CarreraMod import carrera 

class manejafacultades:
    facultades = []

    @classmethod
    def __init__(cls):
        archivo = open("Unidad 3/Ejercicio1/Facultades.csv", encoding='utf8')
        reader = csv.reader(archivo, delimiter=",")

        indice = -1

        for fila in reader:
            
            try:
                carreracod = int(fila[1])

            except ValueError:
                print("No hay carrera, cargando nueva facultad! ", fila[0], "\n\n")

                indice = int(fila[0])
                print("indice: ",indice)

                cls.facultades.append(facultad(fila[0], fila[1], fila[2], fila[3], fila[4]))
                

                
            else:
                print("Carrera ",fila[1]," detectada! Cargando...\n\n")

                carreraleida = carrera(carreracod, fila[2], fila[3], fila[4], fila[5])


                cls.facultades[indice-1].cargarCarrera(carreraleida)

      
             
        archivo.close()

        print("COMPLETADO!\n")

    @classmethod
    def opcionuno(cls):
        

        codingresed = input("Ingrese codigo de facultad: ")

        os.system("CLS")

        for facultad in cls.facultades:
            if facultad.getcod() == codingresed:
                print(facultad.getnom())
                print(" ")
                carrerax = facultad.getcarreras()
                for carrera in carrerax:
                    print("/////// {} - Duración: {} \n" .format(carrera.getnom(), carrera.getdura()))

        input()
                
    @classmethod
    def opciondos(cls):

        nomingresed = input("Ingrese nombre de la carrera: ")
        nomingresed = nomingresed.lower()

        os.system("CLS")

        i = 0
        o = 0
        facultadcod = -1
        carreracod = -1
        encontrado = False
        
        while i < 2 and encontrado == False:
            carreras = cls.facultades[i].getcarreras()
            o = 0
            while encontrado == False and o != len(carreras):

                if carreras[o].getnom().lower() == nomingresed:
                    
                    facultadcod = i + 1
                    carreracod = o + 1
                    encontrado = True
                          
                o+=1

            i+=1

        print("Código de facultad: {} \n\nCódigo de carrera: {}\n" .format(facultadcod, carreracod))
        nombrefacu = cls.facultades[facultadcod-1].getnom()
        localidadfacu = cls.facultades[facultadcod-1].getloc()
        print("Nombre de la facultad: {} \n\nLocalidad: {}\n" .format(nombrefacu, localidadfacu))
        input()