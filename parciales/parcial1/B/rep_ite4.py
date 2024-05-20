nombres = []
respuesta = 'si'
print('Carga de datos')
if respuesta == 'si':
    nombre = input('Nombre: ')
    nombres.append(nombre)
respuesta = input('Quiere cargar más datos (si/no): ')
if respuesta == 'si':
    nombre = input('Nombre: ')
    nombres.append(nombre)
respuesta = input('Quiere cargar más datos (si/no): ')
if respuesta == 'si':
    nombre = input('Nombre: ')
    nombres.append(nombre)

print('Los nombres cargados son:')
for nombre in nombres:
    print(nombre)

