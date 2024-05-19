datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]

nombres = []
apellidos = []
sexos = []
fechas = []
datos2 = []
for dato in datos:
    datos2.append(dato.split(","))

for dat in datos2:
    apellidos.append(dat[0])
    nombres.append(dat[1])
    sexos.append(dat[2])
    fechas.append(dat[3])


#Salida esperada N°1, Iniciales y Apellidos de las personas:
letra = []
salida = []
#voy a recorrer dos listas distintas, por eso utilizo el zip, para decirle que son listas paralelas
for let,ape in zip(nombres,apellidos):
    print(let[1]+".", ape)
#al haber un espacio despues de la , en el array con los nombres, me devuelve los nombres con un espacio, por eso le pido el indice 1

#Salida esperada N°2, Nombre más largo:
mayor = ''
for nombre in nombres:
    if len(nombre) > len(mayor):
        mayor = nombre
print("El nombre más largo es:",mayor)

#Salida esperada N°3, Promedio de edad en Mujeres:
mujeres = []
diaActual = 2
mesActual = 5
añoActual = 2024
fechas_formateadas = []

for sex, fecha in zip(sexos,fechas):
    #De nuevo lo mismo que antes, al haber un espacio luego de la coma, la variable se guardo con un espacio, por eso mismo le pido que me traiga el valor en la posicion 1
    if sex[1] == 'f':
        mujeres.append(sex)
        fechas_formateadas.append(fecha.split("/"))

diferencia_año = []
diferencia_meses = bool
for fecha in fechas_formateadas:
    diferencia_meses = (mesActual, diaActual) < (int(fecha[1]), int(fecha[0]))
    if diferencia_meses == False:
        diferencia_año.append((añoActual - 1) - int(fecha[2]))
    else:
        diferencia_año.append(añoActual - int(fecha[2]))
        

promedio = 0
totalEdades = 0
for dif in diferencia_año:
    totalEdades += dif 
    promedio = totalEdades / len(diferencia_año)
print("El promedio de edad de las mujeres es de",int(promedio))
