class ramo:
    __tamano: str
    __flores= None

    def __init__(self, tamano= "ejemplo"):
        self.__tamano = tamano
        self.__flores = []

    def agregarflor(self, flor):
        self.__flores.append(flor)

    def escribeflor1(self):
        self.__flores[0].printflor()