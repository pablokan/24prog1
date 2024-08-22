from personaje import Personaje
from typing import TYPE_CHECKING

class Doctor(Personaje):
    def __init__(self, nombre: str, salud: int, curacion: int):
        super().__init__(nombre, salud)
        self.curacion = curacion

    def curar(self, ejercito: 'Ejercito'):
        if TYPE_CHECKING:
            from ejercito import Ejercito

        # Encontrar al soldado con la salud mínima
        soldadoMinimaSalud = None
        minimaSalud = float('inf')  # Inicializar con un valor infinito

        for soldado in ejercito.soldados.values():
            if soldado.salud < minimaSalud and soldado.salud > 0:
                minimaSalud = soldado.salud
                soldadoMinimaSalud = soldado

        # Curar al soldado con la salud mínima
        if soldadoMinimaSalud:
            soldadoMinimaSalud.salud += 15
            self.curacion -= 15
            print(f"{self.nombre} curó a {soldadoMinimaSalud.nombre}. Salud actual: {soldadoMinimaSalud.salud}")
        else:
            print(f"{self.nombre} no encontró soldados heridos para curar.")

            
