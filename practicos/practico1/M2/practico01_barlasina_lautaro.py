# Listas de datos
nombres = [
    "Torres, Ana",
    "Hudson, Kate",
    "Quesada, Benicio",
    "Campoamores, Susana",
    "Santamaría, Carlos",
    "Skarsgard, Azul",
    "Catalejos, Walter"
]
sexos = ["f", "f", "m", "f", "m", "f", "m"]
fechas = [
    "02/05/1943",
    "07/04/1984",
    "10/02/1971",
    "21/12/1967",
    "30/01/1982",
    "30/08/1995",
    "18/07/1959"
]

# Proceso 1: Mostrar las iniciales de los nombres con un punto y luego el apellido completo de todas las personas.
def mostrar_iniciales_apellidos(nombres):
    for nombre in nombres:
        apellido, nombre_pila = nombre.split(", ")
        inicial_nombre = nombre_pila[0]
        print(f"{inicial_nombre}. {apellido}")

# Proceso 2: Decir cuál es el nombre de pila más largo.
def nombre_pila_mas_largo(nombres):
    nombres_pilas = [nombre.split(", ")[1] for nombre in nombres]
    nombre_mas_largo = max(nombres_pilas, key=len)
    print(f"El nombre de pila más largo es: {nombre_mas_largo}")

# Proceso 3: Mostrar el promedio de edad de las mujeres.
def promedio_edad_mujeres(sexos, fechas):
    edades_mujeres = []
    for sexo, fecha in zip(sexos, fechas):
        if sexo == "f":
            _, _, año = fecha.split("/")
            edad = 2024 - int(año)  # Suponiendo el año actual como 2024
            edades_mujeres.append(edad)
    if edades_mujeres:
        promedio = sum(edades_mujeres) / len(edades_mujeres)
        print(f"El promedio de edad de las mujeres es: {promedio:.2f}")
    else:
        print("No hay mujeres en la lista.")
        
# Ejecutar los procesos
print("Proceso 1:")
mostrar_iniciales_apellidos(nombres)
print("\nProceso 2:")
nombre_pila_mas_largo(nombres)
print("\nProceso 3:")
promedio_edad_mujeres(sexos, fechas)