# Definimos una clase base Musico
class Musico:
    def __init__(self, nombre, albumes, reproducciones):
        self.nombre = nombre
        self.albumes = albumes
        self.reproducciones = reproducciones

# Definimos una clase Solista que hereda de Musico
class Solista(Musico):
    def __init__(self, nombre, albumes, reproducciones, edad):
        super().__init__(nombre, albumes, reproducciones)
        self.edad = edad

# Definimos una clase Banda que hereda de Musico
class Banda(Musico):
    def __init__(self, nombre, albumes, reproducciones, integrantes):
        super().__init__(nombre, albumes, reproducciones)
        self.integrantes = integrantes

    def obtener_cantantes(self):
        cantantes = []
        for integrante in self.integrantes:
            if "(voz)" in integrante:
                cantantes.append(integrante.split(" (voz)")[0])
        return cantantes

# Creamos las listas iniciales
bandas = [
    ["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
    ["Rage Against the Machine", 4, 243490, "Zack de la Rocha (voz), Tom Morello, Tim Commerford"],
    ["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
]
solistas = [
    ["Peter Gabriel", 10, 17319533, 70],
    ["Jeff Beck", 3, 1023998, 76]
]

# Instanciamos los objetos de bandas y solistas
lista_bandas = [Banda(nombre, albumes, reproducciones, integrantes.split(', ')) for nombre, albumes, reproducciones, integrantes in bandas]
lista_solistas = [Solista(nombre, albumes, reproducciones, edad) for nombre, albumes, reproducciones, edad in solistas]

# Método para obtener el total de reproducciones
def total_reproducciones(bandas, solistas):
    return sum(banda.reproducciones for banda in bandas) + sum(solista.reproducciones for solista in solistas)

# Método para obtener el solista más viejo
def solista_mas_viejo(solistas):
    return max(solistas, key=lambda solista: solista.edad).nombre

# Método para obtener los nombres de los cantantes de las bandas
def cantantes_bandas(bandas):
    cantantes = []
    for banda in bandas:
        cantantes.extend(banda.obtener_cantantes())
    return cantantes

# Método para obtener el nombre del artista (banda o solista) con más álbumes
def mayor_cantidad_albumes(bandas, solistas):
    mayor = max(bandas + solistas, key=lambda musico: musico.albumes)
    return mayor.nombre

# Salida esperada
print(f"Total de reproducciones del sitio: {total_reproducciones(lista_bandas, lista_solistas)}")
print(f"El solista más viejo es: {solista_mas_viejo(lista_solistas)}")
print("Los nombres de los cantantes de las bandas son:")
for cantante in cantantes_bandas(lista_bandas):
    print(cantante)
print(f"El nombre de la banda o el solista con mayor cantidad de álbumes es: {mayor_cantidad_albumes(lista_bandas, lista_solistas)}")
