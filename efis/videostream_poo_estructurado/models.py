class Contenido:
    def __init__(self, id, titulo, genero, ano, director, protagonista, tipo_contenido):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.director = director
        self.protagonista = protagonista
        self.tipo_contenido = tipo_contenido

class Usuario:
    def __init__(self, id, nombre, dni, email, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

class Alquiler:
    def __init__(self, id, usuario_id, contenido_id, dias, fecha_alquiler, fecha_devolucion, total_importe):
        self.id = id
        self.usuario_id = usuario_id
        self.contenido_id = contenido_id
        self.dias = dias
        self.fecha_alquiler = fecha_alquiler
        self.fecha_devolucion = fecha_devolucion
        self.total_importe = total_importe
        self.alquilado = True
