class Persona():
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Abogado(Persona):
    def __init__(self, nombre, matricula) -> None:
        super().__init__(nombre)
        self.matricula = matricula

a = Abogado('Juan', 11111)




