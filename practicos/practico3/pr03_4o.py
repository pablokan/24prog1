# Datos del 2008 en un string
nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

# Datos del 2018 en una estructura más manejable (lista de diccionarios)
data2018 = [
    {'rank': 1, 'male_name': 'Liam', 'male_number': 19837, 'female_name': 'Emma', 'female_number': 18688},
    {'rank': 2, 'male_name': 'Noah', 'male_number': 18267, 'female_name': 'Olivia', 'female_number': 17921},
    {'rank': 3, 'male_name': 'Michael', 'male_number': 14516, 'female_name': 'Ava', 'female_number': 14924},
    {'rank': 4, 'male_name': 'James', 'male_number': 13525, 'female_name': 'Isabella', 'female_number': 14464},
    {'rank': 5, 'male_name': 'Oliver', 'male_number': 13389, 'female_name': 'Sophia', 'female_number': 13928},
]

# Función para convertir los datos del 2008 en una estructura más manejable
def parse_2008_data(data):
    parts = data.split(',')
    parsed_data = []
    for i in range(0, len(parts), 3):
        name, number, sex = parts[i], int(parts[i+1]), parts[i+2]
        parsed_data.append({'name': name, 'number': number, 'sex': sex})
    return parsed_data

data2008 = parse_2008_data(nacidos2008)

# Crear listas específicas para cada sexo y ordenar por el número de nacimientos
male_data2008 = sorted([entry for entry in data2008 if entry['sex'] == 'm'], key=lambda x: x['number'], reverse=True)
female_data2008 = sorted([entry for entry in data2008 if entry['sex'] == 'f'], key=lambda x: x['number'], reverse=True)

# Parte 1: Diferencia en cantidad de bebés entre los nombres de misma posición y mismo sexo
def diferencias(data2008, data2018):
    for i in range(5):
        # Varones
        male_diff = male_data2008[i]['number'] - data2018[i]['male_number']
        print(f"Varones en posición #{i+1}: {abs(male_diff)} nacimientos de diferencia entre {male_data2008[i]['name']} del 2008 y {data2018[i]['male_name']} del 2018")
        
        # Mujeres
        female_diff = female_data2008[i]['number'] - data2018[i]['female_number']
        print(f"Mujeres en posición #{i+1}: {abs(female_diff)} nacimientos de diferencia entre {female_data2008[i]['name']} del 2008 y {data2018[i]['female_name']} del 2018")

diferencias(data2008, data2018)

# Parte 2: Nombres que comienzan con la misma letra en ambos periodos
def nombres_con_inicial(letra, data2008, data2018):
    nombres2008 = [entry['name'] for entry in data2008 if entry['name'].startswith(letra)]
    nombres2018 = [entry['male_name'] for entry in data2018 if entry['male_name'].startswith(letra)] + \
                  [entry['female_name'] for entry in data2018 if entry['female_name'].startswith(letra)]
    
    nombres = set(nombres2008 + nombres2018)
    print(f"Nombres con {letra}: {' '.join(sorted(nombres))}")

letra_inicial = input("Ingrese la letra inicial: ")
nombres_con_inicial(letra_inicial, data2008, data2018)

# Parte 3: Nombres que se repiten en ambos años
def nombres_repetidos(data2008, data2018):
    nombres2008 = {entry['name'] for entry in data2008}
    nombres2018 = {entry['male_name'] for entry in data2018} | {entry['female_name'] for entry in data2018}
    
    repetidos = nombres2008 & nombres2018
    print(f"Nombres que se repiten: {' '.join(sorted(repetidos))}")

nombres_repetidos(data2008, data2018)
