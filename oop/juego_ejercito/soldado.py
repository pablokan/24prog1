from personaje import Personaje

class Soldado(Personaje):
    def __init__(self, nombre: str, salud: int, fuerza: int):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self, rival: Personaje):
        rival.salud -= 20
