nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter",
        
       
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
 
#1 mostrar nombre ej(F.moriena)
nombresSeparados=[]
for i in range(len(nombres)):
     nombresString=str(nombres[i])
     inicial=nombresString[0]
     separador=nombresString.find(" ")
     apellido=nombresString[separador:]
     nombresfinal=inicial+"."+" "+apellido
     print(nombresfinal)


#2 mostrar nombre mas largo
soloNombre=[]
#guarda solo los nombres en una lista(solonombres)
for i in range(len(nombres)):
     nombreString=str(nombres[i])
     separar=nombreString.find(",")
     soloNombre.append(nombreString[0:separar])

#recorre la lista solonombres para decir cual es el nombre con mas caracteres 
contadorDeLetras=0
nombreMasLargo=""
for i in range(len(soloNombre)):
     x=len(str(soloNombre[i]))
     if x>contadorDeLetras:
          contadorDeLetras=x
          nombreMasLargo=soloNombre[i]

print("El nombre mas largo es: ",nombreMasLargo)     

#3 sacar el promedio de edad de las mujeres
mujeres=[]
#separa entre hombres y mujeres,guarda las mujeres en la variable(mujeres)
for i in range(len(sexos)):
     if sexos[i]=="f":
          mujeres.append(nombres[i])

diaLista=[]
mesLista=[]
añoLista=[]

#separa dia,mes,año
for i in range(len(mujeres)):
     fechaString=str(fechas[i])
     separadordia=fechaString.find("/")
     dia=fechaString[0:separadordia]
     diaLista.append(int(dia))
     mes=fechaString[separadordia+1:separadordia+3]
     mesLista.append(int(mes))
     año=fechaString[separadordia+4:]
     añoLista.append(int(año))


#saca promedio,si todavia no cumplio se le resta 1 al año

contadorAños=0
cantidad=0
  

for i in range(len(diaLista)):
     if diaLista[i]>3 and mesLista[i]==5:
          contadorAños+=2024-(añoLista[i]-1)
          cantidad+=1
     elif mesLista[i]>5:
          contadorAños+=2024-(añoLista[i]-1)
          cantidad+=1
    
     else:
          contadorAños+=2024-añoLista[i]
          cantidad+=1

promedio= contadorAños/cantidad
print("El promedio de edad de las mujeres es:",int(promedio))     
    
           
          

     
     
     


          



     
     
  




