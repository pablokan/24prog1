n = '123456789'
nConPuntos = ''
for i in range(len(n)):
   digito = n[(i+1)*-1] 
   nConPuntos = digito + nConPuntos
   if ((i+1) % 3 == 0) and i < len(n)-1:
      nConPuntos = '.'+ nConPuntos
print(nConPuntos)

