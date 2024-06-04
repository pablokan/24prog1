frase = 'Quiero comer manzanas, solamente manzanas.'

def contarLetra(letra, cadena):
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

l = 'a'
cantidad = contarLetra(l, frase)
print(f'La cantidad de veces que aparece la letra "{l}" en la cadena "{frase}" es {cantidad}')

# Otro uso con literales
print(contarLetra('e', 'La especie humana'))
