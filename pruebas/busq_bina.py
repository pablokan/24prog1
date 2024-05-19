# Búsqueda binaria

estado = None
tiro = 500
mini = 1
maxi = 1000

print('Piense un número entero entre 1 y 1000, la computadora intentará adivinarlo. Si lo que tira es mayor, usted ingresa el signo >, si es menor, ingrese el signo <, si la PC acierta, ingrese =. Cuando esté listo, presione enter:')
input()
intentos = 0
while estado != '=':
    intentos += 1
    print(f"Pensaste en un número mayor, menor o igual que {tiro}?")
    estado = input('Estado: ')
    if estado == '=':
        print('Acerté!!!!!!')
        break
    else:
        if estado == ">":
            mini = tiro
            tiro = (tiro + maxi) / 2
            tiro = round(tiro, 0)
            tiro = int(tiro)
        else:
            maxi = tiro
            tiro = (tiro + mini) // 2

    print(f'{mini=} --- {maxi=}')

print(f"Acerté en {intentos} intentos")

