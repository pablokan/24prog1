class Alumno(): # clase secundaria que va a componer a la clase principal
    def __init__(self, n, p) -> None:
        self.nombre = n
        self.promedio = p


class Instituto(): # clase principal que contendrá objetos de la clase secundaria
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.alumnos = []
        hayMas = 's'
        while hayMas == 's':
            self.carga()
            hayMas = input('Hay más alumnos para cargar? (s/n): ')

    def agregarAlumno(self):
        print()
        self.carga()

    def carga(self):
        nom = input('Nombre del alumno: ')
        pro = float(input('Promedio del alumno: '))
        alu = Alumno(nom, pro) # composición
        self.alumnos.append(alu)
    
    
    def listarAlumnos(self):
        print()
        for alumno in self.alumnos:
            print(f'{alumno.nombre} tiene un promedio de {alumno.promedio}')

instituto = Instituto('iTec')
instituto.listarAlumnos()
instituto.agregarAlumno()
instituto.listarAlumnos()
