hayMas = 's'
nombres = []
sexos = []
while hayMas == 's':
    nombre = input('Ingrese un nombre: ')
    nombres.append(nombre)
    sexo = input('Ingrese el sexo: ')
    sexos.append(sexo)
    hayMas = input('Hay más? (s/n): ')

c = 0
for i in range(len(sexos)):
    if sexos[i] == 'f':
        c += 1
        print(nombres[i])
print('La cantidad total de mujeres es', c)

