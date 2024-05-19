texto = "Quiero comer manzanas, solamente manzanas."
palabra = "manzanas"
contador = 0

# cambiando la posición de búsqueda
""" posicion = texto.find(palabra)
while posicion != -1:
    contador = contador + 1
    posicion = texto.find(palabra, posicion + 1)
print(palabra , "se repite" , contador , "veces")
"""

#cortando la cadena
""" posicion = 0
c = 0
while posicion != -1:
    posicion = texto.find(palabra)
    if posicion != -1:
        c += 1
        texto = texto[posicion+1:]
print(c)
"""

frase = "Quiero comer manzanas, solamente manzanas."
contador = 0
frase = frase.split()
buscar_palabra = input("ingrese la palabra que quiere buscar: ")
for x in range(len(frase)):
    if buscar_palabra in frase[x]:
        contador = contador + 1
print(contador)


