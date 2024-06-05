lista = [11, 2, 1, 11, 3, 4, 11, 1, 33, 1]

def devuelveMaximos(numeros):
    print(numeros)
    contadores = []
    valores = []

    for n in numeros:
        try:
            posi = valores.index(n) # index devuelve la posición del argumento en la lista
            contadores[posi] += 1
        except Exception:  
            valores.append(n)
            contadores.append(1)

    #print(valores, contadores)

    maximos = []
    for i in range(len(contadores)):
        if contadores[i] == max(contadores): # max devuelve el máximo
            maximos.append(valores[i])

    return maximos

print(*devuelveMaximos(lista)) # * desempaqueta (para no mostrar los corchetes)
print(*devuelveMaximos([1,2,1]))


    

