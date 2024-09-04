'''
Importante: 

Respetar la consigna, pero sobre todo, incluir los conceptos principales de orientación a objetos trabajados:
HERENCIA y COMPOSICIÓN 

Subir el programa resuelto hasta un minuto antes de la hora especificada. 
Estará DESHABILITADA LA OPCIÓN DE SUBIR EL PROGRAMA FUERA DE HORA.
Se sube el programa con lo mucho o poco que se haya podido escribir!

Enunciado:
Se crea una plataforma de videos con películas y series tipo Netflix.
Se dispone de los siguientes datos (Listas iniciales posibles):

series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]

pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]
]

Cada sublista contiene: nombre, cantidad de visualizaciones y actores. El cuarto dato son las temporadas en el caso de las series y la duración en minutos en el caso de las películas.
Pueden desarmar y rearmar estas listas como les resulte más cómodo.

Importante: Las estructuras con los datos iniciales (listas, diccionarios o cualquier combinación de almacenamiento, sean las propuestas aquí o las construidas por ustedes) solamente pueden usarse para la instanciación de las series y películas. NO para la algoritmia posterior que debe trabajar sobre los objetos.

Necesitamos saber:

El video (película o serie) de mayor número de visualizaciones.
Los nombres de los actores que figuran en series y también en películas.
Las series que tienen menos de 5 temporadas.
Realizar al menos un método para cada uno de los puntos pedidos.

Salida esperada:
El video mas visto: Inception

Actores que trabajan en series y películas:  
- Cillian Murphy
- Ellen Page

Series que tienen menos de 5 temporadas:  
- The Umbrella Academy
'''

class Video:
    def __init__(self):
        series = [["Peaky Blinders", 1234567, 'Cillian Murphy,Paul Anderson,Helen McCrory', 6], ["The Umbrella Academy", 2434908, 'Tom Hopper,Emmy Raver-Lampman,Ellen Page,David Castañeda', 4]]
        self.masVistoSeries = 0
        self.actoresInd = []
        self.menosTemporadasSerie = []
        for i in series:
            self.nomSerie = i[0]
            self.visualSerie = i[1]
            self.actoresSerie = i[2]
            self.capitulosSerie = i[3]
            actorSerie = self.actoresSerie.split(',')
            for j in actorSerie:
                self.actoresInd.append(j)
            if self.visualSerie > self.masVistoSeries:
                self.masVistoSeries = self.visualSerie
            if self.capitulosSerie > 5:
                self.menosTemporadasSerie.append(self.nomSerie)

                print(self.nomSerie, self.visualSerie, self.actoresSerie, self.capitulosSerie, actorSerie)

        pelis = [["Inmortales", 35, 'Mirtha Legrand,Carlitos Balá,Elizabeth The Second', 30],["Inception", 17319533, 'Leonardo DiCaprio,Ellen Page,Joseph Gordon-Levitt', 148], ["Batman Begins",4760183, 'Christian Bale,Leonardo DiCaprio,Cillian Murphy,Michael Caine', 140]]
        self.masVistoPelis = 0
        for i in pelis:
            for j in i:
                self.nomPeli = i[0]
                self.visualPeli = i[1]
                self.actoresPeli = i[2]
                self.actorPeli = self.actoresPeli.split(',')
                minutosPeli = i[3]
                if self.visualPeli > self.masVistoPelis:
                    self.masVistoPelis = self.visualPeli
                print(self.nomPeli, self.visualPeli, self.actoresPeli, minutosPeli)
    def actoresSerieyPeli(self):
        if self.actoresInd in self.actorPeli:
            actor = self.actoresInd
            print(f'Los actores que aparecen en series y en peliculas son {actor}')

    def menosTemporadas(self):
        return self.menosTemporadasSerie
    
    def masVisto(self):
        if self.masVistoSeries > self.masVistoPelis:
            self.loMasVisto = self.masVistoSeries
            print(f'El video mas visto es: {self.loMasVisto}')
        else:
            self.loMasVisto = self.masVistoPelis
            print(f'El video mas visto es: {self.loMasVisto}')

class Serie(Video):
    def __init__(self, nom, vis, act, cap):
        super().__init__()
        self.nom = nom
        self.visualSerie = vis
        self.actoresSerie = act
        self.capitulosSerie = cap

class Peli(Video):
    def __init__(self, nom, vis, act, mints):
        super().__init__()
        self.nom = nom
        self.visualPeli = vis
        self.actoresPeli = act
        self.capitulosPeli = mints

s = Video()
s.mostrarSerie()
s.masVisto()
s.menosTemporadas()