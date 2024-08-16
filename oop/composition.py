# Composición es cuando tengo una clase principal y una o mas clases secundarias que son parte de la clase principal.
# Se verifica con el verbo 'tener'
# La Empresa TIENE empleados

class Empleado(): # clase secundaria (o componente)
    def __init__(self, n, s) -> None:
        self.nombre = n
        self.sueldo = s

    def getSalary(self):
        return self.sueldo

class Empresa(): # clase principal
    def __init__(self) -> None:
        self.empleados = []
        e1 = Empleado('Ana', 100) # Composición
        e2 = Empleado('Luis', 40) 
        self.empleados.append(e1)
        self.empleados.append(e2)

empresa = Empresa()
for trabajador in empresa.empleados:
    print(f'{trabajador.nombre} gana {trabajador.getSalary()}')
