class Email:
    __idcuenta = "-"
    __dominio = "-"
    __tipodom = "-"
    __contra = "-"
    def __init__(self, idcuenta="ejemplo", dominio= "mail", tipodom= "ej", contra= "ejemplo"):
        self.__idcuenta = idcuenta
        self.__dominio = dominio
        self.__tipodom = tipodom
        self.__contra = contra
    def retornaEmail(self) -> str:
        return self.__idcuenta + "@" + self.__dominio + "." + self.__tipodom
    def getDominio(self) -> str:
        return self.__dominio
    def getContra(self) -> str:
        return self.__contra
    def setContra(self, nuevacon):
        self.__contra = nuevacon
        print("\nContraseña guardada!\n")
    def getIDcuenta(self) -> str:
        return self.__idcuenta
    def crearCuenta(self, mail: str, confirm: bool):
        self.__idcuenta = mail.split('@')[0]
        domycom = mail.split('@')[1]
        self.__dominio = domycom.split('.')[0]
        self.__tipodom = domycom.split('.')[1]
        if confirm:
            print("Direccion registrada!\n")