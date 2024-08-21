class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

class Soldado(Personaje):
    def __init__(self, nombre, salud, fuerza):
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self, rival):
        rival.salud -= 20

class Doctor(Personaje):
    def __init__(self, nombre, salud, curacion):
        super().__init__(nombre, salud)
        self.curacion = curacion

    def curar(self, aliado):
        aliado.salud += 15
        self.curacion -= 15
        if aliado.salud > 100:
            aliado.salud = 100

class Monstruo(Personaje):
    def __init__(self, nombre, salud, poder):
        super().__init__(nombre, salud)
        self.poder = poder

    def atacar(self, rival):
        if self.poder == 'fuego':
            rival.salud = 0


class Ejercito:
    def __init__(self, nombre, cS, cD, cM) -> None:
        """
        Construye un ejército
            Parámetros:
                nombre del ejército
                cantidad de soldados
                cantidad de doctores
                cantidad de monstruos
        """
        self.nombre = nombre
        self.soldados = [Soldado(f'Sol{i+1}', 100, 100) for i in range(cS)]
        self.doctores = [Doctor(f'Doc{i+1}', 50, 80) for i in range(cD)]
        self.monstruos = [Monstruo(f'Mon{i+1}', 200, 'fuego') for i in range(cM)]


class Juego:
    def __init__(self):
        self.esparta = Ejercito('Esparta', 3, 1, 0)
        self.persia = Ejercito('Persia', 1, 0, 1)

    def estado(self, ejercito):
        print()
        print(f'{ejercito.nombre}:', end=' - ')
        for soldado in ejercito.soldados:
            print(f'{soldado.nombre}: Salud={soldado.salud if soldado.salud>0 else 'muerto'}', end=' - ')
        

j = Juego()
j.estado(j.esparta)
j.estado(j.persia)
s = Soldado('Juan', 300, 300)
j.esparta.soldados.append(s)
j.persia.soldados[0].atacar(j.esparta.soldados[0])
j.persia.soldados[0].atacar(j.esparta.soldados[0])
j.estado(j.esparta)
j.esparta.doctores[0].curar(j.esparta.soldados[0])
j.estado(j.esparta)
j.persia.monstruos[0].atacar(j.esparta.soldados[1])
j.estado(j.esparta)

