class Animal:
    def __init__(self, id, peso) -> None:
        self.id = id
        self.peso = peso

    def salud(self, pesoSano):
        return "Sano" if self.peso >= pesoSano else "Enfermo"

class Puma(Animal):
    def __init__(self, id, peso, edad) -> None:
        super().__init__(id, peso)
        self.edad = edad
        self.pesoSano = 200

    def esAdulto(self):
        return self.edad > 5
    
class Venado(Animal):
    def __init__(self, id, peso) -> None:
        super().__init__(id, peso)
        self.pesoSano = 120

class Jaula:
    def __init__(self, tipoAnimal, cantidad) -> None:
        self.titulo = f'Jaula de {tipoAnimal}s'
        self.tA = tipoAnimal
        self.animales = []
        for i in range(cantidad):
            peso = int(input(f'Peso del {tipoAnimal}: '))            
            if tipoAnimal == 'puma':
                edad = int(input(f'Edad del {tipoAnimal}: '))
                a = Puma(i+1, peso, edad)
            else:
                a = Venado(i+1, peso)
            self.animales.append(a)

    def datos(self):
        print(self.titulo)
        for a in self.animales:
            print(f'# {a.id} - {a.salud(a.pesoSano)}')

    def cantidadAdultos(self):
        c = 0
        if self.tA == 'venado':
            return "No aplica"
        for p in self.animales:
            if p.esAdulto():
                c += 1
        return c

    
jaulaPumas = Jaula('puma', 4)
jaulaVenados = Jaula('venado', 2)
jaulaPumas.datos()
print(f'Cantidad de adultos: {jaulaPumas.cantidadAdultos()}')
jaulaVenados.datos()
print(f'Cantidad de adultos: {jaulaVenados.cantidadAdultos()}')

