nombreDias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

totalLluviaCaida = 0
diaMasLluvioso = ''
masLluviaXdia = 0
for dia in nombreDias:
    mensaje = 'Ingrese lluvia caída el día ' + dia + ': '
    mm = int(input(mensaje))
    totalLluviaCaida += mm
    if mm > masLluviaXdia:
        masLluviaXdia = mm
        diaMasLluvioso = dia

print('El total de lluvia caída fue:', totalLluviaCaida, 'mm.')
print('Y el día más lluvioso fue el', diaMasLluvioso)
