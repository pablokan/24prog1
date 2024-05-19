# start: 14:15
from random import randint

pista1 = '🏁____🌲__________________🌲__🌲___🚙'
#pista1 = '🏁________🚙'
#print(f'######## {len(pista1)=} #########')
azulPos = len(pista1) - 1
print(f'######## {pista1=} #########')
while azulPos > 0:
#    print(f'######## {azulPos=} #########')
    avance = randint(1, 3)
    print(f'######## {avance=} #########')
    azulPos -= avance
    pista1 = pista1.replace('🚙', '_')
    
    if azulPos < 0:
        azulPos = 0
    pistaRestante = pista1[:azulPos]
    if pista1[azulPos] == '🌲':
        pistaRecorrida = '🌲' + pistaRecorrida
    print(f'######## {pistaRestante=} #########')

    pistaRecorrida = pista1[azulPos+1:]
#    print(f'######## {pistaRecorrida=} #########')

    #    print(f'######## {pista1=} #########')
    pista1 = pistaRestante + '🚙' + pistaRecorrida
    print(f'######## {pista1=} #########')
    if azulPos == 0:
        print('🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁🏁')





# pista2 = ' 🏁_🌲_🌲___🌲______________________🚗'
