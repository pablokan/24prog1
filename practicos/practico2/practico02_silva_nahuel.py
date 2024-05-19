#Quiero obtener:
#Los apellidos de las personas nacidas antes de un año solicitado al usuario.
#La cantidad de personas nacidas en un país ingresado por el usuario.
#El nombre de pila de la persona más joven de Europe.
personas = [
    "Josefa Taponales,France(Europe),30-01-2000",
    "Virgie Brach,Argentina(America),04-02-1994",
    "Adeline Quispe,United States(America),18-06-2002",
    "Willy Branscombe,Norway(Europe),21-11-2007",
    "Diane Piffe,France(Europe),07-08-1993",
    "Britta Causbey,Germany(Europe),24-01-2000",
    "Elisabeth Cleeve,Norway(Europe),04-03-1991",
    "Sasha Ivanchenkov,Argentina(America),28-04-2002",
    "Zerk Milsom,Norway(Europe),03-12-1994",
    "Kathryn Backshell,United States(America),04-01-2000"
]
#1
apellidos = []
año = []
añopedido = int(input('ingrese año limite'))
for i in range(len(personas)):
    espacio = personas[i].find(' ')
    coma = personas[i].find(',')
    apellidos.append(personas[i][espacio+1:coma])
    año.append(int(personas[i][-4:]))
print(f'apellidos de las personas nacidas antes del año {añopedido} son :')    
for i in range(len(año)):
    if año[i] < añopedido :
        print(apellidos[i])
print()        
#2
contador = 0
paisIngresado = input('ingrese pais')
for i in range(len(personas)):
    coma = personas[i].find(',')
    parentesis = personas[i].find('(')   
    if paisIngresado == personas[i][coma+1:parentesis] :
        contador = contador +1
print()        
print(f'la cantidad de personas de {paisIngresado} son {contador}')
#3
nombre = []
añoNac = []
for i in range(len(personas)):
    espacio = personas[i].find(' ')
    parentesis = personas[i].find('(')
    if personas[i][parentesis+1:parentesis+7] =='Europe':
        nombre.append(personas[i][:espacio])   
        añoNac.append(personas[i][parentesis+9:])
edadMenor = 99      
for i in range(len(nombre)):
    fecha = añoNac[i]      
    diaNac = int(fecha[:2])
    mesNac = int(fecha[3:5])
    añoNaci = int(fecha[6:])  
    diaHoy, mesHoy, añoHoy = 6,5,2024
    edad = añoHoy - añoNaci
    if (mesNac > mesHoy) or (mesHoy == mesNac and diaHoy < diaNac):
            edad = edad - 1        
    if edadMenor > edad :    
        edadMenor = edad
        nombreMenor = nombre[i]   
print()                
print(f'la persona mas joven de europa es {nombreMenor}')