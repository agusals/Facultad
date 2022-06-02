class flor:
    __num : int
    __nombre: str
    __color: str
    __desc: str

    def __init__(self, num=-1, nombre="ejemplo", color="ejemplo", desc="ejemplo"):
        self.__num = num
        self.__nombre = nombre
        self.__color = color
        self.__desc = desc

    def printflor(self):
        print(self.__nombre, "\n")