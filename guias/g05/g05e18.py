# un set o conjunto es una estructura de datos, es decir, una variable de almacenamiento múltiple que tiene dos características: 1) no hay repetición de elementos y 2) no hay orden
s1 = {'a', 'e', 'i', 'o', 'u'} # conjunto
s2 = 'miau'
s2 = set(s2) # convierte s2 a conjunto
print(s2)
s3 = s1.intersection(s2)
print(f'{s3=}') # truco para mostrar el nombre de la variable y su contenido
if  s3 == s1:
    print('todas')
else:
    print(f'faltan {s1 - s3}')