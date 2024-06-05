nombres = ["Ana", "Luis", "Juan", 'Lisa', 'Quico']
fecNac = ["23-05-2006", "31-12-1990", "01-12-2006", "23-01-2001", "23-01-2006"]

diaHoy = 20
mesHoy = 5
aniHoy = 2024
for x in range(len(nombres)):
    diaNac = int(fecNac[x][:2])
    mesNac = int(fecNac[x][3:5])
    aniNac = int(fecNac[x][-4:])
    edad = aniHoy - aniNac
    if (mesNac > mesHoy) or (mesNac == mesHoy and diaNac > diaHoy):
        edad -= 1
    if edad >= 18:
        print(nombres[x])

