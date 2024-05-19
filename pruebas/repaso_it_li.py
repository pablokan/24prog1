""" 
lista = [111, 222, 999]
numeroAbuscar = int(input('ingrese numero a buscar: '))
if numeroAbuscar in lista:
    print('ta')
else:
    print('no ta')
"""

letras = ['q', 'a', 'e', 'z', 'z','i','z','i','z','z']

c = 0
for i in range(len(letras)):
    if letras[i] in ['a', 'e', 'i', 'o', 'u']:
        c = c + 1
print(c)
