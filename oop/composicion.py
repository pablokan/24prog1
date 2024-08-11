# Composición es el proceso de creación de objetos de una clase secundaria dentro de una clase Principal

# Siempre se puede comprobar si existe esta relación construyendo una frase con el verbo 'tener'.

# Por ejemplo, en este caso, la Empresa 'tiene' Empleados

class Empleado: # compone Empresa (es parte de)
    def __init__(self, n) -> None:
        self.nombre = n

class Empresa: # clase principal (compuesta por)
    def __init__(self) -> None:
        self.listaEmpleados = []
        # instancio los objetos de la clase subordinada dentro de la clase Principal
        self.listaEmpleados.append(Empleado('Juan'))
        self.listaEmpleados.append(Empleado('Ana'))

empresa = Empresa()
for empleado in empresa.listaEmpleados:
    print(empleado.nombre)
