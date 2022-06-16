from .CalefactoresMod import calefactor

class calefactorgas(calefactor):
    __calorias: int
    __matricula: str

    def __init__(self, costo=-1, marca="ejemplo", modelo="ejemplo", calorias=-1, matricula="ejemplo"):
        super().__init__(costo, marca, modelo)
        self.__calorias = calorias
        self.__matricula = matricula
    
    def gettipo(self):
        return "gas"

    def getcosto(self):
        return self._costo

    def getmarca(self):
        return self._marca

    def getmodel(self):
        return self._modelo

    def getcalorias(self):
        return self.__calorias

    def getmatricula(self):
        return self.__matricula