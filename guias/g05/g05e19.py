
def recu(palabra):
    esi = '\u2554'
    esd = '\u2557'
    eii = '\u255A'
    eid = '\u255D'
    rh= '\u2550'
    rv = '\u2551'

    print(esi, end='')
    for x in range(len(palabra)+2):
        print(rh, end='')
    print(esd)
    print(rv, end='')
    print(' ', end='')
    print(palabra, end='')
    print(' ', end='')
    print(rv)
    print(eii, end='')
    for x in range(len(palabra)+2):
        print(rh, end='')
    print(eid)

resp = ''
while resp != 'n':
    p = input('Ingresa palabra o frase a recuadrar: ')
    recu(p)
    resp = input('"n" para terminar ')
