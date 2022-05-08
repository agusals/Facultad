class ViajeroFrecuente:
    __num_viajero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millas_acum: int

    def __init__(self, num_viajero=-1, dni= "ejemplo", nombre="ejemplo", apellido="ejemplo", millas_acum=0):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def __gt__(self, otro):
        if type(self) == type(otro):
            return self.__millas_acum > otro.cantidadTotalMillas()
        if type(otro) == int:
            return self.__millas_acum > otro

    def __eq__(self, otro):
        return self.__millas_acum == otro

    def __add__(self, otro):
        if type(self) == type(otro):
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()+otro.cantidadTotalMillas())
        if type(otro) == int:
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()+otro)

    def __radd__(self, otro):
        if type(self) == type(otro):
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()+otro.cantidadTotalMillas())
        if type(otro) == int:
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()+otro)

    def __sub__(self, otro):
        if type(self) == type(otro):
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()-otro.cantidadTotalMillas())
        if type(otro) == int:
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()-otro)
        
    def __rsub__(self, otro):
        if type(self) == type(otro):
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()-otro.cantidadTotalMillas())
        if type(otro) == int:
            return ViajeroFrecuente(millas_acum = self.cantidadTotalMillas()-otro)
    

    def cantidadTotalMillas(self) -> int:
        return self.__millas_acum

    def acumularMillas(self, millas: int) -> int:
        self.__millas_acum += millas
        return self.__millas_acum
    
    def canjearMillas(self, millas: int) -> int:
        if millas <= self.__millas_acum:
            self.__millas_acum -= millas
            print("Millas canjeadas!\n")
            return self.__millas_acum
        else:
            print("Error! No se pudo canjear\n")

    def getNumviajero(self) -> int:
        return self.__num_viajero

    
        
        
        