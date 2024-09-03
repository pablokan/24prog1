class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años"


class Perro(Mascota):
    def __init__(self, nombre, edad, raza, collar_color, collar_material, mueve_cola):
        super().__init__(nombre, edad)
        self.raza = raza
        self.collar_color = collar_color
        self.collar_material = collar_material
        self.mueve_cola = mueve_cola

    def estado_animo(self):
        if self.mueve_cola:
            return "contento"
        else:
            return "triste"

    def descripcion(self):
        base = super().descripcion()
        return f"{base}, es un {self.raza} que lleva un collar {self.collar_color} de {self.collar_material} y está {self.estado_animo()}."


class Gato(Mascota):
    def __init__(self, nombre, edad, sexo, color, maulla):
        super().__init__(nombre, edad)
        self.sexo = sexo
        self.color = color
        self.maulla = maulla

    def estado_animo(self):
        if self.maulla:
            return "tiene hambre"
        else:
            return "no tiene hambre"

    def descripcion(self):
        base = super().descripcion()
        return f"{base}, es un {self.sexo} {self.color} y {self.estado_animo()}."


# Crear los objetos de las mascotas
bobby = Perro("Bobby", 3, "rottweiler", "rojo", "cuero", False)
toffee = Perro("Toffee", 5, "ovejero alemán", "negro", "tela", True)
grisina = Gato("Grisina", 4, "gata", "gris", False)
shevek = Gato("Shevek", 1, "gato", "naranja", True)

# Imprimir la descripción de cada mascota
print(bobby.descripcion())
print(toffee.descripcion())
print(grisina.descripcion())
print(shevek.descripcion())
