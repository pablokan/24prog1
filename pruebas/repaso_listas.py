lista = [213, "mesa", 0.74]
# lista[3] = 'algo' fuera de rango
lista[2] = 0.33 # esto funciona porque la posición 2 ya existe

print(lista)
print(lista[1])

# agregar elementos
lista.append("Lisa") # agrega al final de la lista
print(lista)
lista.insert(2, 222222) # inserta en la tercera (2) posición
print(lista)

# quitar elementos
lista.pop() # sin argumentos quita el último
print(lista)
valorSacado = lista.pop(1) # si el argumento es un entero, elimina el elemento de dicha posición
# y si además lo asigno a una variable, el elemento quitado va a almacenarse allí
print(lista, valorSacado)
saleAlgo = lista.remove(213)
print(lista, saleAlgo) # devuelve None (ninguno, valor nulo) porque el remove a diferencia del pop solo quita

otraLista = [111, 'pepe']
otraLista.remove('pepe')
print(otraLista)
