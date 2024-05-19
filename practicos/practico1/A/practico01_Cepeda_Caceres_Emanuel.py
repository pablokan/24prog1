#Cepeda Caceres Emanuel. Dni 35543865 Comicion "A".
#elegi la lista paralela
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
lista_aux = nombres
letra=[]
ape = []
posi = 0
lista_aux = '.'.join(nombres)

while posi != -1:
    posi = lista_aux.find(' ',posi)
    if posi != -1:
        posi +=1
        letra.append(lista_aux[posi:posi+1])
posi = 0
res = 0
        
while posi != -1:
    posi = lista_aux.find(',',posi)
    if res == 0 and posi!= -1:
        ape.append(lista_aux[res:posi])
        res = posi
        posi +=1
    elif res != 0 and posi != -1:
        res = lista_aux.find('.',res)
        ape.append(lista_aux[res+1:posi])
        res +=1
        posi +=1

nombres_junto = []
for i in range(len(ape)):
    nombres_junto.append(letra[i]+'. '+ape[i])

posi = 0
res = 0
nomb = []  
while posi != -1:
    posi = lista_aux.find('.',posi)
    res = lista_aux.find(' ',res)
    if res != -1 and posi != -1:
        nomb.append(lista_aux[res+1:posi])
        res +=1
        posi +=1
        
print('1)Iniciales y apellido de las personas: ')
for i in range(len(nombres_junto)):
    print(nombres_junto[i])         
mayor = 0
pila = ''
for i  in range(len(nomb)):
    if mayor <= len(nomb[i]):
        pila = nomb[i]
        mayor = len(nomb[i])
        
print(f'\n2)El nombre mas largo es "{pila}"') 

femeninos=[]
for i in range(len( sexos)):
    if sexos[i] == 'f':
        femeninos.append(fechas[i])

fech = '.'.join(femeninos)
fech = fech + '.'
posi = 0
fech_aux = []  
while posi != -1:
    posi = fech.find('.',posi)
    if posi != -1:
        fech_aux.append(int(fech[posi-4:posi]))
        posi +=1

anio_v=2024
promedio = 0
for i in range(len(fech_aux)):
    anio_v -= fech_aux[i]
    promedio += anio_v
    anio_v = 2024 

print(f'\n3)El promedio de edad de mujeres es {promedio//len(fech_aux)}')

