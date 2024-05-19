# PRÁCTICO 01 - Programación I
# Alumno: Blengino, Giuliano
# Fecha: 02/05/2024

nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 
sexos = ["f","f","m","f","m","f","m"]
fechas = [
"02/05/1943",
"07/04/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]

# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

print('Iniciales y apellido de las personas:')
print('')
for i in range(len(nombres)):
    nombreApellido = nombres[i].split(', ')
    nombre = nombreApellido[1]
    nombre = nombre[:1] + '.'
    print(nombre, nombreApellido[0])

cantNombreMasLargo = 0

# 2) Decir cuál es el nombre de pila más largo.

for i in range(len(nombres)):
    nombreApellido = nombres[i].split(', ')
    nombreActual = nombreApellido[1]
    cantLetrasNombre = len(nombreActual)
    if cantLetrasNombre > cantNombreMasLargo:
        cantNombreMasLargo = cantLetrasNombre
        nombreMasLargo = nombreActual

print('')
print('El nombre mas largo es:', nombreMasLargo)

# 3) Mostrar el promedio de edad de las mujeres. 

totalEdadMujeres = 0
cantidadMujeres = 0

for i in range(len(nombres)):
    if sexos[i] == 'f':
        cantidadMujeres += 1
        fechaNacimiento = fechas[i].split('/')
        diaNacimiento = int(fechaNacimiento[0])
        mesNacimiento = int(fechaNacimiento[1])
        añoNacimiento = int(fechaNacimiento[2])
        if mesNacimiento <= 5 and diaNacimiento <= 2:
            edadMujer = 2024 - añoNacimiento
            totalEdadMujeres = totalEdadMujeres + edadMujer
        else:
            edadMujer = 2023 - añoNacimiento
            totalEdadMujeres = totalEdadMujeres + edadMujer

promedioEdadMujeres = totalEdadMujeres // cantidadMujeres

print('')
print('El promedio de edad de las mujeres es:', promedioEdadMujeres)
        