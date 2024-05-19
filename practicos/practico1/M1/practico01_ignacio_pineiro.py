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

apellidos = []
iniciales = []
nombreDePila = []

for i in range(len(nombres)):
    posicionComa = nombres[i].find(", ")
    apellidos.append(nombres[i][:posicionComa])
    iniciales.append(nombres[i][posicionComa+2:posicionComa+3])
    nombreDePila.append(nombres[i][posicionComa+2:])
    inicialesYapellidos = iniciales[i] + ". " + apellidos[i]
    print(inicialesYapellidos)
    len(nombres[i][posicionComa+2:])

nombreLargo = ''

for x in range(len(nombreDePila)):               #En este tarde porque llamaba a la variable del bucle de arriba, en vez de iterar sobre "x"
    if len(nombreDePila[x]) > len(nombreLargo):
        nombreLargo = nombreDePila[x]
print("El nombre más largo es:", nombreLargo)

diaHoy = 30
mesHoy = 4
anoHoy = 2024
totalEdades = 0
promedioEdad = 0
for y in range(len(fechas)):
    if sexos[y] == "f":
        fNac = fechas[y]
        diaNac = int(fNac[:2])
        mesNac = int(fNac[3:5])
        anoNac = int(fNac[6:])
        edad = anoHoy - anoNac
    
        if (mesNac > mesHoy) or (mesNac == mesHoy & diaNac > diaHoy):
            edad = edad - 1
            totalEdades += edad
            promedioEdad = totalEdades / 4
    print(sexos[y]== "f")                     #la lista de sexos me da valores True o False (????? POR QUE?????
print("el promedio de edad de", promedioEdad)
