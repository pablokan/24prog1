#
# Date: 02/05/2024
# Name: MUCHUT Ulises Samuel

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

#Consigna 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

for i in range(len(nombres)):
     separacion = nombres[i].find(",")
     inicial = nombres[i][separacion+2]
     apellido = nombres[i][+1 :separacion]
     print(inicial+"."+" "+apellido)
     
# Consigna 2) Decir cuál es el nombre de pila más largo.

for i in range(len(nombres)):
    separacion = nombres[i].find(",")
    
   
# No se como seguir me trabe   




# Consigna 3) Mostrar el promedio de edad de las mujeres. 
cantidadMujeres = 0
for i in sexos:
    if i == "f":
         cantidadMujeres += 1
print(cantidadMujeres)


for i in range(len(fechas)):
    dia = fechas[i].split("/")
    mes = fechas[i].split("/")
    año = fechas[i].split("/")

# No pude resolverlo
   