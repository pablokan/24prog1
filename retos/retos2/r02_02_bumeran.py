"""
Enunciado: Hacer un programa que cuente el número total de bumeranes de 
una lista de números enteros y muestre cada uno de ellos.
Un búmeran es una secuencia formada por 3 números seguidos, 
en la cual el primero y el último son iguales, y el segundo es diferente. 
Por ejemplo [2, 1, 2].
En la lista [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).
"""

lista = [7, 2, 1, 2, 3, 3, 3, 4, 2, 4, 1, 8]
print(lista)
c = 0
for i in range(len(lista)-2):
    bum = lista[i:i+3]
    if bum[0] == bum[2] and bum[0] != bum[1]:
        print(bum)
        c += 1
print(c)

