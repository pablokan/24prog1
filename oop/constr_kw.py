class Persona():
    def __init__(self, especie='Homo Sapiens', nombre='Sin nombre' ) -> None:
        self.especie = especie
        self.nombre = nombre

p1 = Persona()
print(p1.especie, p1.nombre)
