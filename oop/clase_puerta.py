from clase_ventana import Ventana

class Puerta():
    def __init__(self, posicion, estado='cerrada') -> None:
        self.posicion = posicion
        self.estado = estado
        self.ventana = Ventana(posicion, estado)

    def abrir(self):
        if self.estado == 'abierta':
            print(f'La puerta {self.posicion} ya está abierta')
        else:
            print(f'Abro puerta {self.posicion}')
            self.estado = 'abierta'

    def cerrar(self):
        if self.estado == 'cerrada':
            print(f'La puerta {self.posicion} ya está cerrada')
        else:
            print(f'Cierro puerta {self.posicion}')
            self.estado = 'cerrada'


