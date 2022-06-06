class jugador:
    __nom: str
    __dni: int
    __ciunatal: str
    __paisorigen: str
    __fechanac: str

    def __init__(self, nom="ej", dni=-1, ciunatal="ej", paisorigen="ej", fechanac="ej"):

        self.__nom = nom
        self.__dni = dni
        self.__ciunatal = ciunatal
        self.__paisorigen = paisorigen
        self.__fechanac = fechanac


    def getdni(self):
        return self.__dni

    def __str__(self) -> str:
        lestring = "Jugador: {}\nDNI: {}\nCiudad Natal: {}\nPais de origen: {}\nFecha de nacimiento: {}\n" .format(self.__nom, self.__dni, self.__ciunatal, self.__paisorigen, self.__fechanac)
        return lestring