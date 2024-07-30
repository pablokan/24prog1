# Sara, Luis, Ana, Julián. 2 columnas. 10 caracteres de ancho por columna.
nombres = ['Sara', 'Luis', 'Ana', 'Julián', 'Pepe', 'Walter', 'Lara']
columnas = 1
ancho = 10

def modifAncho(s, a):
    return ' ' + s + (a - len(s)-1) * ' '

print()
for i in range(len(nombres)):
    s = f'| {modifAncho(nombres[i], 10)}'
    print(s, end='')
    if (i+1) % columnas == 0:
        print('|', end='')
        print()
    else:
        if i == len(nombres)-1:
            print('|', end='')
print()

