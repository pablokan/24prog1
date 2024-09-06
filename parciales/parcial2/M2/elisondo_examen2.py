# Lista series y peliculas
series = [
    ["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6],
    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]
]

pelis = [
    ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],
    ["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
    ["Batman Begins", 4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

#clase Main
class Video:
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores

# Clase Serie hereda de Video
class Serie(Video):
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas

# Clase Pelicula hereda de Video
class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion

# Composición - Plataforma donde están las series y las películas
class Netflyx:
    def __init__(self):
        self.series = []
        self.peliculas = [] 
    
    # Función para agregar las series y las películas
    def agregarSerie(self, serie):
        self.series.append(serie)

    def agregarPelicula(self, pelicula):
        self.peliculas.append(pelicula)

    # Actores en pelis y series
    def ActoresSeriesyPelis(self):
        #separo los actores por coma y los agrego al conjunto
        actoresSeries = {actor for serie in self.series for actor in serie.actores.split(',')} 
        actoresPelis = {actor for pelicula in self.peliculas for actor in pelicula.actores.split(',')}
        #busco la interseccion entre actores de serie y pelicula, q eso seria actores q trabajen en ambas
        return actoresSeries.intersection(actoresPelis) 

    # Serie con menos de 5 temporadas
    def SeriesCorta(self):
        return [serie.nombre for serie in self.series if serie.temporadas < 5]


# Creamos la plataforma
netflyx = Netflyx()

# Agregar series y películas a la plataforma
for serie in series:
    netflyx.agregarSerie(Serie(*serie))

for peli in pelis:
    netflyx.agregarPelicula(Pelicula(*peli))
# Agrego los actores q participan en ambas
actoresenComunes = netflyx.ActoresSeriesyPelis()

#Salida
print(f'El video mas visto: ') #no me salio
# Salida punto 2 
print("Actores que trabajan en series y películas:")
for actor in actoresenComunes:
    print(f"- {actor}")
#Salida punto 3
seriesCorta = netflyx.SeriesCorta()
print("Series con menos de 5 temporadas:")
for serie in seriesCorta:
    print(f"- {serie}")