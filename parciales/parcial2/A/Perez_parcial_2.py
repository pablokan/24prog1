class Cantante:
    def __init__(self,nom) -> None:
        self.nombre = nom

class Banda:
    def __init__(self, nom, alb, rep, inte) -> None:
        self.nombre = nom
        self.album = alb
        self.reproducciones =rep
        self.integrantes = inte


class Solista(Cantante):
    def __init__(self, nom, alb, rep,edad) -> None:
        super().__init__(nom)
        self.album = alb
        self.reproducciones =rep
        self.edad = edad

class Sitio:
    def __init__(self) -> None:
        self.solista1 = Solista("Peter Gabriel", 10, 17319533,70)
        self.solista2 = Solista("Jeff Beck", 3, 1023998, 76) 
        self.banda1 = Banda("Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones")
        self.banda2 = Banda("Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford")
        self.banda3 = Banda("Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)")
        self.totalSitio = [self.solista1,self.solista2,self.banda1,self.banda2,self.banda3]
        self.solistas = [self.solista1,self.solista2]
        self.bandas = [self.banda1,self.banda2,self.banda3]

    def total_Rep (self):
        reproduccion = 0
        for musico in self.totalSitio:
            reproduccion = musico.reproducciones + reproduccion
        print(f'Total de reproducciones del sitio: {reproduccion}')

    def viejo(self):
        edades = 0
        for solista in self.solistas:
            if solista.edad > edades:
                edades = solista.edad
                nombre = solista.nombre
        print(f'El solista más viejo es: {nombre}')

    def masAlbumes(self):
        albumes = 0
        for musico in self.totalSitio:
            if musico.album > albumes:
                albumes = musico.album
                nombre = musico.nombre
        print(f'El nombre de la banda o el solista con mayor cantidad de álbumes es: {nombre}')

    def voz (self):
        solo_cantantes = []
        for banda in self.bandas:
            integran = banda.integrantes.split(',')
            
            for inte in integran:
                
                if 'voz' in inte:
                   solo_cantantes.append(inte[0:inte.find('(voz)')])
        print('Los nombres de los cantantes de las bandas son:')
        for cantantes in solo_cantantes:
            print (cantantes)
                   






spoti = Sitio()
spoti.total_Rep()
spoti.viejo()
spoti.voz() 
spoti.masAlbumes()
     
        







