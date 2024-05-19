# Datos de 2008 en formato string
nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

# Procesamiento de los datos de 2008
data_2008 = nacidos2008.split(",")
nombres_2008 = [(data_2008[i], int(data_2008[i+1]), data_2008[i+2]) for i in range(0, len(data_2008), 3)]

# Datos de 2018 estructurados
nombres_2018 = [
    ('Liam', 19837, 'm'),
    ('Noah', 18267, 'm'),
    ('Michael', 14516, 'm'),
    ('James', 13525, 'm'),
    ('Oliver', 13389, 'm'),
    ('Emma', 18688, 'f'),
    ('Olivia', 17921, 'f'),
    ('Ava', 14924, 'f'),
    ('Isabella', 14464, 'f'),
    ('Sophia', 13928, 'f')
]

# Función para calcular diferencias
def calcular_diferencias(pos, sexo):
    nombre_2018 = nombres_2018[5 * (sexo == 'f') + pos - 1]
    nombre_2008 = nombres_2008[5 * (sexo == 'f') + pos - 1]
    diferencia = nombre_2018[1] - nombre_2008[1]
    print(f"Diferencia en posición {pos} y sexo {sexo}: {diferencia}")

# Función para nombres que comienzan con una letra dada
def nombres_con_letra(letra):
    print("Nombres que comienzan con", letra, ":")
    for nombre in nombres_2008 + nombres_2018:
        if nombre[0].startswith(letra):
            print(nombre[0])

# Función para encontrar nombres repetidos
def nombres_repetidos():
    nombres_08 = set([nombre[0] for nombre in nombres_2008])
    nombres_18 = set([nombre[0] for nombre in nombres_2018])
    repetidos = nombres_08.intersection(nombres_18)
    print("Nombres repetidos en ambos años:", repetidos)

# Ejemplo de uso
calcular_diferencias(2, 'f')  # Ejemplo: Posición 1 y sexo masculino
nombres_con_letra('J')        # Ejemplo: Nombres que comienzan con 'E'
nombres_repetidos()           # Nombres repetidos en 2008 y 2018
