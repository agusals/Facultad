class pedidos:
    __pedidonum: int
    __descripcion: str
    __cant: int
    __preciouni: int
    __pedidoestado: str

    def __init__(self, pn=-1, desc="ejemplo", cant=-1, pu=-1, pe="ejemplo"):
        self.__pedidonum = pn
        self.__descripcion = desc
        self.__cant = cant
        self.__preciouni = pu
        self.__pedidoestado = pe
    
    def getpedidoestado(self):
        return self.__pedidoestado

    def getpedidonum(self):
        return self.__pedidonum
    
    def getdesc(self):
        return self.__descripcion
    
    def getcant(self):
        return self.__cant

    def getpreciouni(self):
        return self.__preciouni
    
