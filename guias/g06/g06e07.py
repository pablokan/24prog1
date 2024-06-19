from libreria.funcs import inputInt
def inputChoice(opciones, pregunta='Elija una opción'):
    opciones = opciones.split('/')
    pregunta = f'{pregunta} ({opciones}): '
    respuesta = ''
    while respuesta not in opciones:
        respuesta = input(pregunta)
    return respuesta

#r = inputChoice('hola/chau')

def inputChoiceMenu(opciones, pregunta='Elija una opción'):
    opciones = opciones.split('/')
    for i in range(len(opciones)):
        print(f'{i+1}) {opciones[i]}')
    opc = inputInt('Ingrese opción', 1, len(opciones))
    return opciones[opc-1]

print(inputChoiceMenu('Altas/Bajas/Modificaciones'))
