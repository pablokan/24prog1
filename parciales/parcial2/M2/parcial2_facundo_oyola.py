class Plataforma:
    def __init__(self,nombre) -> None:
        self.nombre = nombre

class Peliculas(Plataforma):
    def __init__(self, nombre, cantidadVisualizaciones, actores,duracion) -> None:
        super().__init__(nombre)
        self.duracion = duracion
        self.cantidadVisualizaciones = cantidadVisualizaciones
        self.actores = actores

    def masVisualizacionPeliculas(self):
        return self.nombre
    
    def actoresPelis(self):
        return self.actores.split(",")
    
class Series(Plataforma):
    def __init__(self, nombre, cantidadVisualizacionesSeries, seriesActores,temporadas) -> None:
        super().__init__(nombre)
        self.temporadas = temporadas
        self.cantidadVisualizacionesSeries = cantidadVisualizacionesSeries
        self.seriesActores = seriesActores

    def masVisualizacionSeries(self):
        return self.cantidadVisualizacionesSeries
    
    def actoresSeries(self):
        return self.seriesActores.split(",")

p = Plataforma("Netflix")
print(f"La Plataforma: {p.nombre}")
print()

series = [
        Series("Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6), 
        Series("The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4)
          ]

pelis = [
        Peliculas("Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30),
        Peliculas("Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148), 
        Peliculas("Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140)
]



for pelicula in pelis:
    for serie in series:
        if pelicula.cantidadVisualizaciones < serie.cantidadVisualizacionesSeries:
            print(f"El video más visto en la plataforma de {p.nombre} es: {pelicula.masVisualizacionPeliculas()}")
            break
        else:
            print(f"El video más visto en la plataforma de {p.nombre} es: {serie.masVisualizacionSeries()}")
    break

for seriesss in series:
    actoreS = seriesss.actoresSeries()

for pelisss in pelis:
    actoresP = pelisss.actoresPelis()

actoreSerieYpeli = actoresP + actoreS

print("Actores que trabajan en series y peliculas: ") 
for actor in actoreSerieYpeli:
    if actoresP == actoreS:
        print(f"{actor}")
#No llegue con el tiempo no me salio perdon profe :(

for serie in series:
    if serie.temporadas < 5:
        print(f"Series que tienen menos de 5 temporadas: {serie.nombre}")