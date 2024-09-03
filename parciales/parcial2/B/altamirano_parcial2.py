




class Mascota():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrarDatos(self):
        print(f'{self.nombre} tiene {self.edad} años')


class Perro(Mascota):
    def __init__(self, nombre, edad, raza, collarColor, collarMaterial):
        super().__init__(nombre, edad)
        self.raza = raza
        self.collarColor = collarColor
        self.collarMaterial = collarMaterial


    def datosPerro(self):
        print(f'{self.nombre} tiene {self.edad} años, lleva un collar de color {self.collarColor} y es de {self.collarMaterial}')


class Gato(Mascota):
    def __init__(self, nombre, edad, sexo, color):
        super().__init__(nombre, edad)
        self.sexo = sexo
        self.color = color


    def datosGato(self):
        print(f'{self.nombre} tiene {self.edad} años, es de sexo {self.sexo} y es de color {self.color}')








perro1 = Perro("Bobby",3,"rottweiler","rojo","cuero")
perro2 = Perro("Toffee", 5, "ovejero aleman", "negro", "tela")
perro1.datosPerro()
perro2.datosPerro()

gato1 = Gato("Grisina", 4, "femenino", "gris")
gato2 = Gato("Shevek", 1, "masculino", "naranja")
gato1.datosGato()
gato2.datosGato()

