hayMas = 's'
nombres = []
while hayMas == 's':
    nombre = input('Ingrese un nombre: ')
    nombres.append(nombre)
    hayMas = input('Hay más? (s/n): ')

nombreBuscado = input('Ingrese un nombre a buscar: ')

if nombreBuscado in nombres:
    i = 0
    while nombreBuscado != nombres[i]:
        i += 1
    print(nombreBuscado, 'está en la posición', i)
else:     
    print(nombreBuscado, 'no está')


