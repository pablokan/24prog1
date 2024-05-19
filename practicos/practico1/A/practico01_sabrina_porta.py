#Practico numero 1
nombres = ["Torres, Ana", "Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"] 
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943","07/04/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]

#Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
for nombres, sexos in zip(nombres, sexos):
    apellidos, nombres = nombres.split(", ")
    inicial = nombres[0]
    print(f"{inicial}. {apellidos}")

#2) Decir cuál es el nombre de pila más largo.
nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"]
nombreMasLargo = ""
for nombre_apellido in nombres:
    nombre = nombre_apellido.split(", ")[1]
    if len(nombre) > len(nombreMasLargo):
        nombreMasLargo = nombre
print("El nombre de pila más largo es:", nombreMasLargo)

#3) Mostrar el promedio de edad de las mujeres. 

nombres = ["Torres, Ana", "Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"] 
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943","07/04/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]

#Profe sacar el promedio de la edad de mujeres no me salio, intente pero no sabia como llegar a eso, ya no me queda tiempo asique me rindo por hoy :)
