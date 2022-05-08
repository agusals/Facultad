from PlanAhorroMod import PlanAhorro as pah
import os

class actualizaValor:

    @classmethod
    def actualizador(cls, lista):

        for pa in lista:
            pa.showvariables()
            pa.setvalorauto(int(input("Actualizar valor vehiculo: ")))
            os.system("CLS")

        print("Valores actualizados!\n")
        input()
