class Animal(): # clase ancestro o madre en este caso
    def ponerNombre(self, n):
        self.nombre = n

class Perro(Animal): # Perro hereda Animal
    pass

class Gato(Animal):
    pass

perrito = Perro()
perrito.ponerNombre('Rocky')
print(perrito.nombre)

gatito = Gato()
gatito.ponerNombre('Michi')
print(gatito.nombre)

