datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]

# Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas

rangoDatos = len(datos)
iniciales = []
apellidos = []

print("1) Iniciales y apellido de las personas:")
for x in range(rangoDatos):
    inicio = datos[x].find(",")
    soloNombre = datos[x][inicio+2:]
    iniciales.append(soloNombre[:1])
    soloApellido = datos[x][:inicio]
    apellidos.append(soloApellido)
    print(iniciales[x]+".",apellidos[x])

# Decir cuál es el nombre de pila más largo.

nombre = []
largura = []
largura1 = [0]

print ("El nombre más largo es:")
for x in range(rangoDatos):
    inicio = datos[x].find(",")
    soloNombre = datos[x][inicio+2:]
    finalNombre = soloNombre.find(",")
    nombre.append(soloNombre[:finalNombre+1])
    largo = str(nombre[x]).find(",")
    largura.append(largo)

for x in range(rangoDatos):
    print(largura[x],largura1) 
    if largura[x] > int(largura1[x]):
        largura1.insert(0, largura[x])

# No llegue a terminar/encontrar la logica
        
    

    

# Mostrar el promedio de edad de las mujeres.

# No se llego.