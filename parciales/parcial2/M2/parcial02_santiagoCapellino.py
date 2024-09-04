class Programa():
    def __init__(self, lista) -> None:
        self.lista = lista

    def mayorVisualizaciones(self):
        serieMayor = ''
        contador = 0
        for programa in self.lista:
            if programa[1] > contador:
                serieMayor = programa[0]
                contador = programa[1]
            else:
                pass
        return serieMayor
    
    def separarActores(self):
        actores = []
        listaActores = []
        listaFinalActores = []
        for act in self.lista:
            actores.append(act[2])
        for acto in actores:
            listaActores.append(acto.split(','))
        for actor in listaActores:
            for i in actor:
                listaFinalActores.append(i)
        return listaFinalActores # no me alcanzo el tiempo para hacer el numero 2
        

    def creacionSeriePelicula(self):
        series = []
        peliculas = []
        for programa in self.lista:
            if programa[3] < 10: # las peliculas tienen mas de 10 minutos de duracion, entonces se sabe diferenciar entre peliculas y series
                series.append(Serie(programa[0], programa[3])) # guarda el nombre de la serie, y las temporadas
            else:
                peliculas.append(Pelicula(programa[0], programa[3])) # guarda el nombre de la pelicula y la duracion
        return series, peliculas

class Serie(Programa):
    def __init__(self, lista, temporadas) -> None:
        super().__init__(lista)
        self.temporadas = temporadas
    
    def mayorVisualizaciones(self):
        return super().mayorVisualizaciones()
    
    def menosTemporadas(self):
        seriesMenor = ''
        for programa in self.lista:
            if programa[3] < 5:
                seriesMenor = programa[0]
        else:
            pass
        return seriesMenor

class Pelicula(Programa):
    def __init__(self, lista, minutos) -> None:
        super().__init__(lista)
        self.minutos = minutos
    
    def mayorVisualizaciones(self):
        return super().mayorVisualizaciones()

series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]

pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

videos = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4], ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]]

programa = Programa(videos)
print(f'El video mas visto es: {programa.mayorVisualizaciones()}')

serie = Serie(videos, 4)
print('Series que tienen menos de 5 temporadas:')
print(f' - {serie.menosTemporadas()}')


print(f'{programa.separarActores()}')