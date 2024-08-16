"""
Enunciado: Dada una lista de enteros ordenada ascendente y sin repetidos, 
hacer un programa que genere una nueva lista con todos los que faltan entre
el menor y el mayor.
Mostrar ambas listas.
Comprobar primero que la lista cumpla con la condición inicial.
"""

correcta = True
lista = [0, 2, 5, 6, 7, 10, 11, 12, 14, 15]
faltantes = []
cantidad = len(lista)
i = -1
while correcta and i < cantidad-2:
    i += 1
    if lista[i] >= lista[i+1]:
        correcta = False
print(correcta)

for i in range(lista[-1]-1):
    if i not in lista:
        faltantes.append(i)

print(lista)
print(faltantes)
