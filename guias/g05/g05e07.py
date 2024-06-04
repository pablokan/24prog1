def carga():
    nombres, sexos = [], []
    for x in range(2):
        nombre = input('Nombre: ')
        sexo = input('Sexo: ')
        nombres.append(nombre)
        sexos.append(sexo)
    return nombres, sexos

ns, ss = carga()

def mostrarMujeres(nombres, sexos):
    for i in range(len(sexos)):
        if sexos[i] == 'f':
            print(nombres[i])

mostrarMujeres(ns, ss)
