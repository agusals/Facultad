class Registro:
    __temp: int
    __humedad: int
    __presion: int

    def __init__(self, temp=0, hum=0, pre=0):
        self.__temp = temp
        self.__humedad = hum
        self.__presion = pre

    def gettemp(self) -> int:
        return int(self.__temp)
    
    def gethum(self) -> int:
        return int(self.__humedad)

    def getpresion(self) -> int:
        return int(self.__presion)