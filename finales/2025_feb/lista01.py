# lista de nombres
nombres = ['Juan', 'Ana', 'Luis', 'Pedro', 'Maria']

# mostrar los nombres hasta que se encuentre uno que empiece con 'P'
i = 0
while nombres[i][0] != 'P':
    print(nombres[i])
    i += 1

# salida:
# Juan
# Ana
# Luis

# mostrar la suma de la cantidad de letras de todos los nombres
suma = 0
for n in nombres:
    suma += len(n)
print(suma)

apellidos = ['Perez', 'Gomez', 'Lopez', 'Torres', 'Garcia']

# crear una nueva lista llamada nombres_completos que contenga los nombres y apellidos
nombres_completos = []
for i in range(len(nombres)):
    nombres_completos.append(nombres[i] + ' ' + apellidos[i])
print(nombres_completos)

# usando la lista nombres_completos, mostrar los nombres completos que tengan una cantidad de letras mayor a 10
for n in nombres_completos:
    if len(n) > 10:
        print(n)    