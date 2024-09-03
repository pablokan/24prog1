class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def descripcionAnimal(self):
        return f"{self.nombre} tiene {self.edad} años"

class Perro(Mascota):
    def __init__(self, nombre, edad, raza, colorCollar, materialCollar):
        super().__init__(nombre, edad)
        self.raza = raza
        self.collar = Collar(colorCollar, materialCollar)
        self.estado = 'neutro de ánimo hasta que no mueva la cola'

    def mueveCola(self, velocidad):
        self.estado =  'contento' if velocidad == 'rápido' else 'triste'

    def descripcion(self):
        return f"{self.descripcionAnimal()}, es un {self.raza} que lleva un collar {self.collar.color} de {self.collar.material} y está {self.estado}."

class Collar:
    def __init__(self, color, material) -> None:
        self.color = color
        self.material = material

class Gato(Mascota):
    def __init__(self, nombre, edad, sexo, color):
        super().__init__(nombre, edad)
        self.sexo = sexo
        self.color = color
        self.estado = 'no sé si tiene hambre aún'

    def siMaulla(self, maulla):
        self.estado = 'tiene hambre' if maulla=='maulla' else "no tiene hambre"

    def descripcion(self):
        genero = 'un gato' if self.sexo == 'macho' else 'una gata'
        return f"{self.descripcionAnimal()}, es {genero} {self.color} y {self.estado}."

mascotas = {
                "Bobby": Perro("Bobby", 3, "rottweiler", "rojo", "cuero"),
                "Toffee": Perro("Toffee", 5, "ovejero alemán", "negro", "tela"),
                "Grisina": Gato("Grisina", 4, "hembra", "gris"),
                "Shevek": Gato("Shevek", 1, "macho", "naranja")
            }

mascotas['Toffee'].mueveCola('rápido')
mascotas['Shevek'].siMaulla('maulla')

for mascota in mascotas.values():
    print(mascota.descripcion())
