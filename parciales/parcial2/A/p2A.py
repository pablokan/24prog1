class Video:
    def __init__(self, titulo, vistas, actores):
        self.titulo = titulo
        self.vistas = vistas
        self.actores = actores.split(',')
   
class Serie(Video):
    def __init__(self, titulo, vistas, actores, temporadas):
        super().__init__(titulo, vistas, actores)
        self.temporadas = temporadas

class Pelicula(Video):
    def __init__(self, titulo, vistas, actores, duracion):
        super().__init__(titulo, vistas, actores)
        self.duracion = duracion

class Plataforma:
    def __init__(self, series, peliculas):
        self.series = series
        self.peliculas = peliculas

    def videoMasVisto(self):
        todosLosVideos = self.series + self.peliculas
        l = [(v[1], v[0]) for v in todosLosVideos]
        l.sort(reverse=True)
        return l[0][1]

    def actoresEnAmbas(self):
        

    def seriesMenos5Temporadas(self):
        return [serie for serie in self.series if serie.temporadas < 5]


plataforma = Plataforma([["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]], [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]])

# plataforma.actoresEnAmbas()
# plataforma.seriesMenos5Temporadas()

print(f"El video más visto: {plataforma.videoMasVisto()}")

      
# print("Actores que trabajan en series y películas:")
# for actor in actores_en_ambos:
#     print(f"- {actor}")
# print("Series que tienen menos de 5 temporadas:")
# for serie in series_menos_cinco_temporadas:
#     print(f"- {serie.titulo}")
