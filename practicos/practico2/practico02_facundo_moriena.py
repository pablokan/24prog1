personas = [
    "Josefa Taponales,France(Europe),30-10-2007",
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
año=int(input("ingrese el año que deseé:"))
print("Los apellidos de las personas nacidas antes del",año,"son")

for x in range(len(personas)):
  str(personas[x])
  nombres,_pais,fecha=personas[x].split(",")
  _nombre,apellido=nombres.split(" ")
  _dia,_mes,años=fecha.split("-")
  if int(años)<año:
   print(apellido)

#2
contador=0
paisIngresado=input("ingrese un pais(in english pls)")
paisIngresado=paisIngresado.title()

for x in range(len(personas)):
 str(personas[x])
 _nombres,paises,_fecha=personas[x].split(",")
 pais,continente=paises.split("(")
 if pais==paisIngresado:
   contador+=1
  
print("La cantidad de personas de ",paisIngresado,"es ",contador)

añoComparador,mesComparador,diaComparador=0,0,0
masJoven=""
#3
for x in range(len(personas)):
 str(personas[x])
 nombres,paises,fecha=personas[x].split(",")
 pais,continente=paises.split("(")
 continentes=continente[0:-1]
 nombre,_apellido=nombres.split(" ")
 dia,mes,años=fecha[0:2],fecha[3:5],fecha[6:]
 if continentes=="Europe":
   if int(años)>añoComparador or (int(años)==añoComparador and int(mes)>mesComparador) or (int(años)==añoComparador and int(mes)==mesComparador and int(dia)>dia) :
     diaComparador=int(dia)
     mesComparador=int(mes)
     añoComparador=int(años)
     masJoven=nombre
print(diaComparador,mesComparador,añoComparador)
     
    
      
     
     
     

print("La persona mas joven de Europa es ",masJoven)      


           
  
    
  
