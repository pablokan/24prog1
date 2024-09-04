class Videos:
    def __init__(self, nombre, visualizaciones, actores):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores.split(',')

class Series(Videos): 
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas

class Peliculas(Videos):
    def __init__(self, nombre, visualizaciones, actores, duracion):
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion

class Plataforma:
    def __init__(self): 
        self.peliculas = [Peliculas('Inception', 17319533, 'Leonardo DiCaprio, Ellen Page, Joseph Gordon-Levitt', 148),
                          Peliculas('Batman Begins', 4760183, 'Christian Bale, Leonardo DiCaprio,Cillian Murphy, Michael Caine', 140),
                          Peliculas('Inmortales', 35, 'Mirtha Legrand, Carlitos Balá, Elizabeth The Second', 30)]

        self.series = [Series('Peaky Blinders', 1234567, 'Cillian Murphy, Paul Anderson, Helen McCrory', 6),
                       Series('The Umbrella Academy', 2434908, 'Tom Hopper, Emmy Raver-Lampman, Ellen Page, David Castañeda', 4)]
        
    def mas_visto(self):
            cont = 0
            video = ''

            for i in self.series + self.peliculas:
                if i.visualizaciones > cont:
                    cont = i.visualizaciones
                    video = i.nombre

            return video
    
    def actor(self):
        actores_peliculas = []
        actores_series = []
        repitentes = []
        
        # pone actores de peliculas a la lista
        for i in self.peliculas:
            for p in i.actores:
                if p not in actores_peliculas:
                    actores_peliculas.append(p)
        
        # pone actores de series a la lista
        for i in self.series:
            for p in i.actores:
                if p not in actores_series:
                    actores_series.append(p)
        
        # busca actores que estan en las dos
        for i in actores_peliculas:
            if i in actores_series:
                repitentes.append(i)
    
        return repitentes 

    
    def menos_temp(self):
        serie_larga= ''
        for i in self.series:
            if i.temporadas < 5:
                serie_larga= i.nombre

        return serie_larga

    def printear_todo(self):
            mas_visto_video = self.mas_visto()
            actor_repite = self.actor()
            temporadas = self.menos_temp()

            print("-------------------------------------------------------------------------")
            print(f'El video mas visto: {mas_visto_video}')
            print("-------------------------------------------------------------------------")
            print(f'Actores que trabajan en series y peliculas: {actor_repite}')
            print("-------------------------------------------------------------------------")
            print(f'Series con mas de 5 temporadas: {temporadas}')

netflix = Plataforma()
netflix.printear_todo()