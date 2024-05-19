
# Datos

nombres = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana",
    "Santamaría, Carlos",
    "Skarsgard, Azul",
    "Catalejos, Walter"
]

sexos = ["f", "f", "m", "f", "m", "f", "m"]
fechas = [
    "02/05/1943",
    "07/04/1984",
    "10/02/1971",
    "21/12/1967",
    "30/01/1982",
    "30/08/1995",
    "18/07/1959"
]

# Proceso 1: Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
 
print("Iniciales y Apellido de las personas: ")
for nombre in nombres:
    apellido, primerNombre = nombre.split(", ")
    inicial = primerNombre[0]
    print(f"{inicial}. {apellido}")
"""
# El 2 no me sale profe

# Proceso 3: Mostrar el promedio de edad de las mujeres

edadesMujeres = []
for i in range(len(fechas)):
    if sexos[i]  == "f":
        nacimiento = int(fechas)
        edad = 2024 - nacimiento
        edadesMujeres

# Y... No se como seguirlo
"""