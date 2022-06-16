from zope.interface import Interface
from zope.interface import implementer

class IPosicionador(Interface):

    def insertarElemento(objeto):
        pass

    def agregarElemento(objeto):
        pass

    def mostrarElemento(posicion):
        pass