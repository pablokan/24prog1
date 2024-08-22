from personaje import Personaje

class Monstruo(Personaje):
    def __init__(self, nombre: str, salud: int, poder: str):
        super().__init__(nombre, salud)
        self.poder = poder

    def atacar(self, rival: Personaje):
        if self.poder == 'fuego':
            rival.salud = 0
