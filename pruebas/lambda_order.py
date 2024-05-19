lista = [[1, 2], [1, 3], [1, 1]]

def ordy(l):
    return l[1]

# Ordenar por el segundo elemento de cada sublista
#lista.sort(key=lambda x: x[1])
lista.sort(key=ordy)

print(lista)
# Salida: [[3, 1], [2, 2], [1, 3]]
