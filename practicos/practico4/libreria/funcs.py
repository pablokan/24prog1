def inputInt(mensaje, mini=-10**38, maxi=10**38):
    agregarAlMensaje = ''
    if mini != -10**38 and maxi != 10**38:
        agregarAlMensaje = f' entre {mini} y {maxi}'
    elif mini != -10**38:
        agregarAlMensaje = f' mayor o igual que {mini}'
    elif maxi != 10**38:
        agregarAlMensaje = f' menor o igual que {maxi}'
    mensaje += agregarAlMensaje + ': '
    validado = False
    while not validado: # validado == False
        n = input(mensaje)
        try:
            n = int(n)
            if mini <= n <= maxi:
                validado = True
            else:
                print('No cumple con el rango')
        except:
            print('Debe ingresar un entero')
    return n

def inputChoice(opciones, pregunta='Elija una opción'):
    opciones = opciones.split('/')
    pregunta = f'{pregunta} ({opciones}): '
    respuesta = ''
    while respuesta not in opciones:
        respuesta = input(pregunta)
    return respuesta

def inputChoiceMenu(opciones, pregunta='Elija una opción'):
    opciones = opciones.split('/')
    for i in range(len(opciones)):
        print(f'{i+1}) {opciones[i]}')
    opc = inputInt('Ingrese opción', 1, len(opciones))
    return opciones[opc-1]

def edad(fNac):
    from datetime import date
    hoy = date.today()
    dH, mH, aH  = hoy.day, hoy.month, hoy.year
    dN, mN, aN = [int(n) for n in fNac.split('-')]
    e = aH - aN
    if (mN > mH) or (mN == mH and dN > dH):
        e -= 1
    return e
