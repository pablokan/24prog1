

class Mascota:
    def __init__(self, n, e, a):
        self.nombre = n
        self.edad = e
        self.animo = a

    
    def obtengoNombre(self):
        return self.nombre
    
    def obtengoEdad(self):
        return self.edad
    
    def estadoAnimo(self, aP, aG):
        if self.aP == self.aP( 'mueve la cola rapido esta feliz'):
            print()
        else: 
            self.aG != self.aG('no mueve la cola rapido esta triste')
            print()

        if self.aG == 'si el gato maulla tiene hambre':
            print()
        else: 
            self.aG != 'no tiene hambre'
     

class Perro(Mascota):
    def __init__(self, raza, tipoCollar):
        super().__init__(raza, tipoCollar)
        self.raza = raza
        self.tipoCollar = tipoCollar
  

class Gato(Mascota):
    def __init__(self, sexo, color):
        super().__init__(sexo, color)
        self.sexo = sexo
        self.color = color
    def obtengoSexo(self):
        return self.sexo 

    def obtengoColor(self):
        return self.color

class Familia:
    def __init__(self, tipoMascota, cantidad):
        self.tipoMacota = tipoMascota
        self.cantidad = cantidad
        self.mascotas = []

        if tipoMascota == 'Gato':
            for i in range(cantidad):
                gatito1 = f'Gato{i+1}'
                nombre = 'Grisina'
                edad = '4 años'
                gatito2 = f'Gato{i+1}'
                nombre = 'Shevek'
                edad = '1 año'
                self.mascotas.append(gatito1, gatito2, nombre, edad)
        elif tipoMascota == 'Perro':
            for i in range(cantidad):
                perrito1 = f'Perro{i+1}'
                nombre = 'Bobby'
                edad = '3 años'
                perrito2 = f'Perro{i+1}'
                nombre = 'Toffee'
                edad = '5 año'
                self.mascotas.append(perrito1, perrito2, nombre, edad)
        else: 
            print('no existe animal')


perrito2 = Mascota('Toffee', 1, 'contento')
gatito1 = Mascota('Grisina', 4, 'no tiene hambre')
gatito2 = Mascota('Shevek', 1, 'tiene hambre')






