# Recorrer la lista nombres, filtrar por la lista paralela sexos e ir cargando la nueva lista mujeres

nombres = ["Ana", "Luis", "Carlos", "María"]
sexos = ["F", "M", "M", "F"]
mujeres = []
for i in range(len(sexos)):
    if sexos[i] == 'F':
        mujeres[i] = nombres[i]
print('La cantidad total de mujeres es', len(mujeres))

