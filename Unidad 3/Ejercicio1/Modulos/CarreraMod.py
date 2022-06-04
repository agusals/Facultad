class carrera:
    __cod: int
    __nom: str
    __fechainicio: str
    __dura: str
    __titulo: str

    def __init__(self, cod=-1, nom="ejemplo", fechainicio="ejemplo", dura="ejemplo", titulo="ejemplo"):
        self.__cod = cod
        self.__nom = nom
        self.__fechainicio = fechainicio
        self.__dura = dura
        self.__titulo = titulo

    def getnom(self):
        return self.__nom

    def getdura(self):
        return self.__dura

