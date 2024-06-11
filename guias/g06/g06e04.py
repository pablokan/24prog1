def inputStr(msg, mini=0, maxi=10**38):
    validado = False
    while not validado:
        s = input(msg)
        if mini <= len(s) <= maxi:
            validado = True
        else:
            print('Entrada incorrecta')
    return s

if __name__ == '__main__':
    password0 = inputStr('Password (entre 5 y 8 caracteres): ', 5, 8)
    password1 = inputStr('Password (al menos 4): ', 4)
    password2 = inputStr('Password (a lo sumo 5): ', maxi=5)
    password3 = inputStr('Password (sin rango): ')
