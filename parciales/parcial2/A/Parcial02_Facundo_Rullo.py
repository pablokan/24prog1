#############################
#                           #
#   Alumno: Facundo Rullo   #
#   Comision: A             #
#   Parcial: 02             #
#                           #
#############################

class Musico:
    def __init__(self, nombre, cantAlbumes, cantReproducciones) -> None:
        self.nombre = nombre
        self.cantAlbumes = cantAlbumes
        self.cantReproducciones = cantReproducciones


class Solistas(Musico):
    def __init__(self, nombre, cantAlbumes, cantReproducciones, edad) -> None:
        super().__init__(nombre, cantAlbumes, cantReproducciones)
        self.edad = edad

class Bandas(Musico):
    def __init__(self, nombre, cantAlbumes, cantReproducciones, integrantes) -> None:
        super().__init__(nombre, cantAlbumes, cantReproducciones)
        self.integrantes = integrantes


class Spotify:
    def __init__(self) -> None:
        
        # nombre, cantidad de álbumes y cantidad de reproducciones, integrantes
        self.bandas = [
            ["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
            ["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
            ["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
            ]
        
        # nombre, cantidad de álbumes y cantidad de reproducciones, edad
        self.solistas = [
            ["Peter Gabriel", 10, 17_319_533,70],
            ["Jeff Beck", 3, 1_023_998, 76]
            ]
        
        
        self.bandasMusicales = []
        self.solistasMusicales = []
        
        for ban in self.bandas:
            band = Bandas(ban[0], ban[1], ban[2], ban[3])
            self.bandasMusicales.append(band)
        
        for sol in self.solistas:
            soli = Solistas(sol[0], sol[1], sol[2], sol[3])
            self.solistasMusicales.append(soli)
        
#    1) La suma total de reproducciones de todos (bandas y solistas, un solo total final).
    def sumaTotalReproducciones(self):
        cantReproduccionesBanda = 0
        cantReproduccionesSolista = 0
        
        for banda in self.bandasMusicales:
            cantReproduccionesBanda += banda.cantReproducciones
            
        for solista in self.solistasMusicales:
            cantReproduccionesSolista += solista.cantReproducciones
            
        reproduccionesTotales = cantReproduccionesBanda + cantReproduccionesSolista
        return reproduccionesTotales
    
# 2) El apellido del solista más viejo.
    def solistaViejo(self):
        edadesSolistas = []
        nombresSolistas = []
        
        for solista in self.solistasMusicales:
            edadesSolistas.append(solista.edad)
            nombresSolistas.append(solista.nombre)
        
        if edadesSolistas[0] > edadesSolistas[1]:
            return nombresSolistas[0]
        else:
            return nombresSolistas[1]

# 3) Los nombres de los cantantes de las bandas.
    def cantantesDeBandas(self):
        cantantes = []
        for banda in self.bandasMusicales:
            cantanteVoz = banda.integrantes.split(',')
            for voz in cantanteVoz:
                if '(voz)' in voz:
                    cantantes.append([voz, banda.nombre])
            
        for cant in cantantes:
            print(f'Los cantantes de la banda ----> {cant[1]} <---- son: ')
            print(cant[0])
            print('\n')
    
# 4) El nombre de la banda o el solista con mayor cantidad de álbumes.
    def mayorCantidadDeAlbumes(self): 
        cantidadAbumesBanda = []
        cantidadAlbumesSolista = []
        
        for banda in self.bandasMusicales:
            cantidadAbumesBanda.append([banda.cantAlbumes, banda.nombre])
            
        for solista in self.solistasMusicales:
            cantidadAlbumesSolista.append([solista.cantAlbumes, solista.nombre])
            
        
        maximoAlbumBandas = max(cantidadAbumesBanda)
        maxmoAlbumSolistas = max(cantidadAlbumesSolista)
        
        if maximoAlbumBandas > maxmoAlbumSolistas:
            return f'{cantidadAbumesBanda[0][1]} con un total de {cantidadAbumesBanda[0][0]} albumes.'
        else:
            return f'{cantidadAlbumesSolista[0][1]} con un total de {cantidadAlbumesSolista[0][0]} albumes.'
        

spotify = Spotify()

print('\n**************** Cantidad de Reproducciones ****************\n')

reproducciones = spotify.sumaTotalReproducciones()
print(f'Total de reproducciones de bandas y solistas: {reproducciones}')

print('\n**************** Solista mas Viejo ****************\n')

solistaViejo = spotify.solistaViejo()
print(f'El solista maas viejo es: {solistaViejo}')

print('\n**************** Cantante de las Bandas ****************\n')

spotify.cantantesDeBandas()

print('\n**************** Mayor Cantidad de Albumes ****************\n')

masAlbumes = spotify.mayorCantidadDeAlbumes()
print(f"El nombre de la banda o el solista con mayor cantidad de albunes es: {masAlbumes}")

print('\n')