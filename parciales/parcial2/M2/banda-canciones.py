class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
    
    def modificar_duracion(self, nueva_duracion):
        print(f"Cambio de duración de {self.nombre}:")
        self.duracion = nueva_duracion
    
    def __str__(self):
        return f"Cancion: nombre='{self.nombre}', duracion={self.duracion} segundos"

class Banda:
    def __init__(self, nombre, canciones):
        self.nombre = nombre
        self.canciones = [Cancion(nombre, duracion) for nombre, duracion in canciones]
    
    def mostrar_canciones(self):
        for cancion in self.canciones:
            print(cancion)
    
    def modificar_duracion_cancion(self, nombre_cancion, nueva_duracion):
        for cancion in self.canciones:
            if cancion.nombre == nombre_cancion:
                cancion.modificar_duracion(nueva_duracion)
                print(cancion)
                return
        print(f"No se encontró la canción '{nombre_cancion}'")

# Datos de entrada
nombre_banda = "Led Zeppelin"
lista_canciones = [("The rain song", 452), ("Black dog", 296), ("Kashmir", 512)]

# Crear la banda y mostrar canciones
banda = Banda(nombre_banda, lista_canciones)
banda.mostrar_canciones()

# Modificar la duración de una canción
banda.modificar_duracion_cancion("Black dog", 321)

# Mostrar la última canción para completar la salida esperada
print(banda.canciones[-1])
