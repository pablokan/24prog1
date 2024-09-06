bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]



class Plataforma:
    def __init__(self, bandas, solistas) -> None:
        self.bandas = bandas
        self.solistsa = solistas
        super().__init__()


class Banda(Plataforma):
    bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
    def __init__(self, nombre, cantidadAlbum, cantidadReproducciones, integrantes) -> None:
        self.nombre = nombre
        self.cantidadAlbum = cantidadAlbum
        self.cantidadReproducciones = cantidadReproducciones
        self.integrantes = integrantes
        super().__init__(nombre, cantidadAlbum, cantidadReproducciones, integrantes)


class Solista(Plataforma):
    solistas = [
["Peter Gabriel", 10, 17_319_533, 70], 
["Jeff Beck", 3, 1_023_998, 76]
]
    def __init__(self, nombre, cantidadAlbum, cantidadReproducciones, edad) -> None:
        self.nombre = nombre
        self.cantidadAlbum = cantidadAlbum
        self.cantidadReproducciones = cantidadReproducciones
        self.edad = edad
        super().__init__()