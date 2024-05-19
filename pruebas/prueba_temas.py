








from datetime import date
from devtools import debug
hoy = date.today()
print(hoy)
debug(hoy)

def foo(par) -> str: 
    if par >= 87 and True:
        return "hola"
    elif par == [(1,'hi')]:
        variable = 'variable'
   
# comment
n, s = 91, "hola"
li = [[3, "chau", True, None, (2, 3), int], 1]
di = {"name": "John"}
f = foo(n)

for x in range(len(li)):
    print(li[x])

from dataclasses import dataclass

class Animal:
    def __init__(self) -> None:
        pass

@dataclass
class Persona:
    name: str
    age: int

    def saludo(self):
        print(f"Hola {self.name}, tenés {self.age} años")

    def __str__(self) -> str:
        return f"{self.name} tiene {self.age} años"

abecedario = "abcdefghijklmnopqrstuvwxyz"

ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("oO08 iIlL1 g9qCGQ ~-+=>")
# â é ù ï ø ç Ã Ē Æ œ

p = Persona("Paul", 57)
p.saludo()
print(p)
print(f"\N{Sauropod}")

'''
1) palabras reservadas
2) funciones
    2.1) del lenguaje
    2.2) declaración
    2.3) uso de propias
3) parámetros
4) variables
5) strings literales
6) números
7) comentarios
8) operadores
9) tipos de datos
10) decoradores
11) clases
'''

@dataclass
class Clase:
    pass
def funcionMia(param1, param2):
    lista = [1, 'hola']
    print(lista) #comment
    for i in lista:
        lista >= str and False 
funcionMia()


