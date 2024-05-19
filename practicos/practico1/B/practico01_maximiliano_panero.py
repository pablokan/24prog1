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


#1) Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas.
nom_str=str(nombres)
for x in range(len(nombres)):
    posi_coma  =nom_str.find(",")
    apellidos=nom_str[posi_coma:] #hasta aca llegue, no se como se corta una lista si no es str y en este caso si es str me busca la primera (,) por ciclo

nombres = "Juan y Lisa"
posicionY = nombres.find('y')
nombre1 = nombres[:posicionY]
nombre2 = nombres[posicionY+2:]        #la referencia que quise usar:
print(nombre1)
print(nombre2)
print(nombres.split()) 




    
   