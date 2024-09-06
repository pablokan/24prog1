class Artistas():
    def __init__(self, nombre, discos, reproducciones) -> None:
        self.nombre = nombre
        self.discos = discos
        self.reproducciones = reproducciones

class Solistas(Artistas):
    def __init__(self, nombre, discos, reproducciones, edad) -> None:
        super().__init__(nombre, discos, reproducciones)
        self.edad = edad

class Integrantes():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        if "(voz)" in self.nombre:
            self.cantante = True
            ubiCorte = self.nombre.find("(")
            self.nombre = self.nombre[:ubiCorte]
        else:
            self.cantante = False



class Bandas(Artistas):
    def __init__(self, nombre, discos, reproducciones, integrantes) -> None:
        super().__init__(nombre, discos, reproducciones)
        self.integrantes = [Integrantes(i) for i in integrantes]


class Plataforma():
        

    def __init__(self) -> None:
            banda1 = Bandas("Led Zeppelin", 9, 123456,["Jimmy Page", "Robert Plant (voz)", "John Bonham", "John Paul Jones"])
            banda2 = Bandas("Rage Against the Machine", 4, 243490,["Zack de la Rocha(voz)", "Tom Morello", "Tim Commerford"])
            banda3 = Bandas("Seru Giran", 5, 32419,["Pedro Aznar", "Oscar Moro", "David Lebón (voz)", "Charly García (voz)"] )
            self.listBandas =  [banda1, banda2, banda3]

            solista1 = Solistas("Peter Gabriel", 10, 17_319_533,70)
            solista2 = Solistas("Jeff Beck", 3, 1_023_998, 76)
            self.listSolistas =  [solista1, solista2]
    
    def cantReproducciones(self):
        reproducciones = 0
        for banda in self.listBandas:
            reproducciones = banda.reproducciones + reproducciones

        for solista in self.listSolistas:
            reproducciones = solista.reproducciones + reproducciones
    
        return reproducciones
    
    def edadesSolistas(self):
        mayorEdad = 0
        for solista in self.listSolistas:
            if solista.edad > mayorEdad:
                mayorEdad = solista.edad
                nombreMasViejo = solista.nombre
            
        return nombreMasViejo
    
    def nombresCantantes(self):
        for banda in self.listBandas:
            for integrante in banda.integrantes:
                if integrante.cantante:
                    print(integrante.nombre)

    def mayorCantidadDeAlbumes (self):
        mayorCantidad = 0
        for banda in self.listBandas:
            if banda.discos > mayorCantidad:
                mayorCantidad = banda.discos
                nombre = banda.nombre
            
            for solista in self.listSolistas:
                if solista.discos > mayorCantidad:
                    mayorCantidad = solista.discos
                    nombre = solista.nombre
            
        return nombre
    

spotify = Plataforma()
cantidadReproducciones = spotify.cantReproducciones()
print(f'la cantidad de reproducciones son: {cantidadReproducciones}')
print("-"*32)
solistaMasViejo = spotify.edadesSolistas()
print(f'el solista mas viejo es: {solistaMasViejo}')
print("-"*32)
print('los cantantantes de las bandas son: ')
spotify.nombresCantantes()
print("-"*32)
masDiscos = spotify.mayorCantidadDeAlbumes()
print(f"El nombre de la banda o el solista con mayor cantidad de álbumes es: {masDiscos}")