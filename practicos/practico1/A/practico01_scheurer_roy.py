# no llegue con el tiempo profe, disculpe

nombres = [
        "Torres, Ana",
        "Hudson, Kate",
        "Quesada, Benicio",
        "Campoamores, Susana", 
        "Santamaría, Carlos",
        "Skarsgard, Azul", 
        "Catalejos, Walter"   ] 

sexos = ["f","f","m","f","m","f","m"]

fechas = [
"02/05/1943",
"07/04/1984",
"10/02/1971",
"21/12/1967",
"30/01/1982",
"30/08/1995",
"18/07/1959" ]

i = 0
nom = []
apellidos = []


""" for i in nombres: 
    pos = nombres[i].split(',')
    nom.append(pos)
 """
for nombre in nombres:
    apellido, nombre_comp = nombre.split(", ")
    apellidos.append(apellido)
    nom.append(nombre_comp)

for nombre in nombres:
    apellido, nombre_completo = nombre.split(", ")
    primLetra = nombre_completo[0]  
    print(primLetra + ". " + apellido)


print(nom)

""" for i in range (len(nom[i])):
    max = nom[1]
    if nom[i] >  """


maxi = max(nom)
print('El nombre mas largo es: ', maxi) 










""" for i in range (len(nom)): 
    posi = nom[i].find(',')
    palabra1 = nom[:posi]
    apellidos.append(posi)
 """

'''for i in range (len(nom)):
    posi = nom[i].find(',')
    palabra1 = nom[:posi]
    apellidos.append(palabra1)
    print(nom[i])'''
        