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

#Ejercicio 1

for nombre in range(len(nombres)):
    nombreCompleto = nombres[nombre].split(", ")
    apellido = nombreCompleto[0]
    nombreSeparados = nombreCompleto[1].split(" ")
    inicial = nombreSeparados[0][0]
    print(inicial,apellido)

#Ejercicio 2
nombreMasLargo = ""

for nombre in nombres: 
    nombrePersona = nombre.split(", ")[1]
    if len(nombrePersona) > len(nombreMasLargo):
        nombreMasLargo = nombrePersona

print("El nombre más largo es: ",nombreMasLargo)

#Ejercicio 3



sumaEdades = 0
contador = 0
anioActual = 2024  

for i in range(len(sexos)):
    if sexos[i] == "f":
        fechaNacimiento = fechas[i].split('/')
        dia = int(fechaNacimiento[0])
        mes = int(fechaNacimiento[1])
        anio = int(fechaNacimiento[2])
        edad = anioActual - anio
        if mes > 5 :  
            edad = edad - 1
        sumaEdades = edad + sumaEdades
        contador = contador + 1

if contador > 0:
    promedio = sumaEdades // contador
    print("El promedio de edad de las mujeres es:", promedio)
else:
    print("No hay mujeres en la lista.")