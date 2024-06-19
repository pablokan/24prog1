def edad(fNac):
    from datetime import date
    hoy = date.today()
    dH, mH, aH  = hoy.day, hoy.month, hoy.year
    dN, mN, aN = [int(n) for n in fNac.split('-')]
    e = aH - aN
    if (mN > mH) or (mN == mH and dN > dH):
        e -= 1
    return e

#print(edad('3-6-1965'))


