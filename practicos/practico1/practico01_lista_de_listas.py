datos = [
    ["Torres, Ana", "f", "02/05/1943"], # persona 1
    ["Hudson, Kate", "f", "07/04/1984"], # persona 2
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]

# Construir listas de apellidos y nombres
apellidos = []
nombres = []
fechas = []
sexos = []
for persona in datos:
    nombreCompleto = persona[0]
    apellido, nombre = nombreCompleto.split(', ')
    apellidos.append(apellido)
    nombres.append(nombre)
    sexo = persona[1]
    fecha = persona[2]
    fechas.append(fecha)
    sexos.append(sexo)

print('1) Obtener iniciales y apellidos')
for i in range(len(apellidos)):
    inicialYapellido = nombres[i][0] + '. ' + apellidos[i]
    print(inicialYapellido)

print('2) Obtener el nombre de pila más largo')
nombreMasLargo = ''
for nombre in nombres: # para cada persona en la lista de datos
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre
print(nombreMasLargo)

print('3) Obtener el promedio de edad de las mujeres')
diaHoy, mesHoy, aniHoy = 9, 5, 2024
totalEdades = 0
contadorMujeres = 0
for x in range(len(fechas)):
    if sexos[x] == 'f':
        contadorMujeres += 1
        f = fechas[x]
        diaNac, mesNac, aniNac = int(f[:2]), int(f[3:5]), int(f[6:])
        edad = aniHoy - aniNac
        if (mesNac > mesHoy) or (mesNac == mesHoy and diaNac > diaHoy):
            edad -= 1
        totalEdades += edad
print(int(totalEdades/contadorMujeres))








