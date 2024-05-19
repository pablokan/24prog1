# Datos de personas
personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]

opcion = input("Ingrese 'año' o 'país': ").lower()

if opcion == 'año':
    año = int(input("Ingrese año: "))
    print("Los apellidos de las personas nacidas antes del", año, "son:")
    for persona in personas:
        nombre_apellido, _, fecha_nacimiento = persona.split(',')
        año_nacimiento = int(fecha_nacimiento[-4:])
        if año_nacimiento < año:
            apellido = nombre_apellido.split()[-1]
            print(apellido)
elif opcion == 'país':
    pais = input("Ingrese país: ")
    cantidad = sum(1 for persona in personas if pais in persona)
    print("La cantidad de personas de", pais, "es", cantidad)
else:
    print("Opción no válida.")

mas_joven_europeo = None
edad_mas_joven = float('inf')

for persona in personas:
    nombre, pais_continente, fecha_nacimiento = persona.split(',')
    if 'Europe' in pais_continente:
        año_nacimiento = int(fecha_nacimiento[-4:])
        if año_nacimiento < edad_mas_joven:
            mas_joven_europeo = nombre.split()[0]
            edad_mas_joven = año_nacimiento

if mas_joven_europeo:
    print("La persona más joven de Europe es", mas_joven_europeo)
else:
    print("No hay personas de Europe en la lista.")
