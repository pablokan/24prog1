# Datos del 2008 en un string
nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

# Datos del 2018 en listas
ranks2018 = [1, 2, 3, 4, 5]
male_names2018 = ['Liam', 'Noah', 'Michael', 'James', 'Oliver']
male_numbers2018 = [19837, 18267, 14516, 13525, 13389]
female_names2018 = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia']
female_numbers2018 = [18688, 17921, 14924, 14464, 13928]

# Convertir los datos del 2008 en listas
nacidos2008 = nacidos2008.split(',')

# Inicializar listas para nombres y números
male_names2008 = []
male_numbers2008 = []
female_names2008 = []
female_numbers2008 = []

# Rellenar las listas con los datos de 2008
for i in range(0, len(nacidos2008), 3):
    name = nacidos2008[i]
    number = int(nacidos2008[i+1])
    sex = nacidos2008[i+2]
    if sex == 'm':
        male_names2008.append(name)
        male_numbers2008.append(number)
    else:
        female_names2008.append(name)
        female_numbers2008.append(number)

# Ordenar las listas de 2008 por número de nacimientos de mayor a menor
sorted_male_indices_2008 = sorted(range(len(male_numbers2008)), key=lambda i: male_numbers2008[i], reverse=True)
sorted_female_indices_2008 = sorted(range(len(female_numbers2008)), key=lambda i: female_numbers2008[i], reverse=True)

sorted_male_names2008 = [male_names2008[i] for i in sorted_male_indices_2008]
sorted_male_numbers2008 = [male_numbers2008[i] for i in sorted_male_indices_2008]

sorted_female_names2008 = [female_names2008[i] for i in sorted_female_indices_2008]
sorted_female_numbers2008 = [female_numbers2008[i] for i in sorted_female_indices_2008]
