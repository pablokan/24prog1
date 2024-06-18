s = 'holahola'
print(set(s))
print(set('#$%&'))
conjuntoInterseccion = set(s).intersection(set('#$%&'))
print(conjuntoInterseccion)
longitudDelConjuntoInterseccion = len(set(s).intersection(set('#$%&')))
print(longitudDelConjuntoInterseccion)

s = 'hola#chau'
print(set(s))
print(set('#$%&'))
conjuntoInterseccion = set(s).intersection(set('#$%&'))
print(conjuntoInterseccion)
longitudDelConjuntoInterseccion = len(set(s).intersection(set('#$%&')))
print(longitudDelConjuntoInterseccion)

s1 = 'hola'
s2 = 'moni'
s3 = 'chau'

cU = (set(s1).union(set(s2))).union(set(s3))
print(cU)

