nombres = ["Torres, Ana", "Hudson, Kate", "Quesada, Benicio", "Campoamores, Susana", "Santamaría, Carlos", "Skarsgard, Azul", "Catalejos, Walter"] 
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943", "07/04/1984", "10/02/1971", "21/12/1967", "30/01/1982", "30/08/1995", "18/07/1959"]

inicial_nombres = [nombre.split (", ") [1][0] + ". " + nombre.split (", ") [0] for nombre in nombres]
print ("Iniciales y apellidos completos:")
for nombre_completo in inicial_nombres:
    print (nombre_completo)

nombre_mas_largo = ""
for nombre in nombres:
    nombre_pila = nombre.split(", ")[1]
    if len(nombre_pila) > len(nombre_mas_largo):
        nombre_mas_largo = nombre_pila

print("El nombre de pila más largo es:", nombre_mas_largo)

hoy_dia, hoy_mes, hoy_anio = 30, 4, 2024

print('Los mayores de edad son:')
contador = 0
suma_edades = 0

for i in range(len(fechas)):
    if sexos[i] == "f":
        edad_mujeres = hoy_anio - int(fechas[i].split("/")[2]) - ((hoy_mes, hoy_dia) < (int(fechas[i].split("/")[1]), int(fechas[i].split("/")[0])))
        contador = contador + 1
        suma_edades = suma_edades + edad_mujeres

promedio_edad = suma_edades / contador

print("El promedio de edad de las mujeres es:", round(promedio_edad, 2))





