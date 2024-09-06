bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]


class Musicos:
    def __init__(self, musicos, solistas):
        self.nombres_musicos = [nombres[3] for nombres in musicos]
        self.solistas = solistas

    def solista_mas_viejo(self):
        apellido_solista = ''
        edad_mayor = 0
        for solista in self.solistas:
            if solista[3] > edad_mayor:
                edad_mayor = solista[3]
                apellido_solista = solista[0]
        print(f'El solista más viejo es: {apellido_solista}')
    
    def solista_mayor_reproducciones(self):
        mayor_reproduccion = 0
        for solista in self.solistas:
            if solista[2] > mayor_reproduccion:
                mayor_reproduccion = solista[2]
        return mayor_reproduccion

class Banda:
    def __init__(self, bandas):
        self.bandas = bandas
        self.nombres_bandas = [banda[0] for banda in bandas]
        self.nombres_musicos = [nombres[3] for nombres in bandas]
    
    def obtener_cantantes(self):
        lista_cantantes = []
        for musicos in self.nombres_musicos:
            lista_musicos = musicos.split(", ")
            cantantes = [musico for musico in lista_musicos if "(voz)" in musico]
            lista_cantantes.append(cantantes)
        print(f'Los nombres de los cantantes de las bandas son: {lista_cantantes}')

    def obtener_nombre_banda_mayor_reproduccion(self):
        mayor_reproduccion = 0
        for banda in self.bandas:
            if banda[2] > mayor_reproduccion:
                mayor_reproduccion = banda[2]
        return mayor_reproduccion

class Aplicacion:
    def __init__(self,bandas, musicos):
        self.bandas = bandas
        self.musicos = musicos
    
    """ def total_reproducciones(self):
        total_banda = self.bandas.obtener_nombre_banda_mayor_reproduccion()
        total_solista = self.musicos.solista_mayor_reproducciones()
        if total_banda < total_solista:
            print(f'El nombre de la banda o el solista con mayor cantidad de álbumes es: {total_solista}')
        else:
            print(f'El nombre de la banda o el solista con mayor cantidad de álbumes es: {total_banda}')
 """


musicos = Musicos(bandas, solistas)
musicos.solista_mas_viejo()
banda = Banda(bandas)
banda.obtener_cantantes()
banda.obtener_nombre_banda_mayor_reproduccion()
app = Aplicacion(bandas,solistas)
#app.total_reproducciones()

