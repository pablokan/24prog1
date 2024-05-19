#19:40 - 19:44
datos = 'Juan$120000,Ana$250000,Luis$76500,Vilma$98700'
lista = datos.split(',')
l1 , l2 = [], []
for e in lista:
    n, s = e.split('$')
    l1.append(n)
    l2.append(int(s))
print(l1, l2)

# 19:45 - 19:46
mujeres = ['Lisa', 'Ema', 'Juana', 'Ester']
varones = ['Eduardo', 'Pedro']
inicial = 'E'
lista = mujeres + varones
s = ''
for e in lista:
    if e[0] == inicial:
        s += e + '-'
s = s[:-1]
print(s)

# 19:47
direcciones = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']

nombres = []
for calle in direcciones:
    posiEspacio = calle.rfind(' ')
    nombre = calle[:posiEspacio]
    nombres.append(nombre)
print(nombres)

#q = [(calle, cantidad) for calle in nombres]
