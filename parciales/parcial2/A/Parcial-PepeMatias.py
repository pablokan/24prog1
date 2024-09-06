# Parcial Programacion - Pepe Matias
bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]

class Artistas():
    def __init__(self, nombre, cA, cR) -> None:
        self.nombre = nombre
        self.cantidadAlbumes = cA
        self.cantidadReproducciones = cR
    
class Bandas(Artistas):
    def __init__(self, nombre, cA, cR, integrantes) -> None:
        super().__init__(nombre, cA, cR)
        self.integrantes = integrantes 

class Solistas(Artistas):
    def __init__(self, nombre, cA, cR, edad) -> None:
        super().__init__(nombre, cA, cR)
        self.edad = edad 

class Spotify():
    def __init__(self) -> None:
        self.bandas = [Bandas("Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"),      Bandas("Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"),
                       Bandas("Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)")]
        
        self.solistas = [Solistas("Peter Gabriel", 10, 17_319_533,70),
                         Solistas("Jeff Beck", 3, 1_023_998, 76)]
        
    def sumaReproducciones(self):
        aux = 0 
        for i in range(len(self.bandas)):
            aux += int(self.bandas[i].cantidadReproducciones)
        for j in range(len(self.solistas)):
            aux += int(self.solistas[j].cantidadReproducciones)
        print(f'Total de reproducciones del sitio: {aux}')

    def solistaMV(self):
        masviejo = ''
        ed = 0
        for i in range(len(self.solistas)):
            if (self.solistas[i].edad > ed):
                masviejo = self.solistas[i].nombre
        print(f'El solista más viejo es: {masviejo}')

    def nombresCantantes(self):
        cantTotal = ''
        aux = []
        posi = 0 
        for i in range (len(self.bandas)):
            aux = self.bandas[i].integrantes.split(',')
            for j in range (len(aux)):
                posi = aux[j].find('(')
                if (posi > 0):
                    cantTotal += aux[j][:posi]
        print(f'Los nombres de los cantantes de las bandas son: {cantTotal}')

        

    def mayCantAlbum(self):
        n = ''
        aux = 0
        for i in range(len(self.bandas)):
            if (self.bandas[i].cantidadAlbumes > aux):
                n = self.bandas[i].nombre    
                aux = self.bandas[i].cantidadAlbumes
        
        for j in range (len(self.solistas)):
            if (self.solistas[j].cantidadAlbumes > aux):
                n = self.solistas[j].nombre
                aux = self.solistas[j].cantidadAlbumes
        print(f'El nombre de la banda o el solista con mayor cantidad de álbumes es: {n}')

        
s = Spotify()
s.sumaReproducciones()
s.solistaMV()
s.nombresCantantes()
s.mayCantAlbum()
