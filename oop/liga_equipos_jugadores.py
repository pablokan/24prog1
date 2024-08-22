class Liga:
    def __init__(self) -> None:
        self.river = Equipo('River', ['Acuña', 'Meza'])
        self.boca = Equipo('Boca', ['Cavani'])

class Equipo:
    def __init__(self, nombre, jugadores) -> None:
        self.nombre = nombre
        self.jugadores = [Jugador(j) for j in jugadores]

class Jugador:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

liga = Liga()
print(liga.river.jugadores[1].nombre)
print(liga.boca.jugadores[0].nombre)