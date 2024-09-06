class Netflix():
    def __init__(self, nombre, visualizaciones, actores) -> None:
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores

class Series(Netflix):
    def __init__(self, nombre, visualizaciones, actores, temporadas) -> None:
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas

    def cantidadTemporadas(self):
        return self.nombre if self.temporadas < 5 else ""
    
    def agregarActores(self):
        self.actoresss = []
        for actor in self.actores:
            self.actoresss.append(actor)



class Peliculas(Netflix):
    def __init__(self, nombre, visualizaciones, actores, minutos) -> None:
        super().__init__(nombre, visualizaciones, actores)
        self.minutos = minutos

    def agregarActores(self):
        self.actoress = []
        for actor in self.actores:
            self.actoress.append(actor)


serie = Series("Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6)
serie1 = Series("The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4)
print(serie.cantidadTemporadas())
print(serie1.cantidadTemporadas())








