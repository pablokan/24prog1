class Familia():
    def __init__(self):
        pass
    
class Mascotas():
    def __init__(self, n, e, a):
        self.nombre = n
        self.edad = e
        self.animo = a
        self.perros = []
        self.gatos = []
        hayMas = 's'
        while hayMas != 's':
            m = input('Ingrese una mascota (perro/gato): ')
            if m == 'perro':
                perro = Perro(input('Ingrese el nombre del perro: '), input('Ingrese la edad del perro: '), input('el perro mueve la cola? (s/n): '), input('Ingrese la raza del perro: '), input('Ingrese el tipo de collar del perro: '))
                self.perros.append(perro)
            else:
                gato = Gato(input('Ingrese el nombre del gato: '), input('Ingrese la edad del gato: '), input('El gato maúlla? (s/n): '), input('Ingrese el sexo del gato (f/m): '), input('Ingrese el color del gato: '))
                self.gatos.append(gato)
            hayMas = input('Desea seguir ingresando mascotas? (s/n): ')
            
        if perro (a == 's'):
            self.animo = 'contento'
        else:
            self.animo = 'triste'
        if gato (a == 's'):
            self.animo = 'tiene hambre'
        else:
            self.animo = 'no tiene hambre'
        
            
    def devuelveInformacion(self):
        print(f'{Perro.informacionPerros()}')
        print(f'{Gato.informacionGatos()}')
            
class Perro(Mascotas):
    def __init__(self, n, e, a, r, tC):
        super().__init__(n, e, a)
        self.raza = r
        self.tipoCollar = tC
    
    def informacionPerros():
        return f'{self.n} tiene {self.e} años, es un {self.r} que lleva un collar {self.tC} y está {self.aP}.'
        
class Gato(Mascotas):
    def __init__(self, n, e, a, s, c):
        super().__init__(n, e, a)
        self.sexo = s
        if s == 'f':
            self.sexo = 'gata'
        else:
            self.sexo = 'gato'
        self.color = c
    
    def informacionGatos():
        for i in range(len(self.gatos)):
            return f'{self.n} tiene {self.e} años, es {self.s} {self.c} y {self.aG}'
        
perro1 = Mascotas(Perro('Bobby', 3, 'n', 'rottweiler', 'rojo de cuero'))
perro2 = Mascotas(Perro('Toffee', 5, 's', 'ovejero alemán', 'negro de tela'))
gato1 = Mascotas(Gato('Grisina', 4, 'n', 'f', 'gris'))
gato2 = Mascotas(Gato('Shevek', 1, 's', 'm', 'naranja'))