# 2do Parcial - Programación I
# Alumno: Blengino, Giuliano
# Comisión: A

class Plataforma():
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.bandas = []
        self.solistas = []

        bandas = [
        ["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
        ["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
        ["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
        ]
        solistas = [
        ["Peter Gabriel", 10, 17_319_533,70], 
        ["Jeff Beck", 3, 1_023_998, 76]
        ]

        for banda in bandas:
            agBanda = Banda(banda[0],banda[1],banda[2],banda[3])
            self.bandas.append(agBanda)
        
        for solista in solistas:
            agSolista = Solista(solista[0],True,solista[1],solista[2],solista[3])
            self.solistas.append(agSolista)
        
    def totalReproducciones(self):
        totRepr = 0
        for banda in self.bandas:
            totRepr += banda.cReproducciones
        for solista in self.solistas:
            totRepr += solista.cReproducciones
        return totRepr
    
    def cantantesBandas(self):
        cantantes = []
        msg = ''
        for banda in self.bandas:
            for musico in banda.musicos:
                if musico.cantante == True:
                    nombre = musico.nombre
                    cantantes.append(nombre)
        
        for i in range(len(cantantes)-2):
            msg += cantantes[i] + ', '
        msg += cantantes[len(cantantes)-2]
        msg += ' y ' + cantantes[len(cantantes)-1]

        return msg

    def artistaConMasAlbumes(self):
        artista = ''
        cAlbumes = 0

        for banda in self.bandas:
            if banda.cAlbumes > cAlbumes:
                cAlbumes = banda.cAlbumes
                artista = banda.nombre

        for solista in self.solistas:
            if solista.cAlbumes > cAlbumes:
                cAlbumes = solista.cAlbumes
                artista = solista.nombre

        return artista
    
    def solistaMasViejo(self):
        solista = ''
        edad = 0

        for solista in self.solistas:
            if solista.edad > edad:
                edad = solista.edad
                solista = solista.nombre

        return solista

    

class Banda():
    def __init__(self,nom,cAlbum,cRepr,int) -> None:
        self.nombre = nom
        self.cAlbumes = cAlbum
        self.cReproducciones = cRepr
        self.musicos = []
        integrantes = int.split(', ')
        for musico in integrantes:
            if musico.find('(voz)') != -1:
                musico = Musico(musico[:-6],True)
            else:
                musico = Musico(musico)
            self.musicos.append(musico)
    
class Musico():
    def __init__(self,nombre,cantante=False) -> None:
        self.nombre = nombre
        self.cantante = cantante

class Solista(Musico):
    def __init__(self, nombre,cantante,cAlbum,cRepr,edad) -> None:
        super().__init__(nombre,cantante)
        self.cAlbumes = cAlbum
        self.cReproducciones = cRepr
        self.edad = edad

platMusica = Plataforma('SpotiTune')

print(f'---- {platMusica.nombre} ----')
print('')
print(f'Total de reproducciones del sitio: {platMusica.totalReproducciones()}')
print('')
print(f'El solista más viejo es: {platMusica.solistaMasViejo()}')
print('')
print(f'Los nombres de los cantantes de las bandas son:\n{platMusica.cantantesBandas()}')
print('')
print(f'El nombre de la banda o solista con mayor cantidad de álbumes es: {platMusica.artistaConMasAlbumes()}')