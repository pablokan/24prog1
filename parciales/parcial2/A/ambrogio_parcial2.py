#1 La suma total de reproducciones de todos (bandas y solistas, un solo total final).
#2 El apellido del solista más viejo.
#3 Los nombres de los cantantes de las bandas.
#4 El nombre de la banda o el solista con mayor cantidad de álbumes.

#nombre, cantidad de albumes, cantidad de reproducciones, integrantes (en bandas) y edad (en solistas)

class Artista:
    def __init__(self, nombre, albumes, reproducciones):
        self.nombre = nombre
        self.albumes = albumes
        self.reproducciones = reproducciones

class Banda(Artista):
    def __init__(self, nombre, albumes, reproducciones, integrantes):
        super().__init__(nombre, albumes, reproducciones)
        self.integrantes = integrantes

    def cantantes(self):
        cantantes = []  
        for integrante in self.integrantes:
            if "(voz)" in integrante:
                nombre = integrante.split()[0]
                cantantes.append(nombre)  
        return cantantes

class Solista(Artista):
    def __init__(self, nombre, albumes, reproducciones, edad):
        super().__init__(nombre, albumes, reproducciones)
        self.edad = edad

def crear_artistas(datos_bandas, datos_solistas):
    artistas = []
    for nombre, albumes, reproducciones, integrantes in datos_bandas:
            banda = Banda(nombre, albumes, reproducciones, integrantes)
            artistas.append(banda)
            
    for nombre, albumes, reproducciones, edad in datos_solistas:
            solista = Solista(nombre, albumes, reproducciones, edad)
            artistas.append(solista)
    return artistas

datos_bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
datos_solistas = [
["Peter Gabriel", 10, 17_319_533, 70], 
["Jeff Beck", 3, 1_023_998, 76]
]

artistas = crear_artistas(datos_bandas, datos_solistas)

total_reproducciones = sum(artista.reproducciones for artista in artistas) #total reproducciones
print("total de reproducciones:", total_reproducciones)

cantantes_mas_albumes = (artista.albumes for artista in artistas)

