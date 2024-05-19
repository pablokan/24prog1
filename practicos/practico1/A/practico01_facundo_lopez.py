
# Listas paralelas:

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


# Separar nombres
soloNombres = ""
soloApellidos = ""
quitarComas = " ".join(nombres)
separados = ""

for i in range(len(quitarComas)):
    if quitarComas[i] != ",":
        separados += quitarComas[i]

juntar = separados.split(" ")

posicion = 0
for palabras in juntar:
    posicion += 1
    if posicion % 2 == 0:
        soloNombres += palabras + " "
    else:
        soloApellidos += palabras + " "

listaNombres = soloNombres.split(" ")
listaApellidos = soloApellidos.split(" ")


iniciales = ""

# Iniciales y Apellidos:

for i in range(len(soloNombres)):
    if 65 <= ord(soloNombres[i]) <= 90:
        iniciales += soloNombres[i] + "." + " "

listaIniciales = iniciales.split(" ")
nombreApellido = ""

for i in range(len(listaApellidos)-1):
    nombreApellido += listaIniciales[i] + " " + listaApellidos[i]
print(nombreApellido)






# Determinar el nombre mas largo

cantidadLetras= 0
nombreLargo = ""

for i in range(len(listaNombres)):
    if len(listaNombres[i]) > cantidadLetras:
        cantidadLetras = len(listaNombres[i])
        nombreLargo = listaNombres[i]
print(f"El nombre mas largo es: {nombreLargo}")

