from .CalefactoresMod import calefactor

class calefactorelectrico(calefactor):
    __potmax: int

    def __init__(self, costo=-1, marca="ejemplo", modelo="ejemplo", potenciamax=-1):
        super().__init__(costo, marca, modelo)
        self.__potmax = potenciamax

    def gettipo(self):
        return "electrico"

    def getcosto(self):
        return self._costo

    def getmarca(self):
        return self._marca

    def getmodel(self):
        return self._modelo

    def getpotmax(self):
        return self.__potmax
