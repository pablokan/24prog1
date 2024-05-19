
import random
import time

PISTA_LONGITUD_MIN = 10
PISTA_LONGITUD_MAX = 20
NUM_ARBOLES_MIN = 1
NUM_ARBOLES_MAX = 3
COCHE1 = '🚙'
COCHE2 = '🚗'
META = '🏁'
ARBOL = '🌲'
CHOQUE = '💥'

def generar_pista():
    longitud = random.randint(PISTA_LONGITUD_MIN, PISTA_LONGITUD_MAX)
    pista = ['_'] * longitud
    num_arboles = random.randint(NUM_ARBOLES_MIN, NUM_ARBOLES_MAX)
    for _ in range(num_arboles):
        posicion_arbol = random.randint(0, longitud - 1)
        pista[posicion_arbol] = ARBOL
    return pista

def imprimir_pista(pista, coche_pos):
    pista_con_coches = pista[:]
    for i, pos in enumerate(coche_pos):
        pista_con_coches[pos] = f'{COCHE1 if i == 0 else COCHE2}'
    print(''.join(pista_con_coches))

def avanzar(coche_pos):
    for i in range(len(coche_pos)):
        avance = random.randint(1, 3)
        coche_pos[i] += avance
        if coche_pos[i] >= len(pista):
            coche_pos[i] = len(pista) - 1
        if pista[coche_pos[i]] == ARBOL:
            coche_pos[i] -= avance
            print(CHOQUE)
    return coche_pos

def carrera():
    pista = generar_pista()
    coche1_pos = [len(pista) - 1]
    coche2_pos = [len(pista) - 1]

    while True:
        imprimir_pista(pista, [coche1_pos[0], coche2_pos[0]])
        time.sleep(1)
        coche1_pos = avanzar(coche1_pos)
        coche2_pos = avanzar(coche2_pos)
        if coche1_pos[0] <= 0 and coche2_pos[0] <= 0:
            print("¡Empate!")
            break
        elif coche1_pos[0] <= 0:
            print("¡Coche 1 gana!")
            break
        elif coche2_pos[0] <= 0:
            print("¡Coche 2 gana!")
            break

carrera()
