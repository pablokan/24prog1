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


for nombrecomp in nombres:
    apellido, nombre = nombrecomp.split(", ") # el split lo uso para que divida el apellido del nombre
    inicial_nombre = nombre[0].upper() # el upper para q tome la inicial
    print(f"Inicial: {inicial_nombre}, {nombrecomp} ")

nlargo = ""

for nombrecomp in nombres:
    apellido, nombre = nombrecomp.split(", ")
    if len(nombre) > len(nlargo):
        nlargo = nombre

print(f"El nombre de pila más largo es: {nlargo}")