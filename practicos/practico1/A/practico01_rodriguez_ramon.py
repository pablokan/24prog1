
lista = [
    ["Torres, Ana", "f", "02/05/1943"],
    ["Hudson, Kate", "f", "07/04/1984"],
    ["Quesada, Benicio", "m", "10/02/1971"],
    ["Campoamores, Susana", "f", "21/12/1967"],
    ["Santamaría, Carlos", "m", "30/01/1982"],
    ["Skarsgard, Azul", "f", "30/08/1995"],
    ["Catalejos, Walter", "m", "18/07/1959"],]

for persona in lista:
    apellido_nombre = persona[0]
    
    apellido= apellido_nombre.split()[0] 
    nombre= apellido_nombre.split ()[1] 
    primeraletra= nombre[0][0]+". "
    
    print (primeraletra + apellido.strip (","))
    
    
    
    
   
    
   
    
    






