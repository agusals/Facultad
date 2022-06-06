class contrato:
    __fechainicio: str
    __fechafin: str
    __pagomens: int
    __jugador=None
    __equipo=None

    def __init__(self, fechain="ej", fechaend="ej", pagomens=-1, jugador=None, equipo=None):

        self.__fechainicio = fechain
        self.__fechafin = fechaend
        self.__pagomens = pagomens
        self.__jugador = jugador
        self.__equipo = equipo

    def getfechain(self):
        return self.__fechainicio

    def getjugadordni(self) -> int:
        return self.__jugador.getdni()

    def getequiponom(self):
        return self.__equipo.getnom()

    def getfechaend(self):
        return self.__fechafin

    def getjugador(self):
        return self.__jugador
    
    def getpagomens(self):
        return self.__pagomens

