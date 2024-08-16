class Alumno(): # clase secundaria que se compondrá dentro de la principal
    def __init__(self, n, p) -> None:
        self.nombre = n
        self.promedio = p

class Instituto(): # clase principal
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.alumnos = []
        hayMas = 's'
        while hayMas == 's':
            self.agregarAlumno()
            hayMas = input('Hay más alumnos para cargar? (s/n: )')

    def agregarAlumno(self):
        nom = input('Nombre del alumno: ')
        pro = float(input('Promedio del alumno: '))
        alu = Alumno(nom, pro) # Composición: creación de un objeto de la clase secundaria dentro de la clase principal
        self.alumnos.append(alu)

    def listarAlumnos(self):
        for a in self.alumnos:
            print(f'{a.nombre} tiene un promedio de {a.promedio}')

instituto = Instituto('iTec')
instituto.listarAlumnos()
instituto.agregarAlumno()
instituto.listarAlumnos()


