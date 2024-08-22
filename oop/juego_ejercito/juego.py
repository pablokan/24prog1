from ejercito import Ejercito

class Juego:
    def __init__(self):
        self.esparta = Ejercito('Esparta', 3, 1, 0)
        self.persia = Ejercito('Persia', 1, 0, 1)

    def estado(self, ejercito: Ejercito):
        print()
        print(f'{ejercito.nombre}:', end=' - ')
        for k, v in ejercito.soldados.items():
            print(f'{k}: Salud={v.salud if v.salud>0 else 'muerto'}', end=' - ')

    def accion(self):        
        self.estado(self.esparta)
        self.estado(self.persia)
        self.persia.soldados['Sol1'].atacar(self.esparta.soldados['Sol3'])
        self.persia.soldados['Sol1'].atacar(self.esparta.soldados['Sol3'])
        self.estado(self.esparta)
        self.esparta.doctores['Doc1'].curar(self.esparta)
        self.estado(self.esparta)
        self.persia.monstruos['Mon1'].atacar(self.esparta.soldados['Sol2'])
        self.estado(self.esparta)
