class Mascotas():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def devolverNoEd(self):
        return self.nombre, self.edad
    
class Perro(Mascotas):
    def __init__(self, nombre, edad, raza, colorCollar, material):
        super().__init__(nombre, edad)
        self.raza = raza
        self.colorCollar = colorCollar
        self.material = material

class Gato(Mascotas):
    def __init__(self, nombre, edad, sexo, color):
        super().__init__(nombre, edad)
        self.sexo = sexo
        self.color = color

class EstadoAnimo():
    def __init__(self):
        self.listaPerros = []
        self.listaGatos = []
        self.listaEstadoP = []
        self.listaEstadoG = []
        
        preg = "si"

        while preg == "si":
            self.animal = input("¿De que animal se trata? (Perro/Gato)")
            if self.animal.upper() == "PERRO":
                print("DATOS PERRO: ")
                name = input("Nombre del perro: ")
                edad = int(input("Ingrese la edad: "))
                raza = input("Ingrese la raza: ")
                cCollar = input("¿Cual es el color del collar?: ")
                material = input("¿Y el material?: ")
                estado = input("¿El perro mueve la cola rapido? (si/no): ")
                if estado == "si":
                    self.listaEstadoP.append("está contento")
                else:
                    self.listaEstadoP.append("esta triste")

                perrito = Perro(name, edad, raza, cCollar, material)
                self.listaPerros.append(perrito)

                preg = input("¿Quiere seguir agregando animales? (si/no): ")
            else:
                print("DATOS GATO: ")
                name = input("Nombre del gato: ")
                edad = int(input("Ingrese la edad: "))
                sexo = input("¿Cual es el sexo del gato? (gato/gata): ")
                color = input("Color del gato: ")
                estado = input("¿El gato maulla? (si/no): ")
                if estado == "si":
                    self.listaEstadoG.append("tiene hambre")
                else:
                    self.listaEstadoG.append("no tiene hambre")

                gatito = Gato(name, edad, sexo, color)
                self.listaGatos.append(gatito)

                preg = input("¿Quiere seguir agregando animales? (si/no): ")

    def mostrarDatos(self):
        for x in range(len(self.listaPerros)):
            print(f"{self.listaPerros[x].nombre} tiene {self.listaPerros[x].edad} años, es un {self.listaPerros[x].raza} que lleva un collar {self.listaPerros[x].colorCollar} de {self.listaPerros[x].material} y {self.listaEstadoP[x]}.")
        for x in range(len(self.listaGatos)):
            print(f"{self.listaGatos[x].nombre} tiene {self.listaGatos[x].edad} años, es una {self.listaGatos[x].sexo} {self.listaGatos[x].color} y {self.listaEstadoG[x]}.")

animales = EstadoAnimo()
animales.mostrarDatos()

