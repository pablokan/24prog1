#listas con datos
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

#Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
for i in range(len(nombres)):
    apellido, nombre = nombres[i].split(', ')
    inicial = nombre[0]
    print(inicial + '. ' + apellido)


#Decir cuál es el nombre de pila más largo.
nombre_mas_largo = ''
for nombre in nombres:
    apellido, nombre = nombre.split(", ")
    if len(nombre) > len(nombre_mas_largo):
        nombre_mas_largo = nombre
print('el nombre de pila mas largo es:', nombre_mas_largo)


#Mostrar el promedio de edad de las mujeres. 
contador_mujeres = 0
suma_edades = 0

for i in range(len(nombres)):
    fecha_nacimiento = fechas[i]
    #slicing para separar dia, mes, año
    dd = int(fecha_nacimiento[:2])
    mm = int(fecha_nacimiento[3:5])
    aaaa = int(fecha_nacimiento[6:])
    if sexos[i] == 'f':
        contador_mujeres = contador_mujeres + 1
        edad = 2024 - aaaa # Calcular la edad
        suma_edades = suma_edades + edad
if contador_mujeres > 0:
    promedio = suma_edades / contador_mujeres
print('el prmedio de edad de las mujeres es:', int(promedio))