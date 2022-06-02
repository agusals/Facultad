from Modulos.ManejaFloresMod import manejaflores
from Modulos.RamoMod import ramo

class manejaramos:
    ramosvendidos = []
    __florvendidas = None

    def __init__(self, floresarr):

        ramosize = input("Ingrese tamaño del ramo vendido: ")

        ramoide = ramo(ramosize)

        self.__florvendidas = []
        
        salir = False
        cont = 0
        while salir != True and cont < 4:
            numflor = input("Ingrese número de flor {}/4 (Escriba x para no ingresar mas)" .format(cont+1))
            if numflor.lower() == "x":
                salir = True
            else:
                ramoide.agregarflor(floresarr.flores[int(numflor)-1])

        self.ramosvendidos.append(ramoide)

    def holacomotas(self):
        self.ramosvendidos[0].escribeflor1()
        