# se crea una plataforma de videos con peliculas y series tipo netflix
class video:
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores

    def obtener_nombre(self):
        return self.nombre 
    
    def obtener_visualizaciones(self):
        return self.visualizaciones
    
    def obtener_actores(self):
        return self.actores
    
class pelicula(video):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion 

class serie(video):
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas

class plataforma:
    def __init__(self, series, pelis):
        self.series = [serie(*serie) for serie in series]
        self.peliculas = [pelicula(*peli) for peli in pelis]

    def video_mas_visto(self):
        todos_videos = self.series + self.peliculas
    
    def actores_en_series_y_peliculas(self):
        actores_series = set()
        actores_peliculas = set()

    def series_con_menos_de_5_temporadas(self):
        return [serie.obtener_nombre() for serie in self.series if serie.obtener_temporadas() < 5]
    
# Datos
series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6],
          ["The Umbrella Academy", 2434908 , 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]

pelis = [["Inmortales", 35 , 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],
         ["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
         ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

pltaforma = plataforma(series, pelis)

print(f"el video mas visto: {plataforma.video_mas_visto ()}")

actores_comunes = plataforma.actores_en_series_y_peliculas
print("actores que trabajan en series y peliculas")

series_menos_5_temporadas = plataforma.series_con_menos_de_5_temporadas
print("series que tienen menos de 5 temporadas")


