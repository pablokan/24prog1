'''
Se crea una plataforma de música tipo Spotify.
Se dispone de los siguientes datos (Listas iniciales posibles):

bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]

Cada sublista contiene: nombre, cantidad de álbumes y cantidad de reproducciones. El cuarto dato son los integrantes en el caso de las bandas y la edad en el caso de los solistas.

Pueden desarmar y rearmar estas listas como les resulte más cómodo.

---------------------- realizar---------------
1) La suma total de reproducciones de todos (bandas y solistas, un solo total final).
2) El apellido del solista más viejo.
3) Los nombres de los cantantes de las bandas.
4) El nombre de la banda o el solista con mayor cantidad de álbumes.
'''

class Artista:
    def __init__(self, nombre, cantAlbums, cantRepro) -> None:
        self.nombre = nombre
        self.cantAlbums = cantAlbums  
        self.cantRepro = cantRepro

class Banda(Artista):
    def __init__(self, nombre, cantAlbums, cantRepro, integrantes)-> None:
        super().__init__(nombre, cantAlbums, cantRepro)
        self.integrantes = integrantes

    def obtener_cantantes(self):
        cantantes = []  
        integrantes = self.integrantes.split(', ')  

        for integrante in integrantes:
            if '(voz)' in integrante:  
                nombre = integrante.split(' (voz)')[0]  
                cantantes.append(nombre) 
        return cantantes  

class Solista(Artista):
    def __init__(self, nombre, cantAlbums, cantRepro, edad):
        super().__init__(nombre, cantAlbums, cantRepro)
        self.edad = edad

class itecMusic:
    def __init__(self):
        self.artistas = []

    def aggArtista(self, artista):
        self.artistas.append(artista)

    def totalReprus(self):
        total = 0
        for artista in self.artistas:
            total += artista.cantRepro
        return total
    
    def solistaMasViejo(self):
        masViejo = None
        for artista in self.artistas:
            if isinstance(artista, Solista):
                if masViejo is None or artista.edad > masViejo.edad:
                    masViejo = artista
        return masViejo.nombre.split()[-1] if masViejo else ''
    
    def cantantesBanda(self):
        cantantes = []
        for artista in self.artistas:
            if isinstance(artista, Banda):
                cantantes.extend(artista.obtener_cantantes())
        return cantantes
    
    def mayorCantAlbums(self):
        mayor = None
        for artista in self.artistas:
            if mayor is None or artista.cantAlbums > mayor.cantAlbums: 
                mayor = artista
        return mayor.nombre if mayor else ''
    
bandas = [
    ['Led Zeppelin', 9, 123456, 'Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones'],
    ['Rage Against the Machine', 4, 243490, 'Zack de la Rocha (voz), Tom Morello, Tim Commerford'],
    ['Seru Giran', 5, 32419, 'Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)']
]

solistas = [
    ['Peter Gabriel', 10, 17319533, 70], 
    ['Jeff Beck', 3, 1023998, 76]
]
app = itecMusic()
for banda in bandas:
    app.aggArtista(Banda(banda[0], banda[1], banda[2], banda[3]))
for solista in solistas:
    app.aggArtista(Solista(solista[0], solista[1], solista[2], solista[3]))

print('Total de reproducciones del sitio: ',app.totalReprus())
print('El solista más viejo es: ',app.solistaMasViejo())
print('Los nombres de los cantantes de las bandas son: ',app.cantantesBanda()) 
print('El nombre de la banda o el solista con mayor cantidad de álbumes es:', app.mayorCantAlbums())
