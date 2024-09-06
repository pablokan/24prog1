"""
Importante: 

Respetar la consigna, pero sobre todo, 

incluir los conceptos principales de orientación a objetos trabajados:

HERENCIA y COMPOSICIÓN 

Subir el programa resuelto hasta un minuto antes de la hora especificada. 

Estará DESHABILITADA LA OPCIÓN DE SUBIR EL PROGRAMA FUERA DE HORA.

Se sube el programa con lo mucho o poco que se haya podido escribir!


Enunciado:

Se crea una plataforma de música tipo Spotify.

Se dispone de los siguientes datos (Listas iniciales posibles):

bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]


Cada sublista contiene: nombre, cantidad de álbumes y cantidad de reproducciones. El cuarto dato son los integrantes en el caso de las bandas y la edad en el caso de los solistas.

Pueden desarmar y rearmar estas listas como les resulte más cómodo.

Importante: Las estructuras con los datos iniciales (listas, diccionarios o cualquier combinación de almacenamiento, sean las propuestas aquí o las construidas por ustedes) solamente pueden usarse para la instanciación de las bandas y los solistas. NO para la algoritmia posterior que debe trabajar sobre los objetos.


Necesitamos saber:

La suma total de reproducciones de todos (bandas y solistas, un solo total final).
El apellido del solista más viejo.
Los nombres de los cantantes de las bandas.
El nombre de la banda o el solista con mayor cantidad de álbumes.

Realizar al menos un método para cada uno de los puntos pedidos.

Salida esperada:

Total de reproducciones del sitio: 18742896

El solista más viejo es: Jeff Beck

Los nombres de los cantantes de las bandas son:
Robert Plant, Zach de la Rocha, David Lebón y Charly García

El nombre de la banda o el solista con mayor cantidad de álbumes es:
Peter Gabriel



"""
class Artista:
    def __init__(self, nombre, cantAlbumes, cantReproducciones, tipo):
        self.nombre = nombre
        self.cantAlbumes = cantAlbumes
        self.cantReproducciones = cantReproducciones
        self.tipo = tipo


class Banda(Artista):
    def __init__(self, nombre, cantAlbumes, cantReproducciones, integrantes, tipo):
        super().__init__(nombre, cantAlbumes, cantReproducciones, tipo)
        self.integrantes = integrantes

class Solista(Artista):
    def __init__(self, nombre, cantAlbumes, cantReproducciones, edad, tipo):
        super().__init__(nombre, cantAlbumes, cantReproducciones, tipo)
        self.edad = edad

class Disco:
    def __init__(self, bandas, solistas) -> None:
        self.listadoArtistas = []
        self.listaBandas = bandas
        self.listaSolistas = solistas
        for dato in self.listaBandas:
            self.listadoArtistas.append(Banda(dato[0], dato[1], dato[2], dato[3], 'Banda'))
      
        for dato in self.listaSolistas:
            self.listadoArtistas.append(Solista(dato[0], dato[1], dato[2], dato[3], 'Solista'))
        

    def totalReproducciones(self):
        total = 0
        print(f'Listado de reproducciones')
        for dato in self.listadoArtistas:
            if dato.tipo == 'Banda':
                total += dato.cantReproducciones
            else:
                total += dato.cantReproducciones
        print(f'Total de reproducciones del sitio: {total}')


    def masViejo(self):
        viejo = ''
        edad = 0
        for dato in self.listadoArtistas:
            if dato.tipo == 'Solista':
                if dato.edad > edad:
                    edad = dato.edad
                    viejo = dato.nombre
        print(f'El solista más viejo es: {viejo} y tiene {edad}')
                

    def cantantesBanda(self):
        for dato in self.listadoArtistas:
            if dato.tipo == 'Banda':
                print(f'Los cantantes de {dato.nombre} son: {dato.integrantes}')
    

    def masAlbumes(self):
        cant = 0
        mas = ''
        for dato in self.listadoArtistas:
            if dato.cantAlbumes >= cant:
                cant = dato.cantAlbumes
                mas = dato.nombre
        print(f'El nombre de la banda o solista con mayor cantidad de ambumes es: {mas} con {cant} albumes')

            
    
bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]

disco = Disco(bandas, solistas)
disco.totalReproducciones()
disco.cantantesBanda()
disco.masAlbumes()
disco.masViejo()