frase = 'Quiero comer manzanas, solamente manzanas.'

def totalLetras(cadena):
    contador = 0
    letras = ''.join([chr(x) for x in range(97, 123)]) + 'áéíóúñ'
    for caracter in cadena.lower():
        if caracter in letras:
            contador += 1
    return contador

print(totalLetras(frase))
print(totalLetras('A12Ú3é456Ñi'))
