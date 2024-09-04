#parcial 02 herencia y composicion
class Dato: #? clase madre
    def __init__(self, nom, visual, actores):
        self.nom = nom
        self.visual = visual
        self.actores = actores

class Serie(Dato):  #! herencia
    def __init__(self, nom, visual, actores, tempo):
        super().__init__(nom, visual, actores)
        self.tempo = tempo

class Pelicula(Dato):  #! herencia
    def __init__(self, nom, visual, actores):
        super().__init__(nom, visual, actores)
        self.nom = nom
        self.visual = visual
        self.actores = actores
# instancio las series
series = [
    Serie("Peaky Blinders", 1234567, ['Cillian Murphy', 'Paul Anderson', 'Helen McCrory'], 6),
    Serie("The Umbrella Academy", 2434908, ['Tom Hopper', 'Emmy Raver-Lampman', 'Ellen Page', 'David Castañeda'], 4)
]

# instancio las pelicula
pelis = [
    Pelicula("Inmortales", 35, ['Mirtha Legrand', 'Carlitos Balá', 'Elizabeth The Second']),
    Pelicula("Inception", 17319533, ['Leonardo DiCaprio', 'Ellen Page', 'Joseph Gordon-Levitt']),
    Pelicula("Batman Begins", 4760183, ['Christian Bale', 'Leonardo DiCaprio', 'Cillian Murphy', 'Michael Caine'])
]
def videoMasVisualizaciones(pelis,series): #buscar y guardar el valor mas grande sea tanto serie como pelicula
    maxVisual = 0
    video = None
    for serie in series: #bsuacr la serie mas vista
        if serie.visual > maxVisual:
            maxVisual = serie.visual
            video = serie.nom
    for peli in pelis: #la pelicula mas vista
        if peli.visual > maxVisual:
            maxVisual = peli.visual
            video = peli.nom
    return video #devolver el video mas visto(sea peli o sea serie)
#composicion
def actoresEnComun(series, pelis):#actores que comparten ambas list
    actoresSeries = set()
    for serie in series:
        actoresSeries.update(serie.actores)
    
    actoresPelis = set()
    for peli in pelis:
        actoresPelis.update(peli.actores)
    return actoresSeries.intersection(actoresPelis) #devuelvo la interseccion entre el punto serie y pelicula
    
def seriesMenor(series):
    return [serie.nom for serie in series if serie.tempo < 5] #recorrer la lista de series, serie veces y devolver el nombre de la que sea menor a 5(temporadas)

#ejc
videoMasVisto = videoMasVisualizaciones(series, pelis)
actoresComunes = actoresEnComun(series, pelis)
seriesPocasTemporadas = seriesMenor(series)
# resultados esperado
print(f"el video mas visto es: {videoMasVisto}")
print(f"los actores que trabajan en series y peliculas son: \n- {actoresComunes}")
print(f"series que tienen menos de 5 temporadas: \n{seriesPocasTemporadas}")