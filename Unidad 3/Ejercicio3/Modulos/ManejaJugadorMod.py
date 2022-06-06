import csv
from .JugadorMod import jugador

class manejajugador:
    jugadores = []

    def __init__(self):
        archivo = open("Unidad 3/Ejercicio3/Jugadores.csv")
        reader = csv.reader(archivo, delimiter=";")

        for fila in reader:
            
            self.jugadores.append(jugador(fila[0],fila[1],fila[2],fila[3],fila[4]))
            
        archivo.close()

