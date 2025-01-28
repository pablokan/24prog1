# crea una lista de diccionarios de 10 paises con 5 datos cada uno, al menos un país de cada continente
paises = [
    {"nombre": "España", "capital": "Madrid", "continente": "Europa"},
    {"nombre": "Estados Unidos", "capital": "Washington DC", "continente": "América del Norte"},
    {"nombre": "Argentina", "capital": "Buenos Aires", "continente": "Sudamérica"},
    {"nombre": "Australia", "capital": "Canberra", "continente": "Oceania"},
    {"nombre": "India", "capital": "New Delhi", "continente": "Asia"},
    {"nombre": "Kenia", "capital": "Nairobi", "continente": "África"},
    {"nombre": "China", "capital": "Pekín", "continente": "Asia"},
    {"nombre": "Rusia", "capital": "Moscú", "continente": "Europa"},
    {"nombre": "Brasil", "capital": "Brasilia", "continente": "América del Sur"}
]
# imprime la lista de las capitales ordenadas alfabéticamente
capitales = []
for pais in paises:
    capitales.append(pais["capital"])

print(sorted(capitales))
# agrega las poblaciones reales de los paises
for pais in paises:
    if pais["nombre"] == "España":
        pais["poblacion"] = 46928000
    elif pais["nombre"] == "Estados Unidos":
        pais["poblacion"] = 331002651
    elif pais["nombre"] == "Argentina":
        pais["poblacion"] = 45195777
    elif pais["nombre"] == "Australia":
        pais["poblacion"] = 25365000
    elif pais["nombre"] == "India":
        pais["poblacion"] = 1380004385
    elif pais["nombre"] == "Kenia":
        pais["poblacion"] = 53791664
    elif pais["nombre"] == "China":
        pais["poblacion"] = 1402112000
    elif pais["nombre"] == "Rusia":
        pais["poblacion"] = 145934462
    elif pais["nombre"] == "Brasil":
        pais["poblacion"] = 212559417

# imprime la lista de los paises ordenados por población (solo los nombres)
paises_ordenados = sorted(paises, key=lambda pais: pais["poblacion"])
for pais in paises_ordenados:
    print(pais["nombre"])
    

























