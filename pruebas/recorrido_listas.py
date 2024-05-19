lista = [213, "mesa", 0.74]
longitudLista = len(lista) # len obtiene la cantidad de elementos

# recorrido por indice (posiciones)
for i in range(longitudLista):
    print(lista[i])

# recorrido por elemento (valores)
for elemento in lista:
    print(elemento)

# listas paralelas: cuando a misma posición refieren al mismo objeto
nombres = ['John', 'Alice', 'Jack']
edades = [11, 22, 33]

for i in range(len(nombres)):
    print(nombres[i], 'tiene', edades[i], 'años')



