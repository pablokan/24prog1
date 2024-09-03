class Mascotas ():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def datosMascota (self):
        print(f'Nombre: {self.nombre}. Edad: {self.edad} años')

class Perro (Mascotas):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        self.collar1 = Collar('rojo', 'cuero')
        self.collar2 = Collar ('negro', 'tela')
    
    def animos (self):
        estado = input('el pero mueve la cola (si o no): ')
        if estado == 'si':
            estado = 'esta contento'
        else:
            estado = 'esta triste'

        return estado

class Collar ():
    def __init__(self, color, material) -> None:
        self.material = material 
        self.color = color

class Gato (Mascotas): 
    def __init__(self, nombre, edad, sexo, color):
        super().__init__(nombre, edad)
        self.sexo = sexo
        self.color = color
    
    def estadoAnimo (self):
        estado =input('El gato maulla? (si o no): ')
        if estado == 'si':
            estado = 'tiene hambre'
        else:
            estado = 'no tiene hambre'

        return estado

perro1 = Perro('Bobby', 3, 'rottweiler')
perro1.datosMascota()
estado1= perro1.animos()
print(f'{perro1.nombre} tiene {perro1.edad} años, es un {perro1.raza} que lleva un collar {perro1.collar1.color} de {perro1.collar1.material} y {estado1}')

perro2 = Perro('Toffee', 5, 'ovejero aleman')
perro2.datosMascota()
estado2 = perro2.animos()
print(f'{perro2.nombre} tiene {perro2.edad} años, es un {perro2.raza} que lleva un collar {perro2.collar2.color} de {perro2.collar2.material} y {estado2}')

gato1 = Gato('Grisina', 4, 'gata', 'gris')
gato1.datosMascota()
animo1= gato1.estadoAnimo()
print(f'{gato1.nombre} tiene {gato1.edad} años, es una {gato1.sexo} {gato1.color} y {animo1}')

gato2 = Gato('Shevek', 1, 'gato', 'naranja')
gato2.datosMascota()
animo2 = gato2.estadoAnimo()
print(f'{gato2.nombre} tiene {gato2.edad} años, es una {gato2.sexo} {gato2.color} y {animo2}')
