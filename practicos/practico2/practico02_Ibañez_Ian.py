personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]

# 1) Los apellidos de las personas nacidas antes de un año solicitado al usuario.

anioI = int(input("Ingrese año: "))
print("Los apellidos de las personas nacidas antes del año", anioI, "son:")

for x in range (len(personas)):
    anio = personas[x][-4:]
    inicioApellido = personas[x].find(" ")
    finalApellido = personas[x].find(",")
    apellido = personas[x][inicioApellido+1:finalApellido]
    if int(anio) < anioI:
        print(apellido)

print()
# 2) La cantidad de personas nacidas en un país ingresado por el usuario.

paisI = input("Ingrese país: ")
c = 0

for x in range (len(personas)):
    inicioNacio = personas[x].find(",")
    finalNacio = personas[x].find("(")
    pais = personas[x][inicioNacio+1:finalNacio]
    if pais == paisI:
        c += 1

print("La cantidad de personas de",paisI, "es", c)

print()
# 3) El nombre de pila de la persona más joven de Europe.

europeos = []

for x in range(len(personas)):
    inicioC = personas[x].find("(")
    finalC = personas[x].find(")")
    continente = personas[x][inicioC+1:finalC]
    if continente == "Europe":
        europeos.append(personas[x])

anios = []

for x in range(len(europeos)):
    inicioFecha = str(europeos[x]).find("-")
    anios.append(europeos[x][-4:])

mayor = anios[0]
nombreMayor = ""

for x in range(len(anios)):
    if anios[x] > mayor:
        mayor = anios[x]
        nombreMayor = europeos[x][:str(europeos[x]).find(" ")]


print("La persona más joven de Europe es " + nombreMayor + ".")