frase = 'Real Madrid gana las copas.'
nuevaFrase = ''

""" for letra in frase:
    if letra != 's':
        nuevaFrase += letra
print(nuevaFrase)
"""

lista = frase.split('s')
print(lista)
for subcadena in lista:
    nuevaFrase += subcadena 
print(nuevaFrase)

