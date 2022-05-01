import os
import re

def menu():
    print("¿Qué desea hacer?\n")
    print("1_ Ingresar email\n")
    print("2_ ")

class Email:
    __idcuenta = "-"
    __dominio = "-"
    __tipodom = "-"
    __contra = "-"
    def __init__(self):
        self.__idcuenta = "ejemplo"
        self.__dominio = "ejemplo"
        self.__tipodom = "ejemplo"
        self.__contra = "no asignado"
    def retornaEmail(self):
        return self.__idcuenta + "@" + self.__dominio + "." + self.__tipodom
    def getDominio(self):
        return self.__dominio
    def crearCuenta(self, mail):
        self.__idcuenta = mail.split('@')[0]
        domycom = mail.split('@')[1]
        self.__dominio = domycom.split('.')[0]
        self.__tipodom = domycom.split('.')[1]

        
        

if __name__ == "__main__":
    os.system("CLS")
    emailobj = Email()
    print(emailobj.retornaEmail())

    a = "papa.ola,soy1una7string ¿loca"
    b = re.split(',|1|7| ¿|\.', a)
    print(a)
    print("")
    print(b)
    print("")
    emailobj.crearCuenta("elpepe.etesech@robertinsky.com")
    print(emailobj.retornaEmail())
