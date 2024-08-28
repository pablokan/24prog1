# un ejemplo mínimo de herencia y composición
class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

class Alumno(Persona): # hija de Persona(Herencia) y parte o secundaria o componente de Escuela (Composición)
    def __init__(self, nombre, promedio) -> None:
        super().__init__(nombre)
        self.promedio = promedio

class Escuela:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.alumnos = []
        hayMas = 's'
        print(f'Carga de Alumnos de la escuela {nombre}')
        while hayMas == 's':
            n = input('Nombre del Alumno: ')
            p = float(input('Promedio del alumno: '))
            alumno = Alumno(n, p)
            self.alumnos.append(alumno)
            hayMas = input('Hay más alumnos para cargar? (s/n): ')

    def mostrarAlumnos(self):
        print(f'Listado completo de alumnos de la escuela {self.nombre}')
        for a in self.alumnos:
            print(f'El estudiante {a.nombre} tiene un promedio de {a.promedio}')

escuelaSarmiento = Escuela('Sarmiento')
escuelaBelgrano = Escuela('Manuel Belgrano')
escuelaSarmiento.mostrarAlumnos()
escuelaBelgrano.mostrarAlumnos()
