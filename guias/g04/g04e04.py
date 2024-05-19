palabra = 'hola'
palabraEnMayuscula = ''
for letra in palabra:
    numeroASCII = ord(letra)
    numeroASCIImayuscula = numeroASCII - 32
    letraMayuscula = chr(numeroASCIImayuscula)
    palabraEnMayuscula += letraMayuscula
print(palabraEnMayuscula)

