# Datos del 2008
nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

# Datos del 2018
nacidos2018 = [
    {"rank": 1, "male_name": "Liam", "male_count": 19837, "female_name": "Emma", "female_count": 18688},
    {"rank": 2, "male_name": "Noah", "male_count": 18267, "female_name": "Olivia", "female_count": 17921},
    {"rank": 3, "male_name": "Michael", "male_count": 14516, "female_name": "Ava", "female_count": 14924},
    {"rank": 4, "male_name": "James", "male_count": 13525, "female_name": "Isabella", "female_count": 14464},
    {"rank": 5, "male_name": "Oliver", "male_count": 13389, "female_name": "Sophia", "female_count": 13928}
]

# Procesar datos del 2008
nacidos2008_list = [x.split(',') for x in nacidos2008.split(',f,')[0::2] + nacidos2008.split(',m,')[0::2]]
nacidos2008_dict = [{"rank": i+1, "name": x[0], "count": int(x[1]), "sex": x[2]} for i, x in enumerate(nacidos2008_list)]

# Función para calcular la diferencia en cantidad de bebés
def diff_count(rank, sex):
    for x in nacidos2018:
        if x["rank"] == rank and (x["male_name"] if sex == "m" else x["female_name"]):
            count2018 = x["male_count"] if sex == "m" else x["female_count"]
            break
    for x in nacidos2008_dict:
        if x["rank"] == rank and x["sex"] == sex:
            count2008 = x["count"]
            break
    return count2018 - count2008

# Función para encontrar nombres que comienzan con la misma letra
def find_names_by_letter(letter):
    names = [x["name"] for x in nacidos2018 + nacidos2008_dict if x["name"][0].lower() == letter.lower()]
    return names

# Función para encontrar nombres que se repiten en ambos años
def find_repeated_names():
    names2018 = [x["male_name"] for x in nacidos2018] + [x["female_name"] for x in nacidos2018]
    names2008 = [x["name"] for x in nacidos2008_dict]
    return [x for x in names2018 if x in names2008]

# Ejecutar funciones
print("Diferencia en cantidad de bebés:")
rank = int(input("Ingrese la posición: "))
sex = input("Ingrese el sexo (m/f): ")
print(diff_count(rank, sex))

print("\nNombres que comienzan con la letra:")
letter = input("Ingrese la letra: ")
print(find_names_by_letter(letter))

print("\nNombres que se repiten en ambos años:")
print(find_repeated_names())