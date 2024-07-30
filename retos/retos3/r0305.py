grupos = ['A', 'B', 'AB', 'O']
tipos = ['+', '-']

def construirPares(): # todas las combinaciones
    pares = []
    for donante in grupos:
        for tipoDonante in tipos:
            donanteCompleto = donante + tipoDonante
            for receptor in grupos:
                for tipoReceptor in tipos:
                    receptorCompleto = receptor + tipoReceptor
                    pares.append((donanteCompleto, receptorCompleto))
    return pares

def compatibilidad(t):
    dg = t[0][:-1]
    df = t[0][-1]
    rg = t[1][:-1]
    rf = t[1][-1]
    print(t, end=' : ')
    if df == '+' and rf == '-':
        print('no', end=' / ')
    else: # me quedo solamente con los grupos
        if dg == '0' or dg in rg:
            print('si', end=' / ')
        else:
            print('no', end=' / ')

for par in construirPares():
    compatibilidad(par)

