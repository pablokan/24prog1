class Animal(): # clase ancestro o madre en este caso
    def __init__(self, n):
        self.nombre = n

    def habla(self): # método abstracto
        # sirve para indicar que DEBE ser definido en las clases hijas
        pass

class Perro(Animal): # Perro hereda Animal
    def __init__(self, n):
        super().__init__(n) # call al constructor de la clase madre

    def habla(self):
        return 'guauuuuuu'
    
class Gato(Animal):
    def __init__(self, n):
        super().__init__(n) 

    def habla(self):
        return 'miauuuuuu'


perrito = Perro('Rocky')
print(f'El perrito se llama {perrito.nombre} y dice {perrito.habla()}')

gatito = Gato('Micifuz')
print(f'El gatito se llama {gatito.nombre} y dice {gatito.habla()}')


