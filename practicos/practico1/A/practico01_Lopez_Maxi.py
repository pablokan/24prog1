"""
Procesos para las salidas:

1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

2) Decir cuál es el nombre de pila más largo.

3) Mostrar el promedio de edad de las mujeres. 

Realizar tres procesos separados!
(Pueden hacer 4 procesos si les parece conveniente en primer lugar obtener los nombres y apellidos separados y almacenarlos en listas)

"""

nombres = ["Torres, Ana",
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

#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
nombreIniciales = []
for nombre in nombres:
    nombreSinComa = nombre.split(", ")
    inicial = nombreSinComa[1][0] + "."
    nombreIniciales.append(inicial + " " + nombreSinComa[0])

for apellido in nombreIniciales:
    print(apellido)

#2) Decir cuál es el nombre de pila más largo.

nombreMasLargo = ""
for nombre in nombres:
    nombreSinComa = nombre.split(", ")
    nombrePila = nombreSinComa[1]
    if len(nombrePila) > len(nombreMasLargo):
        nombreMasLargo = nombrePila

print("El nombre de pila más largo es:", nombreMasLargo)

#3) Mostrar el promedio de edad de las mujeres. 

listaEdadesMujeres = []
for i in range (len(sexos)):
    if sexos[i] == 'f':
        listaEdadesMujeres.append(fechas[i])

fechaActual ='02/05/2024'
parteFechaActual = fechaActual.split("/")
diaActual = int(parteFechaActual[0])
mesActual = int(parteFechaActual[1])
aActual = int(parteFechaActual[2])
promedio = 0
for diaMesA in listaEdadesMujeres:
    parteFechaNacimiento = diaMesA.split("/")
    diaNac = int(parteFechaNacimiento[0])
    mesNac = int(parteFechaNacimiento[1])
    aNac = int(parteFechaNacimiento[2])
    edad = aActual - aNac
    if mesActual < mesNac or (mesActual == mesNac and diaActual < diaNac):
        edad -= 1
    promedio = promedio + edad
promedio = promedio // len(listaEdadesMujeres)
print('El promedio de edades de mujeres es: ', promedio, 'años')
