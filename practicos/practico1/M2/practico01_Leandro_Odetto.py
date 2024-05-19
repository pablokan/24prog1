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

#1
iniciales = []

for x in range(len(nombres)):
    nombre = nombres[x]
    str(nombre)
    for i in range (len(nombre)):
        letra = nombre[i]
        if  letra == ","  : 
            apellido = nombre[:i]
            inicialEspacio = nombre[i+2] + ". "
            inicialEspacioApellido = inicialEspacio + apellido
            iniciales.append(inicialEspacioApellido)

for partes in iniciales:
    print(partes)

print("-------")
#2
listaNomPila = []
max = " " 
suma = 0

for elementos in nombres:
    str(elementos)
    for r in range(len(elementos)):
        letra2 = elementos[r]
        if letra2 == ",":
            nombrePila = elementos[r+2:]
            listaNomPila.append(nombrePila)

for gacho in listaNomPila:
    if (len(gacho)>len(max)):
        max = gacho
print("El nombre de pila mas largo es el de ", max)

print("-------")
#3
fechaMujeres = []
hoy = "02/05/2024"
anoHoy = int(hoy[6:])

for sexo in range(len(sexos)):
    if sexos[sexo] == "f":
        fecha = fechas[sexo]
        fechaMujeres.append(fecha)

for f in fechaMujeres:
    str(f)
    anoMujer = int(f[6:])
    resta = anoHoy - anoMujer
    suma = suma + resta

promedio = suma // len(fechaMujeres)

print("El promedio de edad es de ",promedio)

#sé que me falta calcular el tema del mes y el dia pero el resultado ya da 51 y no llegaria con el tiempo, saludos profe!