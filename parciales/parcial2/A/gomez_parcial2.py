bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]

class Banda():
    def __init__(self, nombre, albumes, reproducciones) -> None:
        self.nombre = nombre
        self.albumes = albumes
        self.reproducciones = reproducciones

    def cargaIntegrantes(self, integrantes):
        self.integrantes = integrantes

class Solista(Banda):
    def __init__(self, nombre, cantAlbum, reproducciones, edad) -> None:
        super().__init__(nombre, cantAlbum, reproducciones)
        self.edad = edad

class Spotify():
    def __init__(self) -> None:
        self.listaBandas = []
        self.listaSolistas = []

    def cargaBandas(self, bandas):
        for i in range(len(bandas)):
            nombre = bandas[i][0]
            albumes = bandas[i][1]
            reproducciones = bandas[i][2]
            self.listaBandas.append(Banda(nombre, albumes, reproducciones))

    def cargaSolistas(self, solistas):
        for i in range(len(solistas)):
            nombre = solistas[i][0]
            albumes = solistas[i][1]
            reproducciones = solistas[i][2]
            edad = solistas[i][3]
            self.listaSolistas.append(Solista(nombre, albumes, reproducciones, edad))

    def cargaIntegrantesBandas(self, bandas):
        for i in range(len(bandas)):
            integrantes = bandas[i][3]
            self.listaBandas[i].cargaIntegrantes(integrantes)

    def reproduccionesTotales(self):
        reprBandas = 0
        reprSolistas = 0
        for banda in self.listaBandas:
            reprBandas += banda.reproducciones
        for solista in self.listaSolistas:
            reprSolistas += solista.reproducciones
        reprTotales = reprBandas + reprSolistas
        print(f'Total de reproducciones del sitio: {reprTotales}')

    def solistaMasViejo(self):
        masViejo = 0
        self.apMasViejo = ''
        for solista in self.listaSolistas:
            _, apellido = solista.nombre.split(' ')
            if solista.edad > masViejo:
                masViejo = solista.edad
                self.apMasViejo = apellido
        print(f'El apellido del solista mas viejo es: {self.apMasViejo}')

    def mostrarCantantesBandas(self):
        listaIntegrantes = []
        listaCantantes = []
        for banda in self.listaBandas:
            listaIntegrantes = banda.integrantes.split(', ')
            for i in range(len(listaIntegrantes)):
                if '(voz)' in listaIntegrantes[i]:
                    posi = listaIntegrantes[i].find('(')
                    cantante = listaIntegrantes[i][0:posi]
                    listaCantantes.append(cantante)
        print('Los nombres de los cantantes de las bandas son: ')
        for cantante in listaCantantes:
            print(cantante)
            
    def mayorAlbumes(self):
        mayCantAlb = 0
        self.nombreMasAlb = ''
        for banda in self.listaBandas:
            if banda.albumes > mayCantAlb:
                mayCantAlb = banda.albumes
                self.nombreMasAlb = banda.nombre
        for solista in self.listaSolistas:
            if solista.albumes > mayCantAlb:
                mayCantAlb = solista.albumes
                self.nombreMasAlb = solista.nombre
        
        print(f'El nombre de la banda o el solista con mayor cantidad de albumes es: {self.nombreMasAlb}')

spoti = Spotify()
spoti.cargaBandas(bandas)
spoti.cargaIntegrantesBandas(bandas)
spoti.cargaSolistas(solistas)
spoti.reproduccionesTotales()
spoti.solistaMasViejo()
spoti.mostrarCantantesBandas()
spoti.mayorAlbumes()

#Con respecto al metodo mostrarCantantesBandas(), no estoy seguro de haberlo resuelto bien ya que resuelvo el metodo modificando estos datos en especifico, de ser otra lista la cual los cantantes no tengan especificado (voz), no se podria resolver de esta manera. Fue lo que pude pensar y resolver con el tiempo que tenia. Saludos