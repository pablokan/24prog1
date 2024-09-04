class Video:
    def __init__(self, nombre, visualizaciones, actores, durOtemp):
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores.split(',')
        self.durOtemp=durOtemp

    def videoMasVisto(videos):
        maxVideo = videos[0] 
        for video in videos:
            if video.visualizaciones > maxVideo.visualizaciones:
                maxVideo = video
        return maxVideo.nombre
class Serie(Video):
    def __init__(self, nombre, visualizaciones, actores, durOtemp):
        super().__init__(nombre, visualizaciones, actores, durOtemp)
class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, actores, durOtemp):
        super().__init__(nombre, visualizaciones, actores, durOtemp)
series = [
    ["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6],
    ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]
]

peliculas = [
    ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],
    ["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148],
    ["Batman Begins", 4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]
videos = [Serie(*s) for s in series] + [Pelicula(*p) for p in peliculas]
print(f"el video de mayor visualizacion es {Video.videoMasVisto(videos)}")












