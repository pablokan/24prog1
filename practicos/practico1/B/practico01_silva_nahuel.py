#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
#2) Decir cuál es el nombre de pila más largo.
#3) Mostrar el promedio de edad de las mujeres. 

datos = [
    "Torres, Ana, f, 02/05/1943",
    "Hudson, Kate, f, 07/04/1984",
    "Quesada, Benicio, m, 10/02/1971",
    "Campoamores, Susana, f, 21/12/1967",
    "Santamaría, Carlos, m, 30/01/1982",
    "Skarsgard, Azul, f, 30/08/1995",
    "Catalejos, Walter, m, 18/07/1959",
]
#1
apellido = []
nombres = []
print('lista de nombres antecedidos por inicial de apellido y punto : ')
print()
for i in range(len(datos)):
   coma = datos[i].find(',')
   nombres.append(datos[i][coma+2:-15])
   apellido.append(datos[i][:coma])
   print(apellido[i][0]+'. '+nombres[i])
print()   
#2)
nombreDePila = 0
pilaMasLargo = ''
for i in range(len(nombres)) :
   cantidadLetras = len(nombres[i])
   if cantidadLetras > nombreDePila :
      nombreDePila = cantidadLetras
      pilaMasLargo = nombres[i]
print(f'El nombre de pila mas largo es {pilaMasLargo}')
print()
#3
fecha = []
sexo = []
for i in range(len(datos)):
    sexo.append(datos[i][-13:-12]) 
    if sexo[i] == 'f' :
      fecha.append(datos[i][-10:])
sumador = 0     
for i in range(len(fecha)):
    dividir = fecha[i]      
    diaNac = int(dividir[:2])
    mesNac = int(dividir[3:5])
    añoNac = int(dividir[6:])  
    diahoy, meshoy, añohoy = 30,4,2024
    edad = añohoy - añoNac
    if (mesNac > meshoy) or (meshoy == mesNac and diahoy > diaNac):
        edad = edad - 1 
        sumador = sumador + edad
    else :
       sumador = sumador + edad    
promedio = sumador / len(fecha)       
print(f'el promedio de edad de las mujeres es : {promedio}')
print()