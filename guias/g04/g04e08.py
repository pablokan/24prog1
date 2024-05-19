frase = "Quiero comer manzanas, solamente manzanas."

cuentoLetras = 0
for caracter in frase:
    if caracter not in ' ,.':
        cuentoLetras += 1
print('La cantidad de letras es', cuentoLetras)
