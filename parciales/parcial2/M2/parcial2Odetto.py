#La plataforma tiene peliculas y series (composicion)
#Las peliculas y series son largometrajes (herencia)

class Largometraje:
    def __init__(self,nom,vis,act) -> None:
        self.nombre = nom
        self.vistas = vis
        self.actores = act      
    
class Serie(Largometraje):
    def __init__(self, nom, vis, act, temp) -> None:
        super().__init__(nom, vis, act)
        self.temporadas = temp
            
class Pelicula(Largometraje):
    def __init__(self, nom, vis, act, time) -> None:
        super().__init__(nom, vis, act)
        self.tiempo = time
        
class Plataforma:
    def __init__(self,ls,lp) -> None:
        self.listaS = []
        self.listaP = []
        for elemento in ls:
            n = elemento[0]
            v = elemento[1]
            a = elemento[2]
            t = elemento[3]
            nuevaSerie = Serie(n,v,a,t) #creando objeto serie
            self.listaS.append(nuevaSerie) 
            
        for elemento in lp:
            n = elemento[0]
            v = elemento[1]
            a = elemento[2]
            t = elemento[3]
            nuevaPelicula = Pelicula(n,v,a,t) #creando objeto pelicula
            self.listaP.append(nuevaPelicula)
    
    def mayorVista(self):
        may = ""
        mas = 0
        for parte in self.listaS:
            if parte.vistas > mas:
                mas = parte.vistas
                may = parte.nombre
        for parte in self.listaP:
            if parte.vistas > mas:
                mas = parte.vistas
                may = parte.nombre

        print(f"\nEl video mas visto: {may} con {mas} vistas")
        print("------------------")
    
    def actores(self):
        listaActSeries = []
        listaActPelis = []
        for video in self.listaS: #jutando todos los actores de series
            pos = 0
            i = 0
            while i < len(video.actores):
                pos = video.actores.find((","),i)
                if pos != -1:
                    actor = video.actores[i:pos]
                    i = pos+1
                else:
                    actor = video.actores[i:]
                    i = 1000
                listaActSeries.append(actor)
           
        for video in self.listaP: #juntando todos los actores de peliculas
            pos = 0
            i = 0
            while i < len(video.actores):
                pos = video.actores.find((","),i)
                if pos != -1:
                    actor = video.actores[i:pos]
                    i = pos+1
                else:
                    actor = video.actores[i:]
                    i = 1000
                listaActPelis.append(actor)
        print("Actores que trabajan en series y películas:")
        
        for actor in listaActPelis: #aca verifico si algun actor de las peliculas esta en la de las series
            if actor in listaActSeries:
                print(f"- {actor}")
        print("------------------")
    
    def pocasTemporadas(self):
        print("Series que tienen menos de 5 temporadas: ")
        for serie in self.listaS:
            if serie.temporadas < 5:
                print(f"- {serie.nombre}")
        print("\n")
        

series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]

pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

prueba1 = Plataforma(series,pelis)
prueba1.mayorVista()
prueba1.actores()
prueba1.pocasTemporadas()