class Bicicleta:
    def __init__(self, tipo, color) -> None:
        self.tipo = tipo
        self.color = color


miBiciPlayera = Bicicleta('playera', 'celeste')
tuBiciDeCarrera = Bicicleta('de carrera', 'negra')

print(f'Mi bici es una {miBiciPlayera.tipo} de color {miBiciPlayera.color}')
print(f'Tu bici es una {tuBiciDeCarrera.tipo} de color {tuBiciDeCarrera.color}')
