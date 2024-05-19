nombres = []
sexos = []
hayMas = 's'
while hayMas == 's':
    nombre = input('Nombre: ')
    sexo = input('Sexo (m/f): ')
    nombres.append(nombre)
    sexos.append(sexo)
    hayMas = input('Más datos? (s/n): ')

mujeres = []
for x in range(len(nombres)):
    if sexos[x] == 'f':
        mujeres.append(nombres[x])

print('Lista de mujeres:')
for mujer in mujeres:
    print(mujer)
