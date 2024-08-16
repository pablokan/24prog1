from clase_puerta import Puerta
class Coche():
    def __init__(self) -> None:
        self.puertaIzquierda  = Puerta('izquierda')
        self.puertaDerecha  = Puerta('derecha')

    def estadoCoche(self):
        print('Puertas:', end=' ')
        print(self.puertaIzquierda.posicion, 
              self.puertaIzquierda.estado,
              ' - ',
              self.puertaDerecha.posicion, 
              self.puertaDerecha.estado,
              end=' / ')
        print('Ventanas:', end=' ')
        print(
              self.puertaIzquierda.ventana.posicion,
              self.puertaIzquierda.ventana.estado,
              ' - ',
              self.puertaDerecha.ventana.posicion,
              self.puertaDerecha.ventana.estado)
