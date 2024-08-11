class Animal: # clase abstracta es cuando se define solamente para ser heredada
    def __init__(self, n, w):
        self.name = n
        self.weight = w

    def getName(self):
        return self.name
    
    def talk(self): # método abstracto: para recordar que debe ser definido en las clases herederas
        pass

class Dog(Animal): # Perro hereda Animal
    def __init__(self, n, w, c): # constructor de Dog
        super().__init__(n, w) # call al constructor de Animal
        self.color = c

    def talk(self): # polimorfismo: redefinición de un método heredado
        return 'guauuuuu'
    
    def correr(self, velocidad):
        return f"corre {velocidad}!"
    
class Cat(Animal):
    def __init__(self, n, w):
        super().__init__(n, w)

    def talk(self):
        return 'miauuuuu'

perrito = Dog('Bobby', 20, 'negro')
print(f'El perrito se llama {perrito.getName()} y pesa {perrito.weight} kilos y {perrito.correr('rapido')} y es de color {perrito.color} y dice {perrito.talk()}')

gatito = Cat('Michifuz', 4)
print(f'El gatito se llama {gatito.name} y dice {gatito.talk()}')













