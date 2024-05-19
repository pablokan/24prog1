#Procesos para las salidas:
#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
#2) Decir cuál es el nombre de pila más largo.
#3) Mostrar el promedio de edad de las mujeres. 


nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"] 
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943", "07/04/1984", "10/02/1971", "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]

#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas. 
for nombre in nombres:
    apellido =""
    nombre_completo =""
    for letra in nombre:
        if letra == ",":
            apellido = nombre_completo 
            nombre_completo =" "
        else:
            nombre_completo += letra
    incial_nombre = nombre_completo[2]+"."
    print(incial_nombre, apellido)
    
print()
print()
print()
#2) Decir cuál es el nombre de pila más largo. 
nombre_largo = " "  
longitud_mas_larga = 0

for nombre in nombres:
    longitud_nombre = 0  
    nombre_de_pila = " "    
    for caracter in nombre:
        if caracter != "," and caracter != "": 
            nombre_de_pila += caracter 
            longitud_nombre += 1 
            
    if longitud_nombre > longitud_mas_larga:
        nombre_largo = nombre_de_pila 
        longitud_mas_larga = longitud_nombre 

print("El nombre de pila más largo es:", nombre_largo)

print()
print()
print()

#3) Mostrar el promedio de edad de las mujeres. 

año_actual = 2024
suma_edades = 0
cantidad_mujeres = 0
for fecha in fechas:
    año_nacimiento = int(fecha[-4:])
    edad = año_actual - año_nacimiento
    suma_edades += edad
    cantidad_mujeres += 1

promedio_edad_mujeres = suma_edades / cantidad_mujeres

print("El promedio de edad de las mujeres es:", promedio_edad_mujeres)

