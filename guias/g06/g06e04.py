def inputStr(msg, mini=0, maxi=10**38):
    validado = False
    if mini != 0 and maxi != 10**38:
            msg += f' (entre {mini} y {maxi} caracteres): '
    elif mini != 0:
            msg += f' (al menos {mini} caracteres): '
    elif maxi != 10**38:
            msg += f' (a lo sumo {maxi} caracteres): '
    else:
        msg += ': '
        
    while not validado:
        s = input(msg)
        if mini <= len(s) <= maxi:
            validado = True
        else:
            print('Entrada incorrecta')
    return s

if __name__ == '__main__':
    password0 = inputStr('Password', 5, 8)
    password1 = inputStr('Password', 4)
    password2 = inputStr('Password', maxi=5)
    password3 = inputStr('Password')

