bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]

solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]


# La suma total de reproducciones de todos (bandas y solistas, un solo total final).
# El apellido del solista más viejo.
# Los nombres de los cantantes de las bandas.
# El nombre de la banda o el solista con mayor cantidad de álbumes.
class Musicos():
    def __init__(self,nombre,albunes,reproducciones):
        self.nombre = nombre
        self.albunes = albunes
        self.reproducciones = reproducciones



class Solistas(Musicos):
    def __init__(self, nombre, albunes, reproducciones,edad):
        self.edad = edad
        super().__init__(nombre, albunes, reproducciones)


class Bandas(Musicos):
    def __init__(self, nombre, albunes, reproducciones,integrantes):
        super().__init__(nombre, albunes, reproducciones)
        self.integrantes = integrantes


class Plataforma():
    def __init__(self,nombre,bandas,solistas):
        self.nombre = nombre
        self.listaBandas = []
        self.listaSolistas = []
        self.bandas = bandas
        self.solistas = solistas

        for i in range(len(self.bandas)):
            obj = Bandas(bandas[i][0],bandas[i][1],bandas[i][2],bandas[i][3])
            self.listaBandas.append(obj) 
        for i in range(len(self.solistas)):
            obj = Solistas(solistas[i][0],solistas[i][1],solistas[i][2],solistas[i][3])
            self.listaSolistas.append(obj)


    def mostarTodo(self):
        for obj in self.listaBandas:
            print(f'Banda: {obj.nombre},albunes: {obj.albunes} //Reproducciones: {obj.reproducciones} Intengrantes:{obj.integrantes}')
        print('')
        
        for obj in self.listaSolistas:
            print(f'nombre: {obj.nombre},albunes: {obj.albunes} //Reproducciones: {obj.reproducciones} Edad: {obj.edad}')
    def totalReprod(self):
        repoducB = 0 
        for i in range(len(self.listaBandas)):
            repoducB += self.listaBandas[i].reproducciones
        repoducS = 0
        for i in range(len(self.listaSolistas)):
            repoducS += self.listaSolistas[i].reproducciones     
        self.total = repoducB + repoducS
        return print(f'Total de reproducciones del sitio: {self.total}')
    # El apellido del solista más viejo.
    def solistaMasViejo(self):
        self.solistaAnciano = 0
        self.apellidoAnciano = ''
        for obj in self.listaSolistas:
            pos = obj.nombre.find(' ')
            if self.solistaAnciano < obj.edad :
                self.solistaAnciano = obj.edad
                self.apellidoAnciano = obj.nombre
        return print(f'El solista más viejo es: {self.apellidoAnciano[:pos]}')
    # Los nombres de los cantantes de las bandas
    # en desarrollo...
    def nameCantante(self):
        self.integrantes = []
        for obj in self.listaBandas:
            self.integrantes.append(obj.integrantes)
        
        
        for i in range(len(self.integrantes)):
            integrante = self.integrantes[i].split(',')
            integrans = []
            for i in range(len(integrante)):
                integran = integrante[i].split(',')
                integrans.append(integran)
                print(integran)        
    
    





spotify = Plataforma('Spotify',bandas,solistas)
spotify.mostarTodo()
spotify.totalReprod()
spotify.solistaMasViejo()
spotify.nameCantante()

# for i in range(len(bandas)):
#     obj = Bandas(bandas[i][0],bandas[i][1],bandas[i][2],bandas[i][3])
#     listaObjetos.append(obj)


# for obj in listaObjetos:
#     print(f'Banda: {obj.nombre},albunes: {obj.albunes} //Reproducciones: {obj.reproducciones} Intengrantes: {obj.integrantes}')

# listaSolistas = []

# for i in range(len(solistas)):
#     obj = Solistas(solistas[i][0],solistas[i][1],solistas[i][2],solistas[i][3])
#     listaSolistas.append(obj)



