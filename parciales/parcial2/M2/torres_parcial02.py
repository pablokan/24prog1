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
    def __init__(self, nombre, visualizaciones, actores, temporadas):
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas
        
class Plataforma:
    def __init__(self):
        self.peliculas = [Peliculas("Inmortales", 35, "Mirtha Legrand,Carlitos Balá,Elizabeth The Second", 30),
                          Peliculas("Inception", 17319533, "Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt", 148),
                          Peliculas("Batman Begins",4760183, "Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine", 140)]
        
        self.series    = [Series("Peaky Blinders", 1234567, "Cillian Murphy,Paul Anderson,Helen McCrory", 6),
                          Series("The Umbrella Academy", 2434908,"Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda", 4)]
       
    def masVisto(self):
        contar = 0
        video = ""
        
        for serie in self.series + self.peliculas:
            if serie.visualizaciones > contar:
                contar = serie.visualizaciones
                video = serie.nombre
        return video        
        
    def actorProtagonista(self):
        duracion = 0
        actor = []
        
        for p in self.peliculas and self.series:
            if p.temporadas > duracion:
                duracion = p.temporadas
                actores = p.actores
                if len(actores) > 0:
                    actor = actores[0]
        return actor
    
    def mostarTodo(self):
        masVistoVideo = self.masVisto()
        principalActor = self.actorProtagonista()
        cincoTemporadas = [serie.nombre for serie in self.series if serie.temporadas < 5]
                           
        print(f'El video mas visto es: {masVistoVideo}')
        print()
        print(f'Actores que trabajan en series y películas: {principalActor}') #ME DA UNO SOLO
        print()
        print(f'Series que tienen menos de 5 temporadas: {", ".join(cincoTemporadas)}')       
        
Netflix = Plataforma()
Netflix.mostarTodo()                         

