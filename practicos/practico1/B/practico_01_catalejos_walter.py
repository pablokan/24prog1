#Mostrar las iniciales de los nombres con un punto, luego un espacio y finalmente el apellido completo de todas las personas
nombres = ["Torres, Ana","Hudson, Kate","Quesada, Benicio","Campoamores, Susana", "Santamaría, Carlos","Skarsgard, Azul", "Catalejos, Walter"]
for nombres in nombres:
    nombres= nombres.split()
    iniciales= " ".join ([nombre[0] + "." for nombre in nombres [:-1]])
    apellido= nombres[-1]
    print(f"{iniciales} {apellido}")

#hasta aca llegue profe la verdad trate de solucionarlo un poco con lo que vimos anoche, pero bueno estoy tratando de alentar los practicos! 