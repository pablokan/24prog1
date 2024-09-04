class Video:
    def __init__(self, title, views, actors):
        self.title = title
        self.views = views
        self.actors = actors.split(',')

    def __str__(self):
        return self.title

class Serie(Video):
    def __init__(self, title, views, actors, seasons):
        super().__init__(title, views, actors)
        self.seasons = seasons

class Pelicula(Video):
    def __init__(self, title, views, actors, duration):
        super().__init__(title, views, actors)
        self.duration = duration

class Plataforma:
    def __init__(self):
        self.series = []
        self.peliculas = []

    def agregar_serie(self, serie):
        self.series.append(serie)

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def video_mas_visto(self):
        todos_videos = self.series + self.peliculas
        return max(todos_videos, key=lambda video: video.views)

    def actores_en_series_y_peliculas(self):
        actores_series = set(actor for serie in self.series for actor in serie.actors)
        actores_peliculas = set(actor for pelicula in self.peliculas for actor in pelicula.actors)
        return actores_series.intersection(actores_peliculas)

    def series_con_menos_de_cinco_temporadas(self):
        return [serie for serie in self.series if serie.seasons < 5]

# Instanciación de series y películas con los datos proporcionados
plataforma = Plataforma()

serie1 = Serie("Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6)
serie2 = Serie("The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4)
pelicula1 = Pelicula("Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30)
pelicula2 = Pelicula("Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148)
pelicula3 = Pelicula("Batman Begins", 4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140)

plataforma.agregar_serie(serie1)
plataforma.agregar_serie(serie2)
plataforma.agregar_pelicula(pelicula1)
plataforma.agregar_pelicula(pelicula2)
plataforma.agregar_pelicula(pelicula3)

# Resultados solicitados
video_mas_visto = plataforma.video_mas_visto()
actores_en_ambos = plataforma.actores_en_series_y_peliculas()
series_menos_cinco_temporadas = plataforma.series_con_menos_de_cinco_temporadas()

# Imprimir resultados
print(f"El video más visto: {video_mas_visto.title}")
print("Actores que trabajan en series y películas:")
for actor in actores_en_ambos:
    print(f"- {actor}")
print("Series que tienen menos de 5 temporadas:")
for serie in series_menos_cinco_temporadas:
    print(f"- {serie.title}")
