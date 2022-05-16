class repartidores:
    __id: int
    __ap: str
    __nom: str
    __tele: int
    __tipomov: str
    importecomision = 0

    def __init__(self, id=-1, ap="ejemplo", nom="ejemplo", tele=-1, tipomov="ejemplo", impcom = 0):
        self.__id = id
        self.__ap = ap
        self.__nom = nom
        self.__tele = tele
        self.__tipomov = tipomov
        self.importecomision = impcom
    
    def getid(self):
        return self.__id

    def getap(self):
        return self.__ap

    def getnom(self):
        return self.__nom
    
    def getmov(self):
        return self.__tipomov
    
    def gettele(self):
        return self.__tele
