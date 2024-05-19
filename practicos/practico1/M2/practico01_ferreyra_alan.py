datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]

# Procesos para las salidas:

# 1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.


for dato in datos:
     apellido, nombre, _, _ = dato.split(", ")
   


# Mostrar la inicial del nombre y agregar un punto

inicialNombre = nombre[0] + "."

print (inicialNombre,apellido)




# 2 Decir cuál es el nombre de pila más largo.

nombreMasLargo = ""
maximaLongitud = 0

for dato in datos:
  apellido, nombre, _, _ = dato.split(", ")
    

# Longitud del nombre
longitudNombre = len(nombre)


if longitudNombre > maximaLongitud:
    nombreMasLargo = nombre
    maximaLongitud = longitudNombre

# Nombre de pila más largo
print("El nombre de pila mas largo es: ",nombreMasLargo)    




# 3 Mostrar el promedio de edad de las mujeres. 

sumaDeEdades = 0
contarMujeres = 0

for dato in datos:
    sexo, fechaDeNacimiento, _, _ = dato.split(",")


if sexo == "f":
    añoDeNacimiento = fechaDeNacimiento.split("/")
    edad = 2024 - int(añoDeNacimiento)
    sumaDeEdades +=edad
    contarMujeres +=1


# Saco promedio

if contarMujeres > 0:
    promedioEdad = sumaDeEdades / contarMujeres

print("El promedio de edad de las mujeres es: ", promedioEdad)









