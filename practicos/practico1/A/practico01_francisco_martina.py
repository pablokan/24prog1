
datos = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/04/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]
print("-----------------------------------------------")
print("Iniciales y apellido de las personas: ")
for personas in datos:
    nombre_completo = personas[0].split(", ")
    nombre = nombre_completo [1][0] + ". " + nombre_completo [0]
    print(nombre)
print("-----------------------------------------------")
nombre_mas_largo = ""
for persona in datos:
    nombre_completo = persona [0].split (", ")[1]
    nombres = nombre_completo.split()
    for nombre in nombres:
        if len(nombre) > len(nombre_mas_largo):
            nombre_mas_largo = nombre

print ("El nombre de pila mas largo es: " , nombre_mas_largo)
print("-----------------------------------------------")

edades_mujeres = []
for persona in datos:
    if persona[1] == "f": 
        fecha_nacimiento = persona[2].split("/")
        edad = 2024 - int(fecha_nacimiento[2])
        edades_mujeres.append(edad)

if len(edades_mujeres) > 0:
    promedio_edad_mujeres = sum(edades_mujeres) // len(edades_mujeres)
    print ("El promedio de edad de las mujeres es:", promedio_edad_mujeres)
else:
    print("No hay mujeres en la lista de datos.")
print("-----------------------------------------------")
