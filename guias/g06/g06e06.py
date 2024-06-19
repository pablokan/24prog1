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

n = inputInt('Ingrese un entero', 3, 7)
m = inputInt('Cualquier número entero')
maxito = inputInt('ingrese un entero', maxi=999)
minito = inputInt('ingrese un entero', 1001)
