class PlataformaNetflix():
    def __init__(self) -> None:
        pass

class Serie(PlataformaNetflix):
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores.split(',')
        self.temporadas = temporadas

class Pelicula(PlataformaNetflix):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores.split(',')
        self.duracion = duracion


series = [Serie(*s) for s in [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]]
peliculas = [Pelicula(*p) for p in [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]]]

#hola profe aca no me salio para dar el video mas visto :( y puse cualquier cosa
def videoMasVistas(videos):
   videos==17319533
   return videos



def actoreAmbos(videos):
    actoresSeries = set(actor for serie in series for actor in serie.actores)
    actoresPeliculas = set(actor for pelicula in peliculas for actor in pelicula.actores)
    return list(actoresSeries & actoresPeliculas)


def seriesMenosTemp(series):
    return [serie.nombre for serie in series if serie.temporadas < 5]

videoMasvisto = videoMasVistas(series + peliculas)
print(f"El video con más visualizaciones es: {videoMasvisto.nombre} con {videoMasvisto.visualizaciones} visualizaciones")

actoresAmbos= actoreAmbos(series + peliculas)
print(f"Los actores que figuran en series y películas son: {', '(actoresAmbos)}")

seriesMenor = seriesMenosTemp(series)
print(f"Las series con menos de 5 temporadas son: {', '(seriesMenor)}")

#espero que esto este bien por lo menos xd
#No me mande a turismo, todo menos eso