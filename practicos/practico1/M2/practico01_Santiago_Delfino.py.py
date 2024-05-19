""" Procesos para las salidas:
1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
2) Decir cuál es el nombre de pila más largo.
3) Mostrar el promedio de edad de las mujeres. 
 """
#Listas paralelas:
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

#act1
nombreSeparadoDeApellido = []

for nombrePunto in nombres:
    partes = nombrePunto.split(", ")
    inicialNombre = partes[1][0]
    apellido = partes[0]
    nombreSeparadoDeApellido.append(f"{inicialNombre}. {apellido}")

for nombre in nombreSeparadoDeApellido:
    print(nombre)
#act2
nombreMasLargo = "" 
for nombrePunto in nombres:
    partes = nombrePunto.split(", ")
    nombre = partes[1]
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre

print("el nombre mas largo de la lista es el de: ", nombreMasLargo)

#act3
totalEdadesMujeres = 0
numMujeres = 0
totalEdadesMujeres = 0
numMujeres = 0

añoActual = 2024

for i in range(len(nombres)):
    if sexos[i] == "f":
        añoNacimiento = int(fechas[i][-4:])
        edad = añoActual - añoNacimiento
        totalEdadesMujeres += edad
        numMujeres += 1
        
if numMujeres > 0:
    promedioEdadMujeres = totalEdadesMujeres // numMujeres
    print("el promedio de edad de las mujeres es de: ", promedioEdadMujeres)
else:
    print("no hay mujeres")
