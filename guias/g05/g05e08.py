nombres = ['Ana', 'Juan', 'Luis', 'Vilma']

def posiNombre(lista, nombre):
    encontrado = False
    p = 0
    while not encontrado and p < len(lista):
        if nombre == lista[p]:
            encontrado = True
        p += 1
    if not encontrado:
        return nombre + ' no encontrado'
    else:
        return p
    
print(posiNombre(nombres, 'Juana'))
