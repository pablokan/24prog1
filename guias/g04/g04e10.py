frase = "Quiero comer manzanas, solamente manzanas."
vocales = ['a', 'e', 'i', 'o', 'u']
cantidades = [0, 0, 0, 0, 0]
for i in range(len(vocales)):
    for letra in frase:
        if vocales[i] == letra:
            cantidades[i] += 1

maximo = 0
for i in range(len(vocales)):
    if cantidades[i] > maximo:
        maximo = cantidades[i]
        letraMasRepetida = vocales[i]

print(f'La letra mas repetida es la "{letraMasRepetida}" y aparece {maximo} veces')