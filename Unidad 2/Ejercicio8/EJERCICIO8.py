import os
from ConjuntoMod import Conjunto as conj

def menu():

    print("¿Qué desea hacer?\n")
    print("1_ Unir dos conjuntos\n")
    print("2_ Diferencia de dos conjuntos\n")
    print("3_ Verficar equivalencia entre conjuntos\n")
    print("4_ Salir\n")

    return int(input())


if __name__ == "__main__":

    os.system("CLS")

    A = {1,2,3,4}
    B = {3,6,9}

    a1 = conj(A)
    b1 = conj(B)

    opcion = menu()
    while opcion != 4:
        os.system("CLS")

        if opcion == 1:
            print("A = {}\n" .format(A))
            print("B = {}\n" .format(B))
            C = a1 + b1
            print("A + B = {}" .format(C.get()))
            input()

        if opcion == 2:
            print("A = {}\n" .format(A)) 
            print("B = {}\n" .format(B))
            C = a1 -b1
            print("A - B = {}" .format(C.get()))
            input()

        if opcion == 3:
            print("A = {}\n" .format(A)) 
            print("B = {}\n" .format(B))
            C = a1 == b1
            print("A == B = {}" .format(C))
            input()

        os.system("CLS")
        opcion = menu()
    
    os.system("CLS")
    print("\nPrograma finalizado...\n")
    


