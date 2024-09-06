#Se crea una plataforma de videos con películas y series tipo Netflix.
#listas con datos
series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]
pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]]

class Video:
    def __init__(self, nom, vis, act) -> None:
        self.nombre = nom
        self.visual = vis
        self.actores = act.split(',')

class Serie(Video):
    def __init__(self, nom, vis, act, cant_temp) -> None:
        super().__init__(nom, vis, act)
        self.cant_temporadas = cant_temp

class Pelicula(Video):
    def __init__(self, nom, vis, act, duracion) -> None:
        super().__init__(nom, vis, act)
        self.duracion = duracion

class NetView: #Netview clase principal - plataforma creada tipo 'Netflix'.
    def __init__(self) -> None:
        self.peliculas = [
                        Pelicula('Inmortales', 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30),
                        Pelicula('Inception', 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148),
                        Pelicula('Batman Begenis', 4760183,'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140)]
        self.series = [
                        Serie('Peaky Blinders', 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6),
                        Serie('The Umbrella Academy', 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4)]
        
    def protagonistas(self):
        actores_peliculas = []
        actores_comunes = []
        for pelicula in self.peliculas:
            for actor in pelicula.actores:
                actores_peliculas.append(actor)

        for serie in self.series:
            for actor in serie.actores:
                if actor in actores_peliculas and actor not in actores_comunes:
                    actores_comunes.append(actor)
        return actores_comunes
    
    def mas_view(self):
        contador = 0
        corte = ''
        for serie in self.series + self.peliculas:  
            if serie.visual > contador:
                contador = serie.visual
                corte = serie.nombre
        return corte
    
    def salida(self):
        cinco_temp = ''
        for serie in self.series:
            if serie.cant_temporadas < 5:
                cinco_temp = serie.nombre
    
        print(f'El video más visto: {self.mas_view()}')
        print()
        print('Actores que trabajan en series y peliculas: ') 
        print(self.protagonistas())
        print()
        print('Series con menos de 5 temporadas:')
        print(f'{cinco_temp}')


#Programa principal
plataforma = NetView()
plataforma.salida()

