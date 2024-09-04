class Plataforma:
    def __init__(self) -> None:
        pass
class Video:
    def __init__(self, nombre, visualizaciones, actores) -> None:
        self.nombre = nombre
        self.visualizaciones = visualizaciones
        self.actores = actores 
    
    def mayor_visualizaciones(self):
        acumulador = 0
        for elemento in videos:
            if elemento[1] > acumulador:
                acumulador = elemento[1]
        return elemento[0]
                
class Pelicula(Video):
    def __init__(self, nombre, visualizaciones, actores, duracion) -> None:
        super().__init__(nombre, visualizaciones, actores)
        self.duracion = duracion
class Serie(Video):
    def __init__(self, nombre, visualizaciones, actores, temporadas) -> None:
        super().__init__(nombre, visualizaciones, actores)
        self.temporadas = temporadas

videos = ["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4], ["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]

series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]
pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

#   Video con mayor numero de visualizaciones:
acumulador = 0
for elemento in videos:
    if elemento[1] > acumulador:
        acumulador = elemento[1]
        video_mas_visto = elemento[0]
print(f"El video mas visto:\n{video_mas_visto}")

#   Series que tienen menos de 5 temporadas:
for serie in series:
    if serie[3] < 5:
        print(f'Series que tienen menos de 5 temporadas:\n {serie[0]}')

#   Actores
actores = []

for serie in series:
    actores_serie = serie[2].split(',')
    actores.append(actores_serie)
    
for peli in pelis:
    actores_peli = peli[2].split(',')
    actores.append(actores_peli)

print(actores)