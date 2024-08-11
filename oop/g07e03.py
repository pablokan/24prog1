class Persona:
    def __init__(self, n) -> None:
        self.nombre = n

personas: list[Persona] = []
hayMas = 's'

while hayMas == 's':
    n = input('Nombre: ')
    p = Persona(n)
    personas.append(p)
    hayMas = input('Hay mas?: ')

for persona in personas:
    print(persona.nombre)

