texto = "Riquelme toma mate"
c = 0
letraBuscada = 'e'

""" for letra in texto:
    if letra == letraBuscada:
        c += 1
"""

for i in range(len(texto)):
    if texto[i] == letraBuscada:
        c += 1


print(f'La letra "{letraBuscada}" aparece {c} veces en el texto "{texto}"')
