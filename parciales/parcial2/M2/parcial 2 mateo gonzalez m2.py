class Plataforma():
    def __init__(self, series, peliculas, video) -> None:
        self.series = series
        self.peliculas = peliculas
        self.video = video 
        series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]
        peliculas = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

class Serie(Plataforma):
    def __init__(self, series, peliculas, video, titulo, actores, visualizaciones, temporadas) -> None:
        super().__init__(series, peliculas)
        self.titulo = titulo
        self.actores = actores.split(',')
        self.visualizaciones = visualizaciones
        self.temporadas = temporadas

class Peliculas(Plataforma):
    def __init__(self, series, pelicula, nombre, video, visualizaciones, actores, duracion) -> None:
        super().__init__(series, pelicula)
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores.split(',')
        self.duracion = duracion

#hola profe, perdon por el codigo desagradable, aca no me salio para saber el video mas visto
def videoMasVistas(video):
    return video
pass


def actoresAmbos(video, series, peliculas, actores):
    actoresSeries = set(actores for serie in series for actor in serie.actores)
    actoresPeliculas = set(actores for pelicula in peliculas for in pelicula.actores)
    return list(actoresSeries y actoresPeliculas)

def menosTemporadas(series):
    return [serie.nombre for serie in series if serie.temporadas < 5]

videoMasVisitas = videoMasVisitas (series + peliculas)
print(f" el video con mas visualizaciones es {videoMasVisitas.nombre} con {videoMasVisitas.visualizaciones} visualizaciones")

actoresAmbos = actoresAmbos (series + peliculas)
print(f" los actores que figuran en series y peliculas son {','(actoresAmbos)}")

seriesMenor = seriesMenorTemp (series)
print(f'las series con menos de 5 temporadas son {','(seriesMenor)}')

#no me mandes a turisimo, ese es el peor destino para cualquier persona de bien