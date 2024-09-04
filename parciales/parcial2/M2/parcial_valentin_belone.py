# 
class Plataforma():
    def __init__(self, tipo, videos):
        self.tipo = tipo
        self.videos = []
        for video in videos:
            if tipo == 'Pelicula':
                n, cv, a, m = video
                self.maxV.append(Pelicula(n,cv,a,m))
            elif tipo == 'Serie':
                n, cv, a, temp = video
                self.maxV.append(Serie(n,cv,a,temp))

    def obtenerDatos(self):
        for video in self.videos:
            if self.tipo == 'Pelicula':
                mayorV = video.getMaxV(Pelicula.maxV)
            elif self.tipo == 'Serie':
                mayorV = video.getMaxV(Serie.maxV)

    
class Video():
    def __init__(self, n, cv, a) -> None:
        self.nombre = n
        self.cantV = cv
        self.actores = a
    
    def getMaxV(self, contP, contS):
        if contP > contS:
            print(f'El video mas visto es {Pelicula.self.nombre}')
        else:
            print(f'El video mas visto es {Serie.self.nombre}')
    
class Pelicula(Video):
    def __init__(self, n, cv, a, m) -> None:
        super().__init__(n, cv, a)
        self.minutos = m
        contP = 0
        if self.cantV > contP:
            contP = self.cantV

class Serie(Video):
    def __init__(self, n, cv, a, temp) -> None:
        super().__init__(n, cv, a)
        self.temporadas = temp
        contS = 0
        if self.cantV > contS:
            contS = self.cantV

        

plataformaPelis = [ Plataforma('Pelicula', [("Inmortales"), (35), ('Mirtha Legrand,Carlitos Balá,Elizabeth The Second'), (30)])
Plataforma('Pelicula', [("Inception"), (17319533),( 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt'), (148)])
Plataforma('Pelicula', [("Batman Begins"),(4760183), ('Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine'), (140)])
]
plataformaPelis.obtenerDatos()


plataformaSerie = [ Plataforma('Serie', ["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6])
Plataforma('Serie', ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4])
]
