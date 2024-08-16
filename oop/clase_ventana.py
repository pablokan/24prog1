class Ventana:
    def __init__(self, posicion, estado='cerrada') -> None:
        self.posicion = posicion
        self.estado = estado

    def abrir(self):
        if self.estado == 'abierta':
            print(f'La ventana {self.posicion} ya está abierta')
        else:
            print(f'Abro ventana {self.posicion}')
            self.estado = 'abierta'

    def cerrar(self):
        if self.estado == 'cerrada':
            print(f'La ventana {self.posicion} ya está cerrada')
        else:
            print(f'Cierro ventana {self.posicion}')
            self.estado = 'cerrada'
