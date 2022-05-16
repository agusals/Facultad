import os
from Modulos.pedidos_mod import pedidos as p
from Modulos.repartidores_mod import repartidores as r


class listador:

    @classmethod
    def lista(cls, pedidosarr, repartidoreslista):

        for rep in repartidoreslista:
            print("Apellido: {}                     Nombre: {}" .format(rep.getap(), rep.getnom()))
            print("Teléfono: {}                     Tipo Mov {}" .format(rep.gettele(), cls.__tipomov(rep)))
            print("N° pedido            Descripcion         Cantidad        Precio Unitario         Total\n")
            cls.__pedidolista(pedidosarr, rep.getid())
        cls.__importeacobrar()

    @classmethod
    def __pedidolista(cls, pedidosarr, idrep):
        for id in range(len(pedidosarr)):
            if id == idrep:
                for pedido in pedidosarr[id]:

                    print("{}           {}          {}          {}      " .format(pedido.getpedidonum(), pedido.getdesc(), pedido.getcant(), pedido.getpreciouni()))

    @classmethod
    def __importeacobrar(cls):
        pass

    @classmethod
    def __tipomov(cls, rep):

        if rep.getmov() == "B":
            return "Bicicleta"
        elif rep.getmov() == "M":
            return "Moto"
        else:
            return "Auto"
