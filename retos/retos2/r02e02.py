lista = [7, 2, 1, 2, 3, 3, 3, 4, 2, 4, 1, 8]
bumeranes = []
for i in range(len(lista)-2):
    if lista[i] == lista[i+2] and lista[i] != lista[i+1]:
        bumeran = [lista[i], lista[i+1], lista[i+2]]
        bumeranes.append(bumeran)
print(bumeranes)
