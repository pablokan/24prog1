# salida -> 'Juan le lleva 7 años a Pedro'

nombre1 = 'Juan'
edad1 = 12
nombre2 = 'Pedro' 
edad2 = 15 

if edad1 > edad2:
    salida = f'{nombre1} le lleva {edad1-edad2} años a {nombre2}'
else:
    salida = nombre2 + " le lleva " + str(edad2-edad1) + " años a " + nombre1

print(salida)
