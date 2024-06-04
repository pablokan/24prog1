frase = 'Quiero comer manzanas, solamente manzanas.'

def reemplazarPalabra(cadena, palabraVieja, palabraNueva):
    while palabraVieja in cadena:
        posiPalVie = cadena.find(palabraVieja)
        inicio = cadena[:posiPalVie]
        final = cadena[posiPalVie+len(palabraVieja):]
        cadena = inicio + palabraNueva + final
    return cadena

print(reemplazarPalabra(frase, "manzanas", "peras"))
print(reemplazarPalabra('torre-mesa-torre-silla', "torre", "base"))


