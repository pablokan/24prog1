nombres = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana", 
    "Santamaría, Carlos",
    "Skarsgard, Azul", 
    "Catalejos, Walter"
]

# Proceso 1
print("Iniciales y apellido de las personas:")
for nombre in nombres:
    partes_nombre = nombre.split(", ")
    apellido = partes_nombre[0]
    nombres_completos = partes_nombre[1].split()
    inicial = nombres_completos[0][0]
    print(f"{inicial}. {apellido}")

# Proceso 2
nombres_pila = [nombre.split(", ")[1].split()[0] for nombre in nombres]
nombre_mas_largo = max(nombres_pila, key=len)
print(f"El nombre más largo es: {nombre_mas_largo}")

# Proceso 3
fechas = [
    "02/05/1943",
    "07/04/1984",
    "10/02/1971",
    "21/12/1967",
    "30/01/1982",
    "30/08/1995",
    "18/07/1959"
]
sexos = ["f","f","m","f","m","f","m"]
suma_edades = 0
contador_mujeres = 0
for i in range(len(sexos)):
    if sexos[i] == "f":
        fecha_nacimiento = fechas[i].split("/")
        edad = 2024 - int(fecha_nacimiento[2])
        if int(fecha_nacimiento[1]) > 5 or (int(fecha_nacimiento[1]) == 5 and int(fecha_nacimiento[0]) > 2):
            edad -= 1
        suma_edades += edad
        contador_mujeres += 1

if contador_mujeres != 0:
    promedio_edad_mujeres = suma_edades / contador_mujeres
    print(f"El promedio de edad de las mujeres es: {promedio_edad_mujeres:.0f}")
else:
    print("No hay mujeres en la lista.")