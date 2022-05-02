class Ventana:

    __titulo: str
    __x_supi: int
    __y_supi: int
    __x_infd: int
    __y_infd: int

    def __init__(self, ti="ej", xsi=0, ysi=0, xid=0, yid=0):
        self.__titulo=ti
        if xsi < 0 and xsi > xid:
            print("Error! N° menor a 0 y/o mayor a X de inf. der\n")
            return
        if ysi < 0 and ysi > yid:
            print("Error! N° menor a 0 y/o mayor a Y de inf. der\n")
            return
        self.__x_supi=xsi
        self.__y_supi=ysi
        self.__x_infd=xid
        self.__y_infd=yid

    def mostrar(self):
        print("Título: ", self.__titulo)
        print("\nX sup. izq.: ", self.__x_supi)
        print("\nY sup. izq.: ", self.__y_supi)
        print("\nX inf. der.: ", self.__x_infd)
        print("\nY inf. der.: ", self.__y_infd)

    def getTitulo(self) ->str:
        return self.__titulo

    def alto(self) ->int:
        return self.__y_infd

    def ancho(self) ->int:
        return self.__x_infd

    def moverDerecha(self, mo=0):
        mor=round(mo)

        self.__x_infd += mor
        self.__x_supi += mor

    def moverIzquierda(self, mo=0):
        mor=round(mo)

        self.__x_infd -= mor
        self.__x_supi -= mor

    def bajar(self, mo=0):
        mor=round(mo)

        self.__y_infd -= mor
        self.__y_supi -= mor

    def subir(self, mo=0):
        mor=round(mo)

        self.__y_infd += mor
        self.__y_supi += mor
    
