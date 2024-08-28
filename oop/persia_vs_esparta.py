# Vinculación entre las clases, comprobamos construyendo frases con los verbos
# SER (Herencia): Soldado ES Personaje
# TENER (Composición): Ejército TIENE Soldados

class Personaje:
    def __init__(self, nombre, salud) -> None:
        self.nombre = nombre
        self.salud = salud

class Soldado(Personaje):
    def __init__(self, nombre, salud, fuerza) -> None:
        super().__init__(nombre, salud)
        self.fuerza = fuerza

    def atacar(self, rival):
        rival.salud -= 20

class Doctor(Personaje):
    def __init__(self, nombre, salud, curacion) -> None:
        super().__init__(nombre, salud)
        self.curacion = curacion

    def curar(self, aliado):
        aliado.salud += 15
        self.curacion -= 15
        if aliado.salud > 100:
            aliado.salud = 100

class Monstruo(Personaje):
    pass

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
        # Construyo una lista de soldados
        self.nombre = nombre
        self.soldados = []
        for i in range(cS):
            s = Soldado(f'Sol{i+1}', 100, 100)
            self.soldados.append(s)
        
        # Construyo una lista de doctores, similar a la de soldados, 
        # pero en una sola línea usando el recurso de lista por comprensión
        self.doctores = [Doctor(f'Doc{i+1}', 50, 80) for i in range(cD)]

        # Falta la lista self.monstruos

class Juego:
    def __init__(self) -> None:
        self.esparta = Ejercito('Esparta', 3, 1, 0)
        self.persia = Ejercito('Persia', 1, 0, 1)

    def estado(self, ejercito):
        print()
        print(ejercito.nombre, end=' - ')
        for s in ejercito.soldados:
            print(f'{s.nombre} - Salud:{s.salud}', end=' - ')
            for d in ejercito.doctores:
                print(f'{d.nombre} - Puntos de curación:{d.curacion}', end=' - ')

    def accion(self):
        self.estado(self.esparta)
        self.estado(self.persia)
        self.persia.soldados[0].atacar(self.esparta.soldados[0])
        self.persia.soldados[0].atacar(self.esparta.soldados[0])
        self.estado(self.esparta)
        self.esparta.doctores[0].curar(self.esparta.soldados[0])
        self.estado(self.esparta)

j = Juego()
j.accion()

