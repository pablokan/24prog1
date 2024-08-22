class Personaje:
    def __init__(self, nombre: str, salud: int):
        self.nombre = nombre
        self.salud = salud

class Soldado(Personaje):
    def __init__(self, nombre: str, salud: int, fuerza: int):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self, rival: Personaje):
        rival.salud -= 20

class Doctor(Personaje):
    def __init__(self, nombre: str, salud: int, curacion: int):
        super().__init__(nombre, salud)
        self.curacion = curacion

    def curar(self, ejercito: Ejercito):
        pass        
        

class Monstruo(Personaje):
    def __init__(self, nombre: str, salud: int, poder: str):
        super().__init__(nombre, salud)
        self.poder = poder

    def atacar(self, rival: Personaje):
        if self.poder == 'fuego':
            rival.salud = 0


class Ejercito:
    def __init__(self, nombre: str, cS: int, cD: int, cM: int) -> None:
        """
        Construye un ejército
            Parámetros:
                nombre del ejército
                cantidad de soldados
                cantidad de doctores
                cantidad de monstruos
        """
        self.nombre = nombre
        self.soldados = {f'Sol{i+1}': Soldado(f'Sol{i+1}', 100, 100) for i in range(cS)}
        self.doctores = {f'Doc{i+1}': Doctor(f'Doc{i+1}', 50, 80) for i in range(cD)}
        self.monstruos = {f'Mon{i+1}': Monstruo(f'Mon{i+1}', 200, 'fuego') for i in range(cM)}


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
        self.persia.soldados['Sol1'].atacar(self.esparta.soldados['Sol1'])
        self.persia.soldados['Sol1'].atacar(self.esparta.soldados['Sol1'])
        self.estado(self.esparta)
        self.esparta.doctores['Doc1'].curar(self.esparta.soldados['Sol1'])
        self.estado(self.esparta)
        self.persia.monstruos['Mon1'].atacar(self.esparta.soldados['Sol2'])
        self.estado(self.esparta)

j = Juego()
j.accion()


