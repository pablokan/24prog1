datos = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/04/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],
]
#Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
for i in range (len(datos)):
    dato = datos[i]
    nombreComp = dato [0]
    nombreSp = nombreComp.split (", ")
    nombre = nombreSp [1]
    letranom = nombre [0]
    print(f"{letranom}. {nombreSp [0]}")
#Decir cuál es el nombre de pila más largo
numeroLetras = 0
nombreMasLargo= ""
for i in range (len(datos)):
    dato = datos[i]
    nombreComp = dato [0]
    nombreSp = nombreComp.split (", ")
    nombre = nombreSp [1]
    largo = len(nombre)
    if largo > numeroLetras:
        nombreMasLargo = nombre
        numeroLetras = largo
print(f"El nombre más largo es : {nombreMasLargo}")
#Mostrar el promedio de edad de las mujeres.
anoActual = 2024
totAnos = 0
for i in range (len(datos)):
    dato = datos[i]
    fecha = dato [2]
    fechaSp = fecha.split ("/")
    ano = int(fechaSp[2])
    anos = anoActual - ano
    if dato[1] == "f":
        totAnos += anos
print(f"El promedio de edad de las muejres es: {totAnos/4}")
    
    

