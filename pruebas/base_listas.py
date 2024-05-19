lista = [11, 'burro', 0.2]
print(lista[1])
lista.append('otro dato')
print(lista)
lista.insert(2, 'insertado')
print(lista)
lista[0] = 'pepe'
print(lista)
otraLista = []
# otraLista[0] = 'qq' # da error porque no existe esa posición

lista.pop()
print(lista)
dato = lista.pop(1)
print(lista)
print(dato)
lista.remove('pepe')
print(lista)

lista = [11, 'burro', 0.2]
# recorrido por indice (posiciones)
for i in range(len(lista)):
    print(lista[i], end='---')
print()
# recorrido por elemento (valores)
for elemento in lista:
    print(elemento, end ='***')

# listas paralelas
nombres = ['John', 'Alice', 'Jack']
edades = [11, 22, 33]
