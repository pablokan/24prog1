# Se puede construir una frase relacionando clases y usando los verbos:
# Ser (para Herencia)
# Tener (para Composición)

class Personaje:
    def __init__(self, nombre, salud) -> None:
        self.nombre = nombre
        self.salud = salud

class Soldado(Personaje): # El Soldado ES un Personaje ---> hay Herencia
    def __init__(self, nombre, salud, fuerza) -> None:
        super().__init__(nombre, salud) # llamada al constructor de Personaje
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
        self.doctores = [Doctor(f'Doc{i+1}', 50, 80) for i in range(cS)]

class Juego:
    def __init__(self) -> None:
        self.esparta = Ejercito('Esparta', 3, 1, 0)
        self.persia = Ejercito('Persia', 1, 0, 1)

    def estado(self, ejercito):
        print()
        print(f'{ejercito.nombre}: ', end=' - ')
        for soldado in ejercito.soldados:
            print(f'{soldado.nombre} Salud:{soldado.salud}', end=' - ')

j = Juego()
j.estado(j.esparta)
j.estado(j.persia)
s = Soldado('Juan', 300, 500)
j.esparta.soldados.append(s)
j.persia.soldados[0].atacar(j.esparta.soldados[1])
j.persia.soldados[0].atacar(j.esparta.soldados[1])
j.estado(j.esparta)
j.esparta.doctores[0].curar(j.esparta.soldados[1])
j.estado(j.esparta)


