def suma(*args):
    total = 0
    for valor in args:
        total += valor
    return total

print(suma(1,2,3,4))
print(suma())

def saludo(nombre, ciudad='Río Cuarto'):
    print(f'Hola {nombre}, sos de {ciudad}')

saludo('Vilma', 'Sampacho')
saludo('Juan')
