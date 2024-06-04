def foo(): # función definida por el programador
    print('hola, soy la función foo')

def bar():
    return 'soy la frase retornada por la función bar' # devuelve la string

def masLarga():
    a = 2
    b = 3
    return a - b

# Programa Principal

# las funciones que no tienen retorno se ejecutan solamente poniendo su nombre
foo() # llamada == call == ejecución

# las funciones con return, o bien se pueden printear o bien se pueden asignar
print(bar()) # el valor de retorno vuelve en el nombre de la función
valorDeBar = bar() # lo que retorna se almacena en la variable
print(valorDeBar) # imprime lo mismo
n = 98
bar() # si solo pongo el nombre es equivalente a poner una variable sola
n # como en este caso
print(masLarga())

""" 
def saludo():
    print('Hola persona')

saludo()
saludo()
"""

def saludo(nombre, edad): # nombre es un parámetro
    print(f'Hola {nombre}, tenés {edad} años')

# los argumentos que se envían deben cumplir:
# 1) misma cantidad, 2) en orden 3) mismo tipo de dato
saludo('Ana', 22) # 'Ana' es un argumento, que entra en la función y allí se comporta como nombre
saludo('Juan', 33) # debo enviar la misma cantidad de argumentos que la cantidad de parámetros
n = 'Quico'
e = 11
saludo(n, e)

def suma(n1, n2):
    return n1 + n2

print(suma(2, 1))
print(suma(3, 11))













