class PlanAhorro:
    __codplan: int
    __modelo: str
    __ver: str
    __valor: int
    __cantcuo=0
    __cantcuopagas=0

    def __init__(self, codp=0, modl="ejemplo", ver="ejemplo", valor=0):
        self.__codplan = codp
        self.__modelo = modl
        self.__ver = ver
        self.__valor = valor

    def showvariables(self):
        print("Cod.plan: {}\n" .format(self.__codplan))
        print("Modelo: {}\n" .format(self.__modelo))
        print("Version: {}\n" .format(self.__ver))

    def getcodplan(self):
        return self.__codplan

    def getvalorauto(self):
        return self.__valor

    def setvalorauto(self, valve:int):
        self.__valor = valve

    def getobjcuopagas(self):
        return self.__cantcuopagas

    def setobjcuopagas(self, num:int):
        self.__cantcuopagas = num

    @classmethod
    def setcantcuo(cls, num:int):
        cls.__cantcuo = num

    @classmethod
    def setcantcuopagas(cls, num:int):
        cls.__cantcuopagas = num

    @classmethod
    def getcantcuo(cls):
        return cls.__cantcuo

    @classmethod
    def getcantcuopagas(cls):
        return cls.__cantcuopagas
