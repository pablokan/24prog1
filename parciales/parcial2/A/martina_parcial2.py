class Artista():
    def __init__(self, nombre, cantidadAlbumes, reproducciones):
        self.nombre = nombre
        self.cantidadAlbumes = cantidadAlbumes
        self.reproducciones = reproducciones
         
    def obtReproducciones(self):
        return self.reproducciones
 
    def obtAlbumes(self):
        return self.cantidadAlbumes

class Banda(Artista):
    def __init__(self, nombre, cantidadAlbumes, reproducciones, integrantes):
        super().__init__(nombre, cantidadAlbumes, reproducciones)
        self.integrantes = integrantes
    
    def obtCantantes(self):
        cantantes = [integrantes.split('(')[0] for integrantes in self.integrantes.split(',')]
        return cantantes
        

class Solistas(Artista):
    def __init__(self, nombre, cantidadAlbumes, reproducciones, edad):
        super().__init__(nombre, cantidadAlbumes, reproducciones)
        self.edad = edad
    
    def obtenerApellido(self):
        return self.nombre.split()[-1]
    
bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]


listaArtistaas = []

for banda in bandas:
    listaArtistaas.append(Banda(banda[0], banda[1],banda [2], banda [3]))

for solista in solistas:
    listaArtistaas.append(Solistas(solista[0], solista [1], solista [2], solista [3]))


def obtenerTotalRep(artistas):
    return sum(artista.obtReproducciones() for artista in artistas)
    
    

def obtSolMasViejo(artistas):
    solistas = [artista for artista in artistas if isinstance(artista, Solistas)]
    if not solista:
        return None
    masViejo = max(solistas, key=lambda s: s.edad)
    return masViejo.nombre


def obtenerNomCant(artistas):
    cantantes = []
    for artista in artistas:
        if isinstance(artista, Banda):
            cantantes.extend(artista.obtCantantes())
    return ', '.join(cantantes)

def obtenerArtMayorAlbumes(artistas):
    return max(artistas, key=lambda a: a.obtAlbumes()).nombre

print (f"Total de reporducciones del sitio: {obtenerTotalRep(listaArtistaas)}") 
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -")
print (f"El solista mas viejo: {obtSolMasViejo(listaArtistaas)}")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -")
print (f"Los nombres de los cantantes de las bandas son: \n{obtenerNomCant(listaArtistaas)}")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -")
print (f"El nombre de la banda o el solista con mayor cantidad de álbumes es: {obtenerArtMayorAlbumes(listaArtistaas)}")
print("-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - ")