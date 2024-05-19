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


# 1. Iniciales y apellido de las personas
inicialesApellido = []

for i in nombres:
    partesNombre = i.split(', ')
    apellido = partesNombre[0]
    inicialNombre = partesNombre[1][0] + '.'
    nombreCompleto = inicialNombre + ' ' + apellido
    inicialesApellido.append(nombreCompleto)
print ('\niniciales y apellidos de las personas: ')
for i in inicialesApellido:
    print(i)


# 2. El nombre más largo 
nombreMasLargo = ''
for i in nombres:
    partesNombre = i.split(', ')
    nombrePersona = partesNombre[1] 
    if len(nombrePersona) > len(nombreMasLargo):
        nombreMasLargo = nombrePersona

print('\nEl nombre más largo es:', nombreMasLargo)


# 3. El promedio de edad de las mujeres 
hoy = '02/05/2024'  

fechasNacimiento = []
for fecha in fechas:
    partesFecha = fecha.split('/')
    dia = int(partesFecha[0])
    mes = int(partesFecha[1])
    anio = int(partesFecha[2])
    fechasNacimiento.append((dia, mes, anio))
    
edadesMujeres = []
for i in range(len(fechasNacimiento)):
    if sexos[i] == 'f':
        fecha = fechasNacimiento[i]
        diferenciaAnios = int(hoy[-4:]) - fecha[2]
        if fecha[1] > int(hoy[3:5]) or (fecha[1] == int(hoy[3:5]) and fecha[0] > int(hoy[:2])): # <-- aca tuve que buscar como hacer la condicion para calcular la edad ._.
            diferenciaAnios -= 1
        edadesMujeres.append(diferenciaAnios)

promedioEdadMujeres = sum(edadesMujeres) // len(edadesMujeres)

print('\nEl promedio de edad de las mujeres es:', promedioEdadMujeres)