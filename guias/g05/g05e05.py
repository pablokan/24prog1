frase = 'Quiero comer manzanas, solamente manzanas.'

def armarListaPalabras(cadena):
    letrasMasEspacio = ''.join([chr(x) for x in range(97, 123)]) + 'áéíóúñ'+ ' '
    cadenaLimpia = ''
    for caracter in cadena.lower():
        if caracter in letrasMasEspacio:
            cadenaLimpia += caracter
    return cadenaLimpia.split()

def palabraMasLarga(lista):
    masLarga = ''
    for palabra in lista:
        if len(palabra) > len(masLarga):
            masLarga = palabra
    return masLarga

print(frase)
print(armarListaPalabras(frase))
print('Cantidad de letras de la palabra más larga:')
print(len(palabraMasLarga(armarListaPalabras(frase))))
print()
print('Las maravillas de la noche')
listaDePalabras = armarListaPalabras('Las maravillas de la noche')
print(palabraMasLarga(listaDePalabras))
longitudPalabraMasLarga = len(palabraMasLarga(listaDePalabras))
print(longitudPalabraMasLarga)
