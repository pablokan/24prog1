"""1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
2) Decir cuál es el nombre de pila más largo.
3) Mostrar el promedio de edad de las mujeres.
"""
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



#mostrar inicial
for i in range(len(nombres)):
    nombre=nombres[i]   #variable para buscar subcadena
    separador=nombre.find(", ")   #buscar el separador de apellido y nombre
    apellido=nombre[:separador]   #separar apellido de nombre
    name=nombre[separador+2:]
    inicial=name[0:1]
    print (inicial, ". ", apellido)

#mostrar el nombre mas largo (no llegué a intentar)
#promedio de edad de mujeres (no me salió)
edadTodos=[]
edadMuj=[]
total=0
for i in range(len(sexos)):
    edadTodos.append(fechas[i])
    edades=fechas[i]
    edades.split("/")
    dia=edades[0]
    mes=edades[1]
    ano=edades[2]
    diaActual=30
    mesActual=4
    anoActual=2024
    edad=anoActual - ano
    if mes>mesActual or (mesActual>mes and dia>diaActual):
        edad -= 1
    if sexos[i]=="f":
        edadMuj.append(edad)
        total+=1
    for elemento in range(len(edadMuj[elemento])):
        edadTotal= elemento+elemento
    promedio=edadTotal/total
    print(promedio)