# Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas
datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]
# estoy un poco atrasado por que no pude cursar por dos semanas mes estoy poniendo al dia!

 
for dato in datos:# en este me ayudaron mis compañeros
    nombre, apellido, *_ = dato.split(", ")
    print(f"{apellido.split()[0][0]}. {nombre}")
    
    
# Decir cuál es el nombre de pila más largo    

nombre_mas_largo = ""


for dato in datos:
    
    if dato > nombre_mas_largo:
       
        nombre_mas_largo = dato


print("El nombre más largo es:", nombre_mas_largo) # no supe como hacer para q tome el nombre solo



suma_edades = 0
contador_mujeres = 0

for dato in datos:
    
    if dato[1] == "f":
        anio_actual = 2024
        anio_nacimiento = int(dato[2][-4:])
        edad = anio_actual - anio_nacimiento
        suma_edades += edad
        contador_mujeres += 1

# no llegue con el tiempo !!



    


