class Artista:
    def __init__(self, nombre, albumes, reproducciones):
        self.nombre = nombre
        self.albumes = albumes
        self.reproducciones = reproducciones

class Solista(Artista):
    def __init__(self, nombre, albumes, reproducciones, edad):
        super().__init__(nombre, albumes, reproducciones)
        self.edad = edad

class Banda(Artista):
    def __init__(self, nombre, albumes, reproducciones, integrantes):
        super().__init__(nombre, albumes, reproducciones)
        self.integrantes = integrantes.split(',')

    def obtenerCantantes(self):
        cantantes = []
        for integrante in self.integrantes:
            if "(voz)" in integrante:
                cantantes.append(integrante[:-5])
        return cantantes

class Plataforma:
    def __init__(self, bandas, solistas) -> None:
        self.bandas = [Banda(*banda) for banda in bandas]
        self.solistas = [Solista(*solista) for solista in solistas]

    def totalReproducciones(self):
        artistas = self.bandas + self.solistas
        total = 0
        for artista in artistas:
            total += artista.reproducciones
        return total
    
    def solistaMasViejo(self):
        masViejo = ''
        edad = 0
        for solista in self.solistas:
            if solista.edad > edad:
                masViejo = solista.nombre
                edad = solista.edad
        return masViejo
    
itecfy = Plataforma([["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"], ["Rage Against the Machine", 4, 243490, "Zack de la Rocha (voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]], [["Peter Gabriel", 10, 17319533, 70],["Jeff Beck", 3, 1023998, 76]])

print(itecfy.totalReproducciones())
print(itecfy.solistaMasViejo())
for banda in itecfy.bandas:
    print(*banda.obtenerCantantes())
