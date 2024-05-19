frase = "Quiero comer manzanas, solamente manzanas."
fraseLimpia = ''
# limpio de NO letras, dejo espacios
for caracter in frase:
    if caracter not in ',.':
        fraseLimpia += caracter
palabras = fraseLimpia.split()

masLarga = ''
for palabra in palabras:
    if len(palabra) > len(masLarga):
        masLarga = palabra
print(f'la palabra más larga es "{masLarga}" y su longitud es {len(masLarga)}')
