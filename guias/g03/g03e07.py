lista = ['hola', 'boca', 'mesa', 'tabla', 'boca', 'celda']
print('Lista original: ', lista)
eliminar = input('Ingrese elemento a eliminar: ')
cantidadAntes = len(lista)
while eliminar in lista:
    lista.remove(eliminar)
cantidadDespues = len(lista)
if cantidadAntes == cantidadDespues:
    print('El elemento no está')
else:
    print('Lista con el elemento eliminado: ', lista)