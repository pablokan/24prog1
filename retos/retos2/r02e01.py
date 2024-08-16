ordenadaAscendenteSinRepetidos = [2, 4, 5, 9]

# Comprobar que es ordenada ascendente sin repetidos
noCumple = False
for i in range(len(ordenadaAscendenteSinRepetidos)-1):
    if ordenadaAscendenteSinRepetidos[i] >= ordenadaAscendenteSinRepetidos[i+1]:
        noCumple = True

if noCumple:
    print('La lista original no cumple con las condiciones')
else:
    listaCompleta = []
    losQueNoEstan = []
    for i in range(ordenadaAscendenteSinRepetidos[0], ordenadaAscendenteSinRepetidos[-1]+1):
        listaCompleta.append(i)
    for n in listaCompleta:
        if n not in ordenadaAscendenteSinRepetidos:
            losQueNoEstan.append(n)
    print(losQueNoEstan)
