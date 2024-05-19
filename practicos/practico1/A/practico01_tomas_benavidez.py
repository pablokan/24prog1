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

#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

apellidos = []

for i in range (len(nombres)):
    ubicacionApellido = nombres[i].find(",")
    ape = nombres[i][0:ubicacionApellido]
    ini = nombres[i][ubicacionApellido +2:ubicacionApellido + 3]
    inicialApellido = ini + ". " + ape
    apellidos.append(inicialApellido)

for x in range (len(apellidos)):
    print(apellidos[x])

print("")
print("")
#2) Decir cuál es el nombre de pila más largo.

nom = []

for t in range (len(nombres)):
    ubicacionNombre = nombres[t].find(" ")
    nombre = nombres[t][ubicacionNombre +1:]
    nom.append(nombre)

mayorLong = 0
contador = 0
for n in nom:
    if len(n) > mayorLong:
        mayorLong = len(n)
        nombreMasLargo = n

print(nombreMasLargo)

print("")
print("")

#3) Mostrar el promedio de edad de las mujeres

diaHoy = input("ingrese que numero del dia de hoy: ")
diaHoy = int(diaHoy)
mesHoy = input("ingrese que numero del mes estamos: ")
mesHoy = int(mesHoy)
añoHoy = input("ingrese en que año estamos: ")
añoHoy = int(añoHoy)

dias = []
meses = []
años = []

for q in range (len(fechas)):
    ubiDias = fechas[i].find("/")
    ubiMes = ubiDias + 1
    ubiAños = ubiMes + 3
    dia = fechas[q][0:ubiDias]
    dia = int(dia)
    dias.append(dia)
    mes = fechas[q][ubiMes:ubiAños - 1]
    mes = int(mes)
    meses.append(mes)
    año = fechas[q][ubiAños:] 
    año = int(año)
    años.append(año)





edades = []

for k in range(len(años)):
    if meses[k] > mesHoy:
        edad = (añoHoy - años[k]) - 1
    elif meses[k] == meses and dia[k] > diaHoy:
        edad = (añoHoy - años[k]) - 1
    else:
        edad = añoHoy - años[k]

    edades.append(edad)



sumaEdades = 0
contadorMujeres = 0
for j in range (len(edades)):
    if (sexos[j] == "f"):
        sumaEdades = sumaEdades + edades[j]
        contadorMujeres = contadorMujeres + 1

promedioEdadesMujeres = sumaEdades / contadorMujeres

promedioEdadesMujeres = int(promedioEdadesMujeres)

print ("el promedio de la edad de las mujeres es: ", promedioEdadesMujeres)



