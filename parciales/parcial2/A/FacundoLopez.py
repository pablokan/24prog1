bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]


solistas = [
["Peter Gabriel", 10, 17_319_533,70], 
["Jeff Beck", 3, 1_023_998, 76]
]


class Persona():
    pass

class Solista(Persona):
    def __init__(self) -> None:
        self.edad = []
        self.reproducciones = []
        self.nombres = []
        self.albums = []
        
        for i in range(len(solistas)):
            self.albums.append(solistas[i][1])
        
        for i in range(len(solistas)):
            self.nombres.append(solistas[i][0])
        
        
        for i in range(len(solistas)):
            self.reproducciones.append(solistas[i][2])
            
        for i in range(len(solistas)):
            self.edad.append(solistas[i][3])
            
    def getReproducciones(self):
        return self.reproducciones
            
        
    def mayorSolista(self):
        mayor = 0
        nombreMayor = ""
        for i in range(len(self.edad)):
            if self.edad[i] > mayor:
                nombreMayor = self.nombres[i]
        print(f"El solista más viejo es: {nombreMayor}")
            



class BandasRock():
    def __init__(self) -> None:
        self.nombre = []
        self.integrantes = []
        self.reproducciones = []
        self.albums = []
        
        for i in range(len(bandas)):
            self.albums.append(bandas[i][1])
        
        
        for i in range(len(bandas)):
            self.nombre.append(bandas[i][0])
   
        for i in range(len(bandas)):
            self.reproducciones.append(bandas[i][2])
        
        for i in range(len(bandas)):
            self.integrantes.append(bandas[i][3])
            
    def getReproducciones(self):
        print(self.reproducciones)
        
        
class PlataformaMusical():
    def __init__(self) -> None:
        self.bandas = BandasRock()
        self.solistas = Solista()
        
    def reproduccionesTotales(self):
        acumuladorB = 0
        acumuladorS = 0
        for r in self.bandas.reproducciones:
            acumuladorB += int(r)
        
        for r in self.solistas.reproducciones:
            acumuladorS += int(r)       
        print(f"Total de reproducciones del sitio: {acumuladorB + acumuladorS}")
        
        
    def masAlmbums(self):
        mayor = 0
        mayorBandas = ""
        for i in range(len(self.bandas.albums)):
            if int(self.bandas.albums[i]) > mayor:
                mayorBandas = self.bandas.nombre[i]
                
        mayors = 0
        mayorSolista = ""
        for i in range(len(self.solistas.albums)):
            if int(self.bandas.albums[i]) > mayors:
                mayorSolista = self.solistas.nombres[i]
            
        if mayorSolista > mayorBandas:
            print(f"El nombre de la banda o el solista con mayor cantidad de álbumes es: {mayorSolista}")
        else:
            print(f"El nombre de la banda o el solista con mayor cantidad de álbumes es: {mayorBandas}")
             
            
            
        

Spotify = PlataformaMusical()
Spotify.reproduccionesTotales()
Spotify.solistas.mayorSolista()
Spotify.masAlmbums()