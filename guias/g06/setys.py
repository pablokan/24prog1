s1 = 'hola'
s2 = 'moni'
print(set(s1))
letras = {chr(x) for x in range(97, 123)}.union(set('áéíóúñ'))
print(letras)