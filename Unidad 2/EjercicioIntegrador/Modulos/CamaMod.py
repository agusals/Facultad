class Cama:
    __hab: int
    __estado: bool
    __nya: str
    __diag: str
    __fechain: str
    __fechaalt: str

    def __init__(self, h=-1, es=False, na="None", diag="ejemplo", fein="ejemplo", fealt="ejemplo"):
        self.__hab = h
        self.__estado = es
        self.__nya = na
        self.__diag = diag
        self.__fechain = fein
        self.__fechaalt = fealt

    def gethab(self):
        return self.__hab
    def getestado(self):
        return self.__estado
    def getnya(self):
        return self.__nya
    def getdiag(self):
        return self.__diag
    def getfechain(self):
        return self.__fechain