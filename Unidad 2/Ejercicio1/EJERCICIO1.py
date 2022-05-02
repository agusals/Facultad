import os
import csv
from emailmod import Email as e

def menu() -> int:
    print("¿Qué desea hacer?\n")
    print("1_ Ingresar email\n")
    print("2_ Cambiar contraseña\n")
    print("3_ Registrar email\n")
    print("4_ Leer archivo\n")
    print("5_ Salir\n")

    
    return int(input())

def opcion1(lista):
    nombreuser = input("Ingrese nombre del usuario: ")
    os.system("CLS")
    idcuenta = input("Ingrese identificador de cuenta: ")
    os.system("CLS")
    dominio = input("Ingrese dominio: ")
    os.system("CLS")
    tipodominio = input("Ingrese tipo de dominio: ")
    os.system("CLS")
    contra = input("Ingrese contraseña: ")
    os.system("CLS")
    
    email = e(idcuenta, dominio, tipodominio, contra)
    lista.append(email)

    print("Estimado {}, te enviaremos tus mensajes a la dirección {}.".format(nombreuser, email.retornaEmail()))
    input()

def opcion2(lista):
    contraxd = input("Ingrese contraseña: ")
    if contraxd == lista[0].getContra():
        print("Contraseña correcta!\n")
        contranueva = input("Ingrese nueva contraseña:")
        lista[0].setContra(contranueva)

        input()

def opcion3(lista):
    
    emailnuevo = str(input("Ingrese dirección de correo: "))
    email = e()
    lista.append(email.crearCuenta(emailnuevo))
    input()

def opcion4(listacsv):
    archivo = open("Unidad 2\Ejercicio1\cuentas.csv")
    reader = csv.reader(archivo, delimiter=",", skipinitialspace=True)
    
    for fila in reader:
        for i in range(len(fila)):
            listacsv.append(e())
        for i in range(len(fila)):
            mail = fila[i]
            #print(fila[i]) 
            #correoobj = e()
            listacsv[i].crearCuenta(str(mail), False)
             
        
    archivo.close()

    idcuenta = input("Ingrese identificador de cuenta a buscar: ")
    print(" ")
    for i in range(len(listacsv)):
        if listacsv[i].getIDcuenta() == idcuenta:
            print("id de cuenta repetido!!\n")
    input()
        
if __name__ == "__main__":
    os.system("CLS")
    respuesta = menu()
    lista = []
    listacsv = []

    while respuesta != 5:
        os.system("CLS")
        if respuesta == 1:
            opcion1(lista)
        elif respuesta == 2:
            opcion2(lista)
        elif respuesta == 3:
            opcion3(lista)
        elif respuesta == 4:
            opcion4(listacsv)
    
        os.system("CLS")
        respuesta = menu()
    
    os.system("CLS")
    print("Programa finalizado.")


    """
    emailobj = e("a","b","c","d")
    print(emailobj.retornaEmail())

    a = "papa.ola,soy1una7string ¿loca"
    b = re.split(',|1|7| ¿|\.', a)
    print(a)
    print("")
    print(b)
    print("")
    emailobj.crearCuenta("elpepe.etesech@robertinsky.com")
    print(emailobj.retornaEmail())
    """

#holae