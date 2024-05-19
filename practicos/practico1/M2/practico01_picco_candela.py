""""""
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


inicialesApellidos = []
print("1 Iniciales y apellidos de las personas: ")
for nombre in nombres:
    apellido, nombre = nombre.split(", ")
    inicial = nombre[0]
    inicialesApellidos.append(f"{inicial}. {apellido}")

for nombre in inicialesApellidos:
    print(nombre)
""""""
""""""
nombres = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana",
    "Santamaría, Carlos",
    "Skarsgard, Azul",
    "Catalejos, Walter"
]

nombre_mas_largo = ""

for nombre in nombres:
    nombre_actual = nombre.split(", ")[1]
    if len(nombre_actual) > len(nombre_mas_largo):
        nombre_mas_largo = nombre_actual

print("2 El nombre más largo es:", nombre_mas_largo)
""""""
#el punto 3 no me di ceunta como sacarlo y pasarlo en codigo 