nombres_completos = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 

nombres = []

apellidos = []


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
# 1
# Mostrar titulo
print("1) Iniciales y apellidos de las personas:")

# Recorrer la lista de nombres
for i in range(len(nombres_completos)):
    n = nombres_completos[i]
    # Separar nombre y apellido
    nombre_completo = n.split(", ")
    # Agregar nombre y apellido a listas 
    nombre = nombre_completo[1]
    nombres.append(nombre)
    apellido = nombre_completo[0]
    apellidos.append(apellido)
    # Tomar la inicial de cada nombre
    inicial = nombre[0] 
    # Mostrar resultado
    print(inicial + ".", apellido)

#2
# Asignar como valor maximo el tamaño del primer nombre
tamaño_primer_nombre = len(nombres[0])
mayor_tamaño = tamaño_primer_nombre

# Recorrer la lista de nombres
for i in range(len(nombres)):
    # Variable con tamaño
    tamaño_nombre = len(nombres[i])
    # Verificar si el tamaño del nombre es mayor al valor maximo asignado
    if tamaño_nombre > mayor_tamaño:
        # Si lo es, asignar el nombre como nuevo valor maximo
        mayor_tamaño = tamaño_nombre
        # Guardar como nombre de mayor tamaño
        nombre_mayor_tamaño = nombres[i]

# Mostrar resultados
print("2) El nombre más largo es:", nombre_mayor_tamaño)
    

#3
# Cantidad total de mujeres
total = 0

# Suma total de las edades 
suma_edades = 0

# Recorrer la lista de nombres 
for i in range(len(nombres_completos)):
    # Verificar si es mujer
    if sexos[i] == "f":
        # Guardar fecha de nacimiento
        fec_nac_mujeres = (fechas[i])
        # Separar la fecha en dia,mes y año
        fechas_nac = fec_nac_mujeres.split("/")
        dia = int(fechas_nac[0])
        mes = int(fechas_nac[1])
        año = int(fechas_nac[2])
        # Asignar fecha actual
        dia_actual = 30
        mes_actual = 4
        año_actual = 2024
        # Conseguir edad
        edad = año_actual - año
        # Establecer edad real a la fecha actual
        if mes>mes_actual or (mes_actual>mes and dia>dia_actual):
            edad -= 1
        # Añadir el valor de la edad a la suma total de edades
        suma_edades += edad
        # Añadir 1 por cada mujer 
        total += 1

# Sacar el promedio de edad
promedio = int(suma_edades/total)
# Mostrar resultado
print("3) El promedio de edad es de", promedio)
