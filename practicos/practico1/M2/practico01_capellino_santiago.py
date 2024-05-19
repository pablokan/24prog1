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
apellido = ''
iniciales = []

for nombre in nombres: # no profe, ni idea como puedo separar los nombres con las iniciales, ni como recorrer str que estan dentro de una lista, esto que hice aca lo busque en google porque no pude hacerlo
    for char in nombre:
        if char != ',': # se me ocurre una forma usando .split pero se supone que no se necesita
            iniciales.append(char)
            break
print(iniciales)