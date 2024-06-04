letras = [letra for letra in 'aÑbóEc']
print(letras)

def contarVocalesDeLista(lista):
    contador = 0
    for caracter in lista:
        if caracter.upper() in 'AEIOUÁÉÍÓÚ':
            contador += 1
    return contador

print(contarVocalesDeLista(letras))