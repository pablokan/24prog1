listaRomanos = ['MCMLXV', 'III', 'XLIV','MCDXXXIV', 'CDXXII', 'CMXXIV', 'MMMCCCLII', 'CCLXVII', 'MMMXLVIII', 'DCCCXLIV', 'MCLXXX', 'DCCCXXIX', 'MDCCCXLIV', 'MMCMXVII', 'MMXXVII', 'MCCCXII', 'DLX', 'MMMXLIX', 'DCLXXXII', 'MMCDXX', 'DCCCLXII', 'DCXCIV', 'MCMXXVI', 'CMXXI', 'MMCLX', 'MMCLXXXI', 'MCMXC', 'CLXXXVII', 'MMMDLXI', 'MCCCLXVI', 'MDCCCLII', 'MMMXXVIII', 'MDCCCXXIII']


def romanoAdecimal(romano):
    decimal = 0
    diccRomanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    listaRomano = list(romano)
    #print(listaRomano)
    listaDecimal = [diccRomanos[k] for k in listaRomano]
    #print(listaDecimal)
    i = 0
    while i < len(listaDecimal)-1:
        if listaDecimal[i+1] > listaDecimal[i]:
            decimal += listaDecimal[i+1] - listaDecimal[i]
            i += 2
        elif listaDecimal[i+1] <= listaDecimal[i]:
            decimal += listaDecimal[i]
            i += 1
    if i < len(listaRomano):
        decimal += listaDecimal[-1]
    return romano, decimal

for r in listaRomanos:
    print(romanoAdecimal(r), end=' - ')





