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

#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

print("Iniciales y Apellidos de las Personas")

for persona in nombres:
    apellido, nombre = persona.split(', ') #Divido la cadeba en otra lista y en la posicion 0 le asigno apellidos y en la pisicion 1 nombres
    inicial_nombre = nombre[0].upper() + '.' # busco la iniciar del nombre y la convierto en mayuscula y le agrego el punto 
    print(inicial_nombre, apellido)

print("\n")
#2) Decir cuál es el nombre de pila más largo?

nombres_pila = [nombre.split(', ')[1] for nombre in nombres] #divido la cadena en una lista y me posiciono en la pisicion 1 donde se encuentra el nombre
nombre_mas_largo = max(nombres_pila, key=len) #uso la funcion max para recorrer los nombres y que me devuelva el nombre mas largo

print(f"El nombre mas largo es: {nombre_mas_largo} \n")
    
#3) Mostrar el promedio de edad de las mujeres.

promedio_edades = [fecha.split('/')[2] for fecha in fechas] #obtengo solamente el año de nacimiento
años_enteros = [int(numero) for numero in promedio_edades] #Convierto a enteros los años pra poder hacer la suma

contador_edad = 0
cantidad_de_edades = 0

for i in range(len(años_enteros)): #calculo el promedio de edad recorriendo el arreglo
   edad = 2024 - años_enteros[i]
   cantidad_de_edades += 1
   contador_edad += edad
   promedio = contador_edad / cantidad_de_edades
   
print(f"Promedio de edad de las mujeres: {promedio} \n")

   