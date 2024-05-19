datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]




#Actividad 1. nombres con ". "
lista_nombres = []

for persona in datos:
    apellido, nombre = persona.split(",")[:2] 
    nombre = nombre[1] 
    lista_nombres.append(nombre + '. ' + apellido)

for nombre in lista_nombres:
    print(nombre)
nombres = []

for i in datos:
    nombre = i.split(',')[1:2]
    nombres += nombre




#Actividad 2. nombre mas largo
cantidad_caracteres = 0
nombre_mas_largo = ''

for i in range(len(nombres)):
    for j in range(len(nombres[i])):
        if j > cantidad_caracteres:
            nombre_mas_largo = nombres[i]
            cantidad_caracteres = j
            
print('El nombre mas largo es:' + nombre_mas_largo)

fechas = []
for i in datos:
    fecha = i.split(',')[3:]
    fechas += fecha
 
 
    
#Actividad 3. promedio de edad mujeres
hoy = 2024

edades = []

for persona in datos:
    partes = persona.split(", ")
    if partes[2] == "f":
        año_nacimiento = int(partes[3].split("/")[2])
        edades.append(hoy - año_nacimiento)


suma_edades = 0
for edad in edades:
    suma_edades += edad

promedio_edad = suma_edades / len(edades)

print("El promedio de edad de las mujeres es", int(promedio_edad), "años.")

    
    

    
    



    
    

    



    
    
    











