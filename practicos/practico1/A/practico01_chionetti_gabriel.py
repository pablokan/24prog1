'''
Procesos para las salidas:
1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
2) Decir cuál es el nombre de pila más largo.
3) Mostrar el promedio de edad de las mujeres. 
'''

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

# Proceso 1
print("1) Iniciales y apellido de las personas:")
for i in range(len(nombres)):
    posi = nombres[i].find(",")
    inicial = nombres[i][posi+2:posi+3]
    nombre = nombres[i][posi+2:]
    apellido = nombres[i][:posi]
    inicialPunto = inicial + "."
    print(inicialPunto + " " + apellido)



# Proceso 2
largo = 0
for i in range(len(nombres)):
    posi = nombres[i].find(",")
    nombre = nombres[i][posi+2:]
    if len(nombre) > largo:
        largo = len(nombre)
        nombreLargo = nombre

print("\n""2) El nombre más largo es:", nombreLargo, "\n")

# Proceso 3
cantidad = 0
suma = 0
for i in range(len(sexos)):
    if sexos[i] == "f":
        cantidad = cantidad + 1
        fechasDividias = fechas[i].split('/')
        anio = int(fechasDividias[2])
        suma = suma + (2024 - anio)
        if fechasDividias[1] >= "05":
            if fechasDividias[0] >= "02":
                suma = suma - 1
        
promedio = int(suma/cantidad)
print("3) El promedio de edad de las mujeres es:",promedio)

