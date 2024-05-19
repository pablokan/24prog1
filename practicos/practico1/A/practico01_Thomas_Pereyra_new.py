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

datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]

cadena = (','.join(nombres))
listaCompleta = cadena.split(',')
#separando los apellidos de los nombres
apellidos = []
apellidoSolos = []
nombreSolos = []
for i in range(len(nombres)):
    apellidos.append('a')
    apellidos.append('n')
print(apellidos)
for i in range(len(listaCompleta)):
    if apellidos[i] == 'a':
        apellidoSolos.append(listaCompleta[i])
    elif apellidos[i] == 'n':
        nombreSolos.append(listaCompleta[i])    

#Imprimiendo Inicial con apellido
for i in range(len(nombreSolos)):
    inicial = nombreSolos[i][:2] + '.' +' '+ apellidoSolos[i]
    print(inicial)


#buscando el nombre mas largo e imprimirlo
pila = 0
for i in range(len(nombreSolos)):
    nombre = nombreSolos[i]
    longitud = len(nombreSolos[i])
    if longitud > pila:
        nombreMayor = nombre
        pila = longitud

#nombre de pila mas largo
print('nombre mas largo:',nombreMayor)   

#Mostrar el promedio de edad de mujeres

mujers = []
edadMujer = []

for i in range(len(nombres)):
    if sexos[i] == 'f':
        mujers.append(nombres[i])
        edadMujer.append(fechas[i])
edadTotal = 0
for i in range(len(edadMujer)):
    anoSolo = edadMujer[i][6:]
    anoSolo = int(anoSolo)
    edadM = (2024 - anoSolo)
    edadTotal = (edadTotal + edadM)
    promedio = edadTotal//4

print('edad promedio de mujeres:',promedio,'años')




    
           

