#Mostrar las iniciales de los nombres con un punto, luego un espacio 
#y finalmente el apellido completo de todas las personas.

datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]


for i in datos:
    nombre = i.split(", ")[1][0]
    apellido = i.split(", ")[0]  
    print(nombre + ".", apellido)

    nombreLargo= ""
for dato in datos:
    nombre = dato.split(", ")[1] 
    if len(nombre) > len(nombreLargo):
        nombreLargo = nombre

print("El nombre más largo es: ", nombreLargo)

total = 0
cont = 0
for dato in datos:
    persona = dato.split(", ")
    if persona[2] == "f":  
        fecha = persona[3].split("/")
        nacimiento = int(fecha[2])
        total += 2024 - nacimiento
        cont += 1
        promedio = total / cont

print("El promedio de edad de las mujeres es:", promedio)