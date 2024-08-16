pos = [0, 0]
direcciones = [[1, 1], [-1, 0], [-1, 1], [1, 0]]
i = 0
ordenes = [10, 5, -2, -11, 4]
for o in ordenes:
    pos[direcciones[i][1]] += (o * direcciones[i][0])
    i = i + 1 if i < 3 else 0
print(pos)
