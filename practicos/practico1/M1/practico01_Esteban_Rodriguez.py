# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
# 2) Decir cuál es el nombre de pila más largo.
# 3) Mostrar el promedio de edad de las mujeres.


cadenas_nombre_apellido = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana", 
    "Santamaría, Carlos",
    "Skarsgard, Azul", 
    "Catalejos, Walter"
]

pila_mas_largo = ""

for nombre in cadenas_nombre_apellido:
    apellido, nombre_completo = nombre.split(", ")
    inicial_nombre = nombre_completo[0]

    if len(apellido) > len(pila_mas_largo):
        pila_mas_largo = apellido

    print(inicial_nombre + ". " + apellido)

print("El apellido más largo es:", pila_mas_largo)
