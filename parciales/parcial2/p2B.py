class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def descAnimal(self):
        return f"{self.nombre} tiene {self.edad} años"

class Perro(Animal):
    def __init__(self, nombre, edad, raza, colorCollar, materialCollar):
        super().__init__(nombre, edad)
        self.raza = raza
        self.collar = Collar(colorCollar, materialCollar)

    def moverCola(self, velocidad):
        self.velocidad = velocidad
        return "contento" if velocidad == 'rápido' else 'triste'

    def descrPerro(self):
        return f'{self.descAnimal()}, es un {self.raza} que lleva un {self.collar.descrCollar()} y está {self.moverCola(self.velocidad)}.'

class Collar:
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def descrCollar(self):
        return f"collar {self.color} de {self.material}"

bobbie = Perro('Bobbie', 3, 'rottweiler', 'rojo', 'cuero')
bobbie.moverCola('ni la mueve')
toffee = Perro('Toffee', 5, 'ovejero alemán', 'negro', 'tela')    
toffee.moverCola('rápido')

print(bobbie.descrPerro())
print(toffee.descrPerro())
