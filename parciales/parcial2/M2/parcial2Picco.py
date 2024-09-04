
class Video:
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = set(actores.split(',')) 

    def __str__(self):
        return self.nombre


class Serie(Video):
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas


class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion


class Plataforma:
    def __init__(self):
        self.series = []
        self.peliculas = []

    def agregarSerie(self, serie):
        self.series.append(serie)

    def agregarPelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def videoMasVisto(self):
        videos = self.series + self.peliculas
        masVisto = max(videos, key=lambda video: video.visualizaciones)
        return masVisto

    def actoresEnSeriesyPeliculas(self):
        actoresSeries = set()
        actoresPeliculas = set()

        for serie in self.series:
            actoresSeries.update(serie.actores)

        for pelicula in self.peliculas:
            actoresPeliculas.update(pelicula.actores)

        actoresComunes = actoresSeries.intersection(actoresPeliculas)
        return actoresComunes

    def seriesMenosDe5Temporadas(self):
        seriesMenos5 = [serie for serie in self.series if serie.temporadas < 5]
        return seriesMenos5

# info de consigna
series = [
    ["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6],
    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]
]

pelis = [
    ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],
    ["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
    ["Batman Begins", 4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]


plataforma = Plataforma()


for serie_data in series:
    nombre, visualizaciones, actores, temporadas = serie_data
    serie = Serie(nombre, visualizaciones, actores, temporadas)
    plataforma.agregarSerie(serie)


for pelicula_data in pelis:
    nombre, visualizaciones, actores, duracion = pelicula_data
    pelicula = Pelicula(nombre, visualizaciones, actores, duracion)
    plataforma.agregarPelicula(pelicula)

videoMasVisto = plataforma.videoMasVisto()
print(f"El video más visto: {videoMasVisto}")


actoresComunes = plataforma.actoresEnSeriesyPeliculas()
print("Actores que trabajan en series y películas:")
for actor in actoresComunes:
    print(f"- {actor}")


seriesMenos5 = plataforma.seriesMenosDe5Temporadas()
print("Series que tienen menos de 5 temporadas:")
for serie in seriesMenos5:
    print(f"- {serie}")