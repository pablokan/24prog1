#Se me ataron todos los animales juntos..

bandas = [
["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]

solistas = [
["Peter Gabriel", 10, 17319533,70], 
["Jeff Beck", 3, 1023998, 76]]

class Musicos():
    def __init__(self,nombre,cantidaddealbumes,cantidaddereproducciones) -> None:
        self.nombre=nombre
        self.cantidaddealbumes= cantidaddealbumes
        self.cantidaddereproducciones = cantidaddereproducciones


class Banda(Musicos):
    def __init__(self, nombre, cantidaddealbumes, cantidaddereproducciones,integrantes) -> None:
        super().__init__(nombre, cantidaddealbumes, cantidaddereproducciones)
        
        self.integrantes = integrantes

    def nombreCantante (self):
        pass

class Solista(Musicos):
    def __init__(self, nombre, cantidaddealbumes, cantidaddereproducciones,edad) -> None:
        super().__init__(nombre, cantidaddealbumes, cantidaddereproducciones)

        self.edad = edad
    def solistaMayor (self,solista):
        if solista ("Peter Gabriel") > ("Jeff Beck"):
            return ("Peter es el solista mas antiguo")
        else:
            return ("Jeff es el solista mas antiguo")

class Plataforma:
    def reprodTotal(self,reproduccion):
        self.reprod = Banda("Led Zeppelin", 9, 123456)
        self.reprod2 = Banda("Rage Against the Machine", 4, 243490)
        self.reprod3 = Banda("Seru Giran", 5, 32419)
        self.solista1 = Solista ("Peter Gabriel", 10, 17319533)
        self.solista2 = Solista ("Jeff Beck", 3, 1023998)
    
    def mayorCantAlb(self):
        pass

    def nombreCantante(self):
        pass
    
