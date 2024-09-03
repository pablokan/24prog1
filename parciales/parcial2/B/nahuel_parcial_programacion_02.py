class Mascota(): 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def datos(self):
        return (f'Nombre: {self.nombre} Edad: {self.edad} Años')

class Collar():
    def __init__(self,nombre):
        self.color = input(f'Ingrese color del collar de {nombre} : ')
        self.material = input(f'Ingrese material del collar {nombre}: ')

class Perro(Mascota): 
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        self.collar = Collar(nombre)
        
    def animo(self):
        a = input(f'{self.nombre} mueve la cola? (si/no)')
        if a.lower() == 'si':
            self.contento = 'esta feliz'
        else:
            self.contento = 'esta triste'      
        
class Gato(Mascota): 
    def __init__(self, nombre, edad, sexo, color):
        super().__init__(nombre, edad)
        self.sexo = sexo
        self.color = color

    def animo(self):
        a = input(f'{self.nombre} maulla? (si/no)')
        if a == 'si':
            self.hambre = 'tiene hambre'
        else:
            self.hambre = 'no tiene hambre'
            
class Familia():
    def __init__(self):
        self.perros = [Perro('bobby',3,'rottweiler'),
                       Perro('Toffe', 5,'ovejero aleman')]
        self.gatos = [Gato('grisina',4,'gata','gris'),
                      Gato('shevek',1,'gato','naranja')]
        
    def todosLosDatos(self):
        for perro in self.perros:
            animo = perro.animo()
            print(f'{perro.nombre} tiene {perro.edad} años, es un {perro.raza} que lleva un collar {perro.collar.color} de {perro.collar.material} y {perro.contento}')
        for gato in self.gatos:
            animo = gato.animo()
            print(f'{gato.nombre} tiene {gato.edad} años, es {gato.sexo} de color {gato.color} {gato.hambre}')
mascotas = Familia()

mascotas.todosLosDatos()
print(mascotas.perros[0].datos())
print(mascotas.gatos[0].datos())