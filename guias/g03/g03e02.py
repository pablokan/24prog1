letra = ''
cantidadVocales = 0
letras = []
while letra != '*':
    letra = input('Ingrese una letra (* para terminar la carga): ')
    letras.append(letra)

for letra in letras:
    if letra in 'aeiou':
        cantidadVocales += 1

print('La cantidad de vocales es', cantidadVocales)
