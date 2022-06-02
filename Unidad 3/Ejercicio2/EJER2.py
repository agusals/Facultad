import os
from Modulos.ManejaRamosMod import manejaramos
from Modulos.ManejaFloresMod import manejaflores

if __name__ == "__main__":

    os.system("CLS")
    floresdriver1 = manejaflores()
    ramosdriver1 = manejaramos(floresdriver1)

    os.system("CLS")
    ramosdriver1.holacomotas()

