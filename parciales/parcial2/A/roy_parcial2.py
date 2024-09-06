# Necesitamos saber:
#  La suma total de reproducciones de todos (bandas y solistas, un solo total final).
#  El apellido del solista más viejo.
#  Los nombres de los cantantes de las bandas.
#  El nombre de la banda o el solista con mayor cantidad de álbumes.


class Artista():
    def __init__(self, nombre, cantAlbumes, cantRepro) -> None:
        self.nombre = nombre
        self.cantAlbumes = cantAlbumes
        self.cantRepro = cantRepro

    def masAlbumes(self):  #metodo abstracto, lo voy a usar en otras clases mas abajo profe
        pass

    def reproduccionesTotales(self):
        self.cant = 0
        reproTotales = 0
        for pers in self.listBandas:
             self.cant = self.cant + pers[2]
             reproTotales = self.cant       

class Banda(Artista):
    def __init__(self, integrantes) -> None:
        super().__init__(nombre, cantAlbumes, cantRepro)
        self.integrantes = integrantes

    def mostrarBandas(self):
        for pers in self.listBandas:
         print(pers.nombre)

     

class Solista(Artista): 
    def __init__(self, edad) -> None:
        super().__init__(nombre, cantAlbumes, cantRepro)
        self.edad = edad
        
    def masAlbumes(self):
        aux = 0
        aux2 = ''
        for pers in listBandas:
            if aux >= pers.cantAlbumes :
              aux2 = pers.nombre
              aux = pers.cantAlbumes
        return aux2    

    

    def Oldest(self):  #METODO PARA SABER EL SOLISTA MAS VIEJO
        aux = 0
        masViejo = ''
        for pers in self.listBandas:
            aux = pers.edad
            if (aux >= pers.edad): 
                masViejo = self.nombre
                aux = pers.edad  #actualizo la variable auxiliar 
        print(f'El solista mas viejo es: {masViejo}')

 

class Main():  #CLASE PRINCIPAL
    bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
    solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]
    
    def __init__(self) -> None:   
        self.listBandas = []
        for persona in self.solistas:
            self.nombre = persona[0]
            self.cantAlbumes = persona[1]
            self.cantRepro = persona[2]
            self.edad = persona[3]
            self.listBandas.append(Solista(self.nombre, self.cantAlbumes, self.cantRepro, self.edad))  #INSTANCIACION obj

        for persona in bandas:
            self.nombre = persona[0]
            self.cantAlbumes = persona[1]
            self.cantRepro = persona[2]
            self.integrantes = persona[3]
            self.listBandas.append(Banda(nombre, cantAlbumes, cantRepro, integrantes))    #INSTANCIACION obj

            
inicio = Main()
#inicio.mostrarBandas() """