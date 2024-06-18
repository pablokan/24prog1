cXc = {x for x in range(4)}
print(cXc)

conjuntoLetrasComunes = {chr(x) for x in range(97, 123)}
letras = conjuntoLetrasComunes.union(set('áéíóúñ'))
print(letras)
