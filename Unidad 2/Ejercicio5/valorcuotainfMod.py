from PlanAhorroMod import PlanAhorro as pah
import os

class cuota:

    @classmethod
    def inf(cls, lista):
        valordado = int(input("Ingrese valor: "))
        os.system("CLS")
        print("------Autos con valor de cuota inferiores al valor dado: \n")
        print(" ")
        for pa in lista:
            valorcuota = (pa.getvalorauto()/pah.getcantcuo()) + pa.getvalorauto() * 0.1

            if valorcuota < valordado:
                pa.showvariables()
                print(" ")

        input()

    
    @classmethod
    def montolicitar(cls, lista):
        for pa in lista:
            valorcuota = (pa.getvalorauto()/pah.getcantcuo()) + pa.getvalorauto() * 0.1
            print("---Para licitar: \n")
            pa.showvariables()
            print("---Necesita ${}\n" .format(pa.getobjcuopagas()*valorcuota))
            print(" ")
        
        input()

    @classmethod
    def modificarcuopagas(cls, lista):
        codplandado = int(input("Ingrese Cod. Plan: "))
        os.system("CLS")
        e=0
        i=0
        while e != codplandado:
            print("{} ".format(i))
            if codplandado == lista[i].getcodplan():
                lista[i].setobjcuopagas(int(input("Ingrese nueva cant. de cuotas: ")))
                e=lista[i].getcodplan()
            i+=1
        os.system("CLS")
        input("Proceso terminado, presione cualquier tecla para continuar!")