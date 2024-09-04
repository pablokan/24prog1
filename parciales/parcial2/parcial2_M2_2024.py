class Video:
    def __init__(self, titulo, vistas, actores):
        self.titulo = titulo
        self.vistas = vistas
        self.actores = actores
   
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
        self.series = [Serie(*serie) for serie in series]
        self.peliculas = [Pelicula(*pelicula) for pelicula in peliculas]

    def videoMasVisto(self):
        todosLosVideos = self.series + self.peliculas
        vistasYvideo = [(v.vistas, v.titulo) for v in todosLosVideos]
        vistasYvideo.sort(reverse=True) # ordenar por cantidad de vistas
        return vistasYvideo[0][1]

    def actoresEnAmbas(self) -> set:
        actoresSeries = ''
        for serie in self.series:
            actoresSeries += serie.actores
        actoresSeries = set(actoresSeries.split(','))
        actoresPeliculas = ''
        for pelicula in self.peliculas:
            actoresPeliculas += pelicula.actores
        actoresPeliculas = set(actoresPeliculas.split(','))
        return actoresSeries.intersection(actoresPeliculas)

    def seriesMenos5Temporadas(self):
        return [serie.titulo for serie in self.series if serie.temporadas < 5]


plataforma = Plataforma([["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 2]], [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]])



print(f"El video más visto: {plataforma.videoMasVisto()}")
print(f"Actores que trabajan en series y películas: {plataforma.actoresEnAmbas()}")
print(f"Series que tienen menos de 5 temporadas: {plataforma.seriesMenos5Temporadas()}")
