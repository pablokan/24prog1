'''
PRACTICO 1 (DIAGNOSTICO) PEREZ LUCAS

Procesos para las salidas:

1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

2) Decir cuál es el nombre de pila más largo.

3) Mostrar el promedio de edad de las mujeres. 

'''

nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"
        ] 

print('1: Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas: ')

for nombre_completo in nombres:
        apellido, nombre = nombre_completo.split(', ')
        inicial = nombre[0]
        print(f"{inicial}. {apellido}")

print('2) Decir cuál es el nombre de pila más largo.')
largo = 0
nombre_largo = ''

for nombre_completo in nombres:
        apellido, nombre = nombre_completo.split(', ')
        if len(nombre) > largo:
            largo = len(nombre)
            nombre_largo = nombre


print (f'El nombre mas largo es: {nombre_largo}')




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

print('3: Mostrar el promedio de edad de las mujeres.')
edad=0
edades=0

fecha_de_hoy = '02/05/2024'
dia_hoy, mes_hoy, año_hoy = fecha_de_hoy.split('/')
dia_hoy= int(dia_hoy)
mes_hoy= int(mes_hoy)
año_hoy= int(año_hoy)

for fecha in fechas:
       dia, mes, año = fecha.split('/')
       dia = int(dia)
       mes = int(mes)
       año = int(año)
       edad= año_hoy - año - ((mes, dia) > (mes_hoy, dia_hoy))
       edades = edades + edad

print (f'Promedio de edad de las mujeres: {edades/len(fechas)} años')