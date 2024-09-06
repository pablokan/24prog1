#CepedaCaceresEmanuel
#Parcial 2
class Musica:
    def __init__(self, nombre, cantDiscos, cantReproducciones) -> None:
        self.nombre = nombre
        self.cantDiscos = cantDiscos
        self.cantReproducciones = cantReproducciones
class Banda(Musica):
    def __init__(self, nombre, cantDiscos, cantReproducciones, integrantes) -> None:
        super().__init__(nombre, cantDiscos, cantReproducciones)
        self.integrantes = integrantes


    def mostrarCantantes(self):
        cantantes = []
        for integrante in self.bandas:
            for integ in self.integrantes: 
                if '(voz)' in integ:
                    cantantes.append(integ.nombre)
        print('Los nombres de los cantantes de las bandas son: ')
        for i in range(len(cantantes)):
            if i < len(cantantes):
                print(f'{cantantes[i]},')
            else:
                print(f'y {cantantes[i]}')
    
    
class Solista(Musica):
    def __init__(self, nombre, cantDiscos, cantReproducciones, edad) -> None:
        super().__init__(nombre, cantDiscos, cantReproducciones)
        self.edad = edad

    def antiguo(self):
        antiguo = 0
        for solista in self.solistas:
            if solista.edad > antiguo:
                antiguo = solista.edad
                salida = solista.nombre
        return f'El solista más viejo es: {salida}'

class Spotify:
    bandas = []
    solistas = []
    antiguo = ''
    cantantes = ''
    
    def cargaBanda(self):
        validez = 's'
        while validez == 's':
            nombre = input('Ingrese el nombre de la banda: \n').capitalize()
            discos = int(input('Cuantos discos tienen: \n'))
            reproducciones = int(input('Cuantas reproducciones tiene: \n'))
            validacion = 's'
            integrantes = []
            while validacion == 's':
                integ = input(f'Ingrese nombre de integrante de la banda {nombre}\nSi es el cantante agregue "(voz)": \n')
                integrantes.append(integ)
                validacion = input('carga otro integrante? (s/n)\n').lower()
            banda = Banda(nombre, discos, reproducciones, integrantes)
            self.bandas.append(banda)
            validez = input('Cargar otra banda (S/N)\n').upper()

    def cargaSolista(self):
        validez = 's'
        while validez == 's':
            nombre = input('Ingrese el nombre del solista: \n').capitalize()
            discos = int(input('Cuantos discos tienen: \n'))
            reproducciones = int(input('Cuantas reproducciones tiene: \n'))
            edad = int(input('Ingrese la edad: \n'))
            solista = Solista(nombre, discos, reproducciones, edad)
            antiguo = solista.antiguo()
            self.bandas.append(solista)
            validez = input('Cargar otra solista (S/N)\n').upper()

    def masAlbums(self):
        album = ''
        cantb = 0
        cants = 0
        for disco in self.bandas:
            if disco.cantDiscos > cantb:
                cantb = disco.cantDiscos
                discbanda = disco.nombre 
        for disco in self.solistas:
            if disco.cantDiscos > cants:
                cants = disco.cantDiscos
                discsolis = disco.nombre 
        if cantb > cants:
            album = discbanda
        else:
            album = discsolis 

        return f'El nombre de la banda o el solista con mayor cantidad de álbumes es: {self.album}'
    
    def masReproducido(self):
        total = 0
        for repro in self.bandas:        
            total += repro.cantReproducciones 
        for solis in self.solistas:
            total += solis.cantReproducciones
        return f'Total de reproducciones del sitio: {total}'

#    def mostrarDatos(self):
#        antiguo = 

spotify = Spotify()
spotify.cargaBanda()
spotify.cargaSolista()
spotify.masReproducido()
spotify.antiguo()
spotify.mostrarCantantes()
spotify.masAlbums()







        




