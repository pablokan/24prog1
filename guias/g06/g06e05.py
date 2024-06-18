from g06e04 import inputStr

def inputUser(msg):
    validado = False
    while not validado:
        s = inputStr(msg, 8)
        intersCarEsp = len(set(s).intersection(set('#$%&')))
        intersDigitos = len(set(s).intersection(set('1234567890')))
        letrasMinusculas = {chr(x) for x in range(97, 123)}.union(set('áéíóúñ'))
        letrasMayusculas = {chr(x) for x in range(65, 91)}.union(set('áéíóúñ'.upper()))
        intersLetrasMinusculas = len(set(s).intersection(letrasMinusculas))
        intersLetrasMayusculas = len(set(s).intersection(letrasMayusculas))
        if  intersCarEsp > 0 and intersDigitos > 0 and intersLetrasMinusculas > 0 and intersLetrasMayusculas > 0: 
            validado = True
        if intersCarEsp == 0:
            print('Debe contener al menos un caracter especial (#,$,%,&)')
        if intersDigitos == 0:
            print('Debe contener al menos un número')
        if intersLetrasMinusculas == 0:
            print('Debe contener al menos una letra minúscula')
        if intersLetrasMayusculas == 0:
            print('Debe contener al menos una letra mayúscula')
    return s

usuario = inputUser('Ingrese un nombre de usuario válido (debe contener una letra minúscula, una mayúscula, un dígito y al menos uno de estos caracteres especiales:  #, $, %,&)')
print(usuario)
