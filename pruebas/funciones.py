""" def foo(): # declaración de la función
    print('Soy foo')

def bar():
    return "lo que vuelve" # retorna valores al programa principal

# Programa Principal
foo() # call == llamada == ejecución

print(bar()) # al tener return DEBE ser o bien printeada, o bien asignada

def suma():
    a = 3
    b = 2
    s = a + b
    return s

miSuma = suma()
print(miSuma)

def resta():
    return 2 - 3

print(resta())

def raya():
    print('-------------------------')

raya()

"""

""" def saludoSimple():
    print('Hola persona')

saludoSimple()
print('algo al medio')
saludoSimple() # reutilización

def saludo(nombre): # nombre es un parámetro
    print('Hola', nombre)

saludo('Ana') # 'Ana' es un argumento
n = input('Ingrese su nombre: ')
saludo(n)
"""
""" 
def saludo(nombre, edad): # redefino con dos parámetros
    print(f'Hola {nombre}, tenés {edad} años')

# saludo('Pipo') esto da error porque requiere dos argumentos
saludo('Lisa', 33)
n = input('Nombre: ')
e = int(input('Edad: '))
saludo(n, e)
"""

""" 
# Ejemplo incorrecto
num3 = 11 # variable global: existe en el programa principal
def suma(n1, n2): # super incorrecto!!!!!!!
    # estoy usando una variable global num3 aqui !!!!!!!!
    sumita = n1 + n2 + num3 # variable local: s solamente existe aquí dentro de la función
    return sumita
# print(sumita) esto da error porque sumita es local a suma
print(suma(3, 2))
"""

# Ejemplo correcto
num3 = 11

def suma(n1, n2, n3):
    # la función es autónoma: no necesita nada de afuera
    # solamente usa variables locales y sus parámetros
    sumita = n1 + n2 + n3
    return sumita

print(suma(3, 2, num3)) # uso correcto de llamada al pasarle num3 como argumento


















