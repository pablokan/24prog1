#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.

nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana","Santamaría, Carlos","Skarsgard, Azul","Catalejos, Walter"]
listaSexos = ["f","f","m","f","m","f","m"]
listaFechas = ["02/05/1943","07/04/1984","10/02/1971","21/12/1967","30/01/1982","30/08/1995","18/07/1959"]
listaNombres=["Ana", "Kate", "Benicio", "Susana", "Carlos", "Azul", "Walter"]
listaApellidos=["Torres", "Hudson", "Quesada", "Campoamores", "Santamaria", "Skarsgard", "Catalejos"]

#lo que hice con ayuda porque si no ni arrancaba  
for nombre in listaNombres:    
    iniciales = nombre[0]
    
    for apellido in listaApellidos:
        apCompleto = apellido
    
    nombreCompleto= iniciales + ". " + apCompleto
    print(nombreCompleto)
#no se como hacer para que coicida la inicial con el appellido


#2) Decir cuál es el nombre de pila más largo.
#en este ya me quede sin tiempo
for letra in range(len(listaNombres)):
    largo=0
    print(letra)

if letra > 0:
    nombre = largo
    print("El nombre mas largo es ", largo)

#ni llegue
#3) Mostrar el promedio de edad de las mujeres. 
