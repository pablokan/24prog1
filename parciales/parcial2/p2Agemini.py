class Musico:
    def __init__(self, nombre, cantidad_albumes, reproducciones):
        self.nombre = nombre
        self.cantidad_albumes = cantidad_albumes
        self.reproducciones = reproducciones

    def __str__(self):
        return f"Nombre: {self.nombre}, Álbumes: {self.cantidad_albumes}, Reproducciones: {self.reproducciones}"


class Banda(Musico):
    def __init__(self, nombre, cantidad_albumes, reproducciones, integrantes):
        super().__init__(nombre, cantidad_albumes, reproducciones)
        self.integrantes = integrantes

    def get_cantantes(self):
        cantantes = []
        for integrante in self.integrantes.split(','):
            if "(voz)" in integrante:
                cantantes.append(integrante.replace("(voz)", "").strip())
        return cantantes


class Solista(Musico):
    def __init__(self, nombre, cantidad_albumes, reproducciones, edad):
        super().__init__(nombre, cantidad_albumes, reproducciones)
        self.edad = edad


# Datos iniciales para la instanciación
bandas_data = [
    ["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
    ["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
    ["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas_data = [
    ["Peter Gabriel", 10, 17_319_533, 70],
    ["Jeff Beck", 3, 1_023_998, 76]
]


# Creación de objetos Banda y Solista
bandas = []
for banda in bandas_data:
    bandas.append(Banda(banda[0], banda[1], banda[2], banda[3]))

solistas = []
for solista in solistas_data:
    solistas.append(Solista(solista[0], solista[1], solista[2], solista[3]))


def total_reproducciones(musicos):
    total = 0
    for musico in musicos:
        total += musico.reproducciones
    return total


def solista_mas_viejo(solistas):
    solista_mas_viejo = solistas[0]
    for solista in solistas:
        if solista.edad > solista_mas_viejo.edad:
            solista_mas_viejo = solista
    return solista_mas_viejo.nombre


def cantantes_bandas(bandas):
    cantantes = []
    for banda in bandas:
        cantantes.extend(banda.get_cantantes())
    return ", ".join(cantantes).replace("y ", "y")


def musico_mas_albumes(musicos):
    musico_mas_albumes = musicos[0]
    for musico in musicos:
        if musico.cantidad_albumes > musico_mas_albumes.cantidad_albumes:
            musico_mas_albumes = musico
    return musico_mas_albumes.nombre


# Resultados
todos_los_musicos = bandas + solistas
total_reproducciones_final = total_reproducciones(todos_los_musicos)
solista_mas_viejo_final = solista_mas_viejo(solistas)
cantantes_bandas_final = cantantes_bandas(bandas)
musico_mas_albumes_final = musico_mas_albumes(todos_los_musicos)


print(f"Total de reproducciones del sitio: {total_reproducciones_final}")
print(f"El solista más viejo es: {solista_mas_viejo_final}")
print(f"Los nombres de los cantantes de las bandas son:\n{cantantes_bandas_final}")
print(f"El nombre de la banda o el solista con mayor cantidad de álbumes es:\n{musico_mas_albumes_final}")