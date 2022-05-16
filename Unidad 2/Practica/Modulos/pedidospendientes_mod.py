import os
from Modulos.pedidos_mod import pedidos as p

class pedidospendientes:

    @classmethod
    def obtener(cls, pedidosarr):
        rep = input("Ingrese id repartidor: ")
        os.system("CLS")
        print("Pedidos pendientes de entrega:\n")
        for i in range(len(pedidosarr)):
            e = i+1
            #print(e)
            if e == int(rep):
                for pedido in pedidosarr[i]:
                    if pedido.getpedidoestado()  == "N":
                        print(pedido.getpedidonum())