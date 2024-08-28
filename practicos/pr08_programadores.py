class Empleado:
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje) -> None:
        super().__init__(nombre, sueldo)
        self.lenguaje = lenguaje

    def asignarProyecto(self, proyecto):
        self.proyecto = proyecto

    def lenguajeYproyecto(self):
        return self.lenguaje, self.proyecto
    
class Empresa:
    def __init__(self, nombre, rubro) -> None:
        self.nombre = nombre
        self.rubro = rubro
        self.listaProyectos = ["Web Pollitos", "Sistema Gallina SRL"]
        self.listaLenguajes = ["Python", "JavaScript", "C#", "HTML & CSS"]
        self.listaProgramadores: list[Programador] = []

    def agEmp(self):
        leng = input('Qué lenguaje maneja el candidato a empleado: ')
        if leng not in self.listaLenguajes:
            print(f'No necesitamos programadores de {leng}. Los lenguajes requeridos son {self.listaLenguajes}')
        else: # es contratado
            nombre = input('Nombre: ')
            salario = 3_475_000 if leng == 'Python' else 615_000
            programador = Programador(nombre, salario, leng)
            print(*self.listaProyectos)
            numProyecto = int(input('Proyecto: '))
            programador.asignarProyecto(self.listaProyectos[numProyecto-1])
            self.listaProgramadores.append(programador)

    def mostrarTodo(self):
        print(f'Empresa: {self.nombre}. Rubro: {self.rubro}')
        print('Programadores')
        for p in self.listaProgramadores:
            le, pr = p.lenguajeYproyecto()
            print(f'{p.nombre}. Salario: {p.sueldo}. Sistema: {pr}. Lenguaje: {le}')


empresa = Empresa('iTecLabs', 'Software Development')
for _ in range(4): empresa.agEmp()
empresa.mostrarTodo()
