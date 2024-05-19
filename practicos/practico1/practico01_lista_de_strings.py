datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]

print('1) Obtener iniciales y apellidos')
for persona in datos:
    posiComa = persona.find(',')
    iYa = persona[posiComa+2] + '. ' + persona[:posiComa]
    print(iYa)

print('2) Obtener el nombre de pila más largo')
nombreMasLargo = ''
for persona in datos:
    posiComa1 = persona.find(',')
    posiComa2 = persona.find(',', posiComa1+1)
    nombre = persona[posiComa1+2:posiComa2]
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre
print(nombreMasLargo)

print('3) Obtener el promedio de edad de las mujeres')
diaHoy, mesHoy, aniHoy = 9, 5, 2024
totalEdades = 0
contadorMujeres = 0
for persona in datos:
    if persona[-13] == 'f':
        contadorMujeres += 1
        f = persona[-10:]
        diaNac, mesNac, aniNac = int(f[:2]), int(f[3:5]), int(f[6:])
        edad = aniHoy - aniNac
        if (mesNac > mesHoy) or (mesNac == mesHoy and diaNac > diaHoy):
            edad -= 1
        totalEdades += edad
print(int(totalEdades/contadorMujeres))





        

