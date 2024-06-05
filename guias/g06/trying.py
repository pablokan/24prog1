
def inputInt(mensaje):
    validado = False
    while not validado: # validado == False
        n = input(mensaje)
        try:
            n = int(n) # puede producir la interrupción de la ejecución
            validado = True # esta línea solamente se ejecuta cuando la conversión funciona
        except:
            print('no se pudo realizar la conversión a entero')
    return n

num1 = inputInt('Ingrese primer valor entero: ')
num2 = inputInt('Ingrese segundo valor entero: ')
print(f'La suma es {num1 + num2}')


