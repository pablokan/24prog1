datos =   ["Torres, Ana", "f", "02/05/1943"],["Hudson, Kate", "f", "07/04/1984"],["Quesada, Benicio", "m", "10/02/1971"],["Campoamores, Susana", "f", "21/12/1967"],    ["Santamaría, Carlos", "m", "30/01/1982"],["Skarsgard, Azul", "f", "30/08/1995"],
apellido=[]
inicial= []
nombres= []
contador=[]
sexo = []
fecha=[]
nombre=''
for p in datos:
    dato= p[0]
    f=p[2]
    fac=f.replace('/',' ')
    fec_cha=fac[6:10]
    fecha.append(fec_cha)
    sex= p[1]
    sexo.append(sex)
    nom_apell=dato.replace(',','')
    aux=nom_apell.split()
    inicial.append(aux[1][0])
    apellido.append(aux[0])
    nombres.append(aux[1])


completo='. '.join(inicial)
print('1) iniciales y apellidos de las personas:')
for i in range(len(inicial)):
        print(inicial[i],'.',apellido[i])

contado=0

for i  in range(len(nombres)):
       (len(nombres[i]))
       contador.append(len(nombres[i]))
       if contador[i]>contado:
             contado=contador[i]
             nombre=nombres[i]
print(f'2) El nombre mas largo es {nombre}')
actual=2024
año=[]
edad=[]
promedio= []
fecha_mujeres=[]      
total=[]
for i in range(len(sexo)):
      if sexo[i]== 'f':
        fecha_mujeres.append(fecha[i])
      
for i in range(len(fecha_mujeres)):
      edad.append((actual-int(fecha_mujeres[i])))
total=sum(edad)   
promedio=int((total)/len(edad))

print(f'3) el promedio de la edad de las mujeres es:{promedio}')





