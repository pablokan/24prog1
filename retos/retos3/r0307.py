def trunc(real, decimales):
    realStr = str(real)
    posPunto = realStr.find('.')
    if decimales == 0:
        return int(real)
    if posPunto != -1:
        return float(realStr[:posPunto] + '.' + realStr[posPunto+1:posPunto+decimales+1])
    else:
        return real

print(trunc(3.56, 0))    
print(trunc(3.156, 1))
print(trunc(3.156, 2))
