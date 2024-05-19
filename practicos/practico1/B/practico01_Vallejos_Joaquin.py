#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
#2) Decir cuál es el nombre de pila más largo.
#3) Mostrar el promedio de edad de las mujeres. 

nombres = ["Ana","Kate","Benicio","Susana","Carlos","Azul", "Walter"] 
apellidos = ["Torres","Hudson","Quesada","Campoamores", "Santamaría","Skarsgard","Catalejos"] # No supe como separar los apellidos de los nombres y lo hice yo a mano
sexos = ["f","f","m","f","m","f","m"]
fechas = ["02/05/1943","07/04/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]

print('1) Iniciales y apellido de las personas: ')
for x in range(len(nombres)):
    iniciales = str(nombres[x][:1])
    apel = str(apellidos[x])
    uno = iniciales + '. ' + apel
    print(uno)


nameLargo = ''
largoPalabra = 0
for nombre in nombres:
     if len(nombre) > largoPalabra:
          largoPalabra = len(nombre)
          nameLargo = nombre
print('2) El nombre más largo es:', nameLargo)

# No llegue con el tiempo porque en las primeras me costo darme cuenta de como resolver algunas cosas