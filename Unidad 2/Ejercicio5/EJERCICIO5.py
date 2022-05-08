import os
from Lector import Lectorcsv as lec
from PlanAhorroMod import PlanAhorro as pah
from ActualizaValorVehiculoMod import actualizaValor as actval
from valorcuotainfMod import cuota as cuo


def menu() -> str:
    print("¿Qué desea hacer?\n")
    print("a_ Actualizar el valor del vehículo de cada plan\n")
    print("b_ Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado\n")
    print("c_ Mostrar el monto que se debe haber pagado para licitar el vehículo\n")
    print("d_ Modificar la cantidad de cuotas que se debe tener pagas para licitar\n")
    print("e_ Salir\n")

    
    return str(input())

if __name__ == "__main__":

    os.system("CLS")

    listauto = []

    lec.generarLista(listauto)


    opcion = menu()

    while opcion != 'e':
        os.system("CLS")

        if opcion == 'a':
            actval.actualizador(listauto)

        if opcion == "b":
            cuo.inf(listauto)
        
        if opcion == "c":
            cuo.montolicitar(listauto)

        if opcion == "d":
            cuo.modificarcuopagas(listauto)
        
        os.system("CLS")
        opcion = menu()
    
    os.system("CLS")
    print("\nPrograma finalizado...\n")