class facultad:
    __cod: int
    __nom: str
    __dir: str
    __loc: str
    __tel: str
    __carreras: None

    def __init__(self, cod=-1, nom="ejemplo", dir="ejemplo", loc="ejemplo", tel="ejemplo"):
        self.__cod = cod
        self.__nom = nom
        self.__dir = dir
        self.__loc = loc
        self.__tel = tel
        self.__carreras = []

    def cargarCarrera(self, carrera):
        self.__carreras.append(carrera)

    def getcod(self):
        return self.__cod

    def getnom(self):
        return self.__nom
    
    def getloc(self):
        return self.__loc

    def getcarreras(self):
        return self.__carreras
    
        