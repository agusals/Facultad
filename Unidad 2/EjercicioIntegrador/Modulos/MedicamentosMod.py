class Medicamento:
    __idcama: int
    __idmed: id
    __nomco: str
    __mono: str
    __pres: str
    __cantap: int
    __precioto: int

    def __init__(self, idc=-1, idm=-1, nc="ejemplo", mono="ejemplo", pres="ejemplo", cantap=-1, preciot=-1):
        self.__idcama = idc
        self.__idmed = idm
        self.__nomco = nc
        self.__mono = mono
        self.__pres = pres
        self.__cantap = cantap
        self.__precioto = preciot

    def getidcama(self):
        return self.__idcama
    def getnomco(self):
        return self.__nomco
    def getmono(self):
        return self.__mono
    def getpres(self):
        return self.__pres
    def getcantap(self):
        return self.__cantap
    def getprecio(self):
        return self.__precioto
