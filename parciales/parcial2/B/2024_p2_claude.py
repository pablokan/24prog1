from abc import ABC, abstractmethod

class Mascota(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @abstractmethod
    def describir(self):
        pass
    
    @abstractmethod
    def estado_animo(self):
        pass

class Perro(Mascota):
    def __init__(self, nombre, edad, raza, color_collar, material_collar):
        super().__init__(nombre, edad)
        self.raza = raza
        self.collar = {"color": color_collar, "material": material_collar}
        self.contento = False
    
    def mover_cola(self, rapidez):
        self.contento = rapidez
    
    def estado_animo(self):
        return "contento" if self.contento else "triste"
    
    def describir(self):
        return f"{self.nombre} tiene {self.edad} años, es un {self.raza} que lleva un collar {self.collar['color']} de {self.collar['material']} y está {self.estado_animo()}."

class Gato(Mascota):
    def __init__(self, nombre, edad, sexo, color):
        super().__init__(nombre, edad)
        self.sexo = sexo
        self.color = color
        self.hambre = False
    
    def maullar(self):
        self.hambre = True
    
    def estado_animo(self):
        return "tiene hambre" if self.hambre else "no tiene hambre"
    
    def describir(self):
        return f"{self.nombre} tiene {self.edad} años, es un{'a' if self.sexo == 'hembra' else ''} gat{'a' if self.sexo == 'hembra' else 'o'} {self.color} y {self.estado_animo()}."

# Crear las mascotas
bobby = Perro("Bobby", 3, "rottweiler", "rojo", "cuero")
toffee = Perro("Toffee", 5, "ovejero alemán", "negro", "tela")
grisina = Gato("Grisina", 4, "hembra", "gris")
shevek = Gato("Shevek", 1, "macho", "naranja")

# Establecer estados de ánimo
bobby.mover_cola(False)  # Bobby está triste
toffee.mover_cola(True)  # Toffee está contento
shevek.maullar()  # Shevek tiene hambre

# Mostrar la información de todas las mascotas
mascotas = [bobby, toffee, grisina, shevek]

for mascota in mascotas:
    print(mascota.describir())
