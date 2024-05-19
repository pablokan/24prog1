numerosMayoresDe23 = []
cantidadMayoresDe23 = 0
for i in range(10):
    mensaje = 'Ingrese el número ' + str(i+1) + ': '
    n = int(input(mensaje))
    if n > 23:
        cantidadMayoresDe23 += 1
        numerosMayoresDe23.append(n)
print('Los números mayores a 23 son:', numerosMayoresDe23)
print('Y su cantidad es:', cantidadMayoresDe23)
# También se podía obtener la cantidad sin contar usando len

