# Entrada = 1, 2, 3 --- Salida = 1, 1.5, 2
entrada = [3, 2, 1, 4, 5]

def promedio(lista):
    return sum(lista) / len(lista)

salida = []
for i in range(len(entrada)):
    salida.append(promedio(entrada[:i+1]))

print(entrada)
print(salida)

