personas = ['Juan', 'Ana', 'Pedro', 'Luis']

for i in range(len(personas)):
    for j in range(i + 1, len(personas)):
        print(f'{personas[i]} le da la mano a {personas[j]}')

