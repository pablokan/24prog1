# Ejercicio 1: Sistema Básico de Biblioteca
class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = False
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        if self.prestado:
            self.prestado = False
            return True
        return False

# Ejercicio 2: Gestión de Cuentas Bancarias
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            self.movimientos.append(f"Depósito: +{cantidad}")
            return True
        return False
    
    def retirar(self, cantidad):
        if cantidad > 0 and self.saldo >= cantidad:
            self.saldo -= cantidad
            self.movimientos.append(f"Retiro: -{cantidad}")
            return True
        return False

# Ejercicio 3: Sistema de Empleados con Herencia
class Empleado:
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base
    
    def calcular_salario(self):
        return self.salario_base

class Vendedor(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, comisiones):
        super().__init__(nombre, id_empleado, salario_base)
        self.comisiones = comisiones
    
    def calcular_salario(self):
        return self.salario_base + self.comisiones

# Ejercicio 4: Composición con Vehículos
class Motor:
    def __init__(self, tipo, cilindrada):
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.encendido = False
    
    def encender(self):
        self.encendido = True
    
    def apagar(self):
        self.encendido = False

class Coche:
    def __init__(self, marca, modelo, tipo_motor, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor, cilindrada)
    
    def arrancar(self):
        self.motor.encender()
        return "Coche arrancado"

# Ejercicio 5: Sistema de Formas Geométricas
class Forma:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        pass
    
    def perimetro(self):
        pass

class Rectangulo(Forma):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

# Ejercicio 6: Sistema de Registro Escolar
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.calificaciones = {}
    
    def agregar_calificacion(self, materia, nota):
        if 0 <= nota <= 10:
            self.calificaciones[materia] = nota
            return True
        return False
    
    def promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

# Ejercicio 7: Sistema de Tienda Online
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def actualizar_stock(self, cantidad):
        if self.stock + cantidad >= 0:
            self.stock += cantidad
            return True
        return False

class Carrito:
    def __init__(self):
        self.items = {}
    
    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            if producto in self.items:
                self.items[producto] += cantidad
            else:
                self.items[producto] = cantidad
            producto.actualizar_stock(-cantidad)
            return True
        return False
    
    def total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.items.items())

# Ejercicio 8: Sistema de Tareas
class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
        self.fecha_creacion = None
        self.fecha_completado = None
    
    def completar(self):
        from datetime import datetime
        if not self.completada:
            self.completada = True
            self.fecha_completado = datetime.now()
            return True
        return False

class ListaTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def tareas_pendientes(self):
        return [tarea for tarea in self.tareas if not tarea.completada]

# Ejercicio 9: Sistema de Reservas
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
    
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def habitaciones_disponibles(self):
        return [hab for hab in self.habitaciones if not hab.reservada]
    
    def reservar_habitacion(self, numero_habitacion):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and not habitacion.reservada:
                habitacion.reservada = True
                return True
        return False

# Ejercicio 10: Sistema de Reproducción de Música
class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

class PlayList:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
        self.actual = 0
    
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    
    def siguiente_cancion(self):
        if not self.canciones:
            return None
        self.actual = (self.actual + 1) % len(self.canciones)
        return self.canciones[self.actual]
    
    def cancion_actual(self):
        if not self.canciones:
            return None
        return self.canciones[self.actual]
