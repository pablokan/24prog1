# Definimos una clase base Video que servirá para la herencia
class Video:
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores

    def obtener_nombre(self):
        return self.nombre

    def obtener_visualizaciones(self):
        return self.visualizaciones

    def obtener_actores(self):
        return set(self.actores.split(','))


# Definimos la clase Pelicula que hereda de Video
class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion


# Definimos la clase Serie que hereda de Video
class Serie(Video):
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas


# Clase Plataforma para manejar la composición de videos (películas y series)
class Plataforma:
    def __init__(self):
        self.videos = []

    def agregar_video(self, video):
        self.videos.append(video)

    def video_mas_visto(self):
        video_max = max(self.videos, key=lambda video: video.obtener_visualizaciones())
        return video_max.obtener_nombre()

    def actores_en_series_y_peliculas(self):
        actores_series = set()
        actores_peliculas = set()

        for video in self.videos:
            if isinstance(video, Serie):
                actores_series.update(video.obtener_actores())
            elif isinstance(video, Pelicula):
                actores_peliculas.update(video.obtener_actores())

        actores_comunes = actores_series.intersection(actores_peliculas)
        return actores_comunes

    def series_menos_de_5_temporadas(self):
        series_filtradas = [serie.obtener_nombre() for serie in self.videos if isinstance(serie, Serie) and serie.temporadas < 5]
        return series_filtradas


# Datos iniciales
series = [
    ["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6],
    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]
]

pelis = [
    ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],
    ["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
    ["Batman Begins", 4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

# Instanciación de la plataforma
plataforma = Plataforma()

# Agregamos las series y películas a la plataforma
for serie in series:
    plataforma.agregar_video(Serie(*serie))

for peli in pelis:
    plataforma.agregar_video(Pelicula(*peli))

# Resultados
print(f"El video más visto: {plataforma.video_mas_visto()}")
print("Actores que trabajan en series y películas:")
for actor in plataforma.actores_en_series_y_peliculas():
    print(f"- {actor}")

print("Series que tienen menos de 5 temporadas:")
for serie in plataforma.series_menos_de_5_temporadas():
    print(f"- {serie}")
