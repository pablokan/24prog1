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

listaNombres = []
listaApellidos = []


#1
for i in range(len(nombres)):
    apellido, nombre = nombres[i].split(',')
    listaApellidos.append(apellido)
    listaNombres.append(nombre)
print("Iniciales y apellidos de las personas:")
for i in range(len(listaNombres)):
    inicial = listaNombres[i][1]
    apellido = listaApellidos[i]
    print(inicial + ". " + apellido)




#2
cantMin = 2
for i in range(len(listaNombres)):
    nombre = listaNombres[i]
    cantidad = len(nombre) - 1 # Le resto el espacio en blanco que está al comienzo de cada nombre
    if cantidad > cantMin:
        cantMin = cantidad
        nombreMasLargo = nombre
print("")
print("El nombres mas largo es: ",nombreMasLargo)
    


#3
diaHoy, mesHoy, anioHoy = 30, 4, 2024
sumaEdades = 0
cantMujeres = 0
for i in range(len(sexos)):
    s = sexos[i]
    diaNac, mesNac, anioNac = fechas[i].split('/')
    diaNac, mesNac, anioNac = int(diaNac), int(mesNac), int(anioNac)
    edad = anioHoy - anioNac
    if s == 'f':
        sumaEdades = sumaEdades + edad
        cantMujeres = cantMujeres + 1
promEdad = sumaEdades // cantMujeres
print("")
print("El promedio de edad de las mujeres es: ",promEdad)