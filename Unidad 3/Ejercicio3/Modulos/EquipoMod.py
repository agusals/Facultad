class equipo:
    __nom: str
    __ciudad: str
    __contratos=None

    def __init__(self, nom="ej", ciudad="ej"):
        self.__nom = nom
        self.__ciudad = ciudad
        self.__contratos = []

    def getnom(self):
        return self.__nom

    def getcontratos(self):
        return self.__contratos

    def setcontrato(self, contrato):
        self.__contratos.append(contrato)