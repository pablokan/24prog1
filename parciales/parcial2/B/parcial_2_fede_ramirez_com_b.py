# descripcion de cada clase (perro y gato)
class mascota: 
    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años"

class perro(mascota):
    def descripcion(self):
        estadoAnimo = "contento" if self.movercolaRapido else "triste"
        return f"{super().descripcion()}, es un {self.raza} que lleva un collar {self.colorCollar} de {self.materialCollar} y está {estadoAnimo}."

class gato(mascota):
    def descripcion(self):
        estadoAnimo = "tiene hambre" if self.maullar else "no tiene hambre"
        genero = "gata" if self.sexo == "hembra" else "gato"
        return f"{super().descripcion()}, es una {genero} {self.color} y {estadoAnimo}."

bobby = perro()
bobby.nombre = "bobby"
bobby.edad = 3
bobby.raza = "rottweiler"
bobby.colorCollar = "rojo"
bobby.materialCollar = "cuero"
bobby.movercolaRapido = False

toffee = perro()
toffee.nombre = "toffee"
toffee.edad = 5
toffee.raza = "ovejero alemán"
toffee.colorCollar = "negro"
toffee.materialCollar = "tela"
toffee.movercolaRapido = True

grisina = gato()
grisina.nombre = "grisina"
grisina.edad = 4
grisina.sexo = "hembra"
grisina.color = "gris"
grisina.maullar = False

shevek = gato()
shevek.nombre = "shevek"
shevek.edad = 1
shevek.sexo = "macho"
shevek.color = "naranja"
shevek.maullar = True

print(bobby.descripcion())
print(toffee.descripcion())
print(grisina.descripcion())
print(shevek.descripcion())
