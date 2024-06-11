from g06e04 import inputStr

def inputUser(msg):
    validado = False
    while not validado:
        s = inputStr(msg, 8).lower()
        intersCarEsp = len(set(s).intersection(set('#$%&')))
        intersDigitos = len(set(s).intersection(set('1234567890')))
        letras = {chr(x) for x in range(97, 123)}.union(set('áéíóúñ'))
        intersLetras = len(set(s).intersection(letras))
        if  intersCarEsp > 0 and intersDigitos > 0 and intersLetras > 0: 
            validado = True
    return s

usuario = inputUser('Ingrese un nombre de usuario válido (debe contener una letra, un dígito y al menos uno de estos caracteres especiales:  #, $, %,&)')
print(usuario)
