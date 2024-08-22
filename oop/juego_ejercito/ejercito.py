from soldado import Soldado
from doctor import Doctor
from monstruo import Monstruo

class Ejercito:
    def __init__(self, nombre: str, cS: int, cD: int, cM: int) -> None:
        self.nombre = nombre
        self.soldados = {f'Sol{i+1}': Soldado(f'Sol{i+1}', 100, 100) for i in range(cS)}
        self.doctores = {f'Doc{i+1}': Doctor(f'Doc{i+1}', 50, 80) for i in range(cD)}
        self.monstruos = {f'Mon{i+1}': Monstruo(f'Mon{i+1}', 200, 'fuego') for i in range(cM)}
