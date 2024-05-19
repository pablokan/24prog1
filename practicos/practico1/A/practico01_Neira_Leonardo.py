nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
]

sexos = ["f","f","m","f","m","f","m"]

fechas = [
"02/05/1943",
"07/04/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959"
]

for nombreCompleto in nombres:
    nombreCompletoLimpio = nombreCompleto.replace(",", "")
    nombre, apellido = nombreCompletoLimpio.split()
    print(f"{apellido[0]}. {nombre}")

print("")
nombreLargo = ""

for nombreCompleto in nombres:
    nombreCompletoLimpio = nombreCompleto.replace(",", "")
    apellido, nombre = nombreCompletoLimpio.split()
    if len(nombre)>len(nombreLargo):
        nombreLargo=nombre
print("El nombre mas largo es: "+nombreLargo)    

# sumaEdad = 0
# conteoMujeres= 0

# fechaActual = [2,5,2024]

# for i in range(len(fechas)):
#     if sexos[i]=="f":
#         partesFechas=fechas[i].split("/")
#         dia = int(partesFechas[0])
#         mes = int(partesFechas[1])
#         anio = int(partesFechas[2])
#         edad= fechaActual[2]-anio-((fechaActual[1], fechaActual[0])<(mes, dia))
#         sumaEdad+=edad
#         conteoMujeres+=1
# promedio = sumaEdad / conteoMujeres if conteoMujeres > 0 else 0
# print("el promedio de edad de las mujeres es: "+ promedio)


