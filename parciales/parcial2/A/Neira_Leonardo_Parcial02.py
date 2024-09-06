#Sistema tipo spotify Neira Leonardo

class Artistas:
    def __init__(self, nombre, albunes, reprodu):
        self.nombre = nombre
        self.CantAlbunes = albunes
        self.Reprodu = reprodu
    def nombreArtista(self):
        return self.nombre
    def totalAlbunes(self):
        return self.CantAlbunes
    def cantReprodu(self):
        return self.Reprodu
class Banda(Artistas):
    def __init__(self, nombre, albunes, reprodu, integrantesBanda):
        super().__init__(nombre, albunes, reprodu)
        self.integrantesBanda = integrantesBanda
    def nombresIntegrantes(self):
        return self.integrantesBanda
class Solista(Artistas):
    def __init__(self, nombre, albunes, reprodu, edad):
        super().__init__(nombre, albunes, reprodu)
        self.edad = edad
    def edadSolista(self):
        return self.edad
bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]
IniciarBandas = [Banda(*banda) for banda in bandas]
IniciarSolistas= [Solista(*solista) for solista in solistas]
def sumarCantReprodu(bandas, solistas):
    SumaReprodu= 0
    for banda in bandas:
        SumaReprodu += banda.cantReprodu()
    for solista in solistas:
        SumaReprodu += solista.cantReprodu()
    return SumaReprodu
def solistaViejo(solistas):
    SolistaMasViejo = solistas[0]
    for solista in solistas:
        if solista.edadSolista() > SolistaMasViejo.edadSolista():
            SolistaMasViejo = solista
    return SolistaMasViejo.nombreArtista()
def nombreCantantes(bandas):
    NombreCantantes = []
    for banda in bandas:
        integrantes = banda.nombresIntegrantes().split(",")
        for integrante in integrantes:
            if "(voz)" in integrante:
                NombreCantantes.append(integrante.split("(")[0])
    return NombreCantantes
def nombreMasAlbunes(bandas, solistas):
    NombreMasAlbunes = bandas[0]
    for banda in bandas:
        if banda.totalAlbunes()> NombreMasAlbunes.totalAlbunes():
            NombreMasAlbunes = banda
    for solista in solistas:
        if  solista.cantReprodu() > NombreMasAlbunes.cantReprodu():
            NombreMasAlbunes = solista
    return NombreMasAlbunes.nombreArtista()
print("Total de reproducciones: ", sumarCantReprodu(IniciarBandas, IniciarSolistas))
print("Nombre del solista mas viejo es: ", solistaViejo(IniciarSolistas))
print("Nombre de los cantantes de las bandas: ", nombreCantantes(IniciarBandas))
print("El que tiene mas albunes es: ", nombreMasAlbunes(IniciarBandas, IniciarSolistas))