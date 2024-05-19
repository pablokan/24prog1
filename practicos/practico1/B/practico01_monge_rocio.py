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
maximo_nombre= ""


for i in range (len(nombres)):
    print (nombres [i])
    nombre_completo = nombres [i]
    nombre_y_apellido= nombre_completo.split (", ")
    nombre_solo= nombre_y_apellido [1]
    letra= nombre_solo [0]
    print (letra, ". ", (nombre_y_apellido [0]))    

for i in range (len(nombres)):
    nombre_completo = nombres [i]
    nombre_y_apellido= nombre_completo.split (", ")
    nombre_solo= nombre_y_apellido [1]
    letra= nombre_solo [0]  
    largo_nombre= len(nombre_solo)
    largo_maximo= len (maximo_nombre)
    if largo_nombre > largo_maximo :
        maximo_nombre = nombre_solo
"""
for i in range (len(sexos)) :
    sexo_valor= sexos [i]
    if sexo_valor == ("f"):
        fecha_valor = fechas[i]

 #profe, no me dio el tiempo para calcular la edad.
 
"""


print ("El que tiene mas letras es: ", maximo_nombre )
