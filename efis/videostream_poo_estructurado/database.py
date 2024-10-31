import sqlite3
from datetime import datetime, timedelta

class Database:
    def __init__(self, db_name='videostream.db'):
        self.db_name = db_name
        self.precios = {'Documental': 5, 'Película': 8, 'Serie': 10}

    def agregarUsuario(self, usuario):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, dni, email, telefono, direccion) VALUES (?, ?, ?, ?, ?)", 
                           (usuario.nombre, usuario.dni, usuario.email, usuario.telefono, usuario.direccion))
            conexion.commit()

    def agregarContenido(self, contenido):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO contenido (titulo, genero, ano, director, protagonista, tipo_contenido) VALUES (?, ?, ?, ?, ?, ?)", 
                           (contenido.titulo, contenido.genero, contenido.ano, contenido.director, contenido.protagonista, contenido.tipo_contenido))
            conexion.commit()

    def mostrarUsuarios(self):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()

    def mostrarContenidos(self):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM contenido")
            return cursor.fetchall()

    def mostrarAlquileres(self):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alquileres")
            return cursor.fetchall()

    def borrarUsuario(self, usuario_id):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE dni=?", (usuario_id,))
            conexion.commit()

    def borrarContenido(self, contenido_id):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM contenido WHERE titulo=?", (contenido_id,))
            conexion.commit()

    def alquilarContenido(self, usuario_id, contenido_id, dias, total_importe):
        fecha_alquiler = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fecha_devolucion = (datetime.now() + timedelta(days=dias)).strftime('%Y-%m-%d %H:%M:%S')
        alquilado = True
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO alquileres (usuario_id, contenido_id, fecha_alquiler, fecha_devolucion, importe, alquilado) VALUES (?, ?, ?, ?, ?, ?)", 
                           (usuario_id, contenido_id, fecha_alquiler, fecha_devolucion, total_importe, alquilado))
            conexion.commit()

    def obtenerPrecioPorTipo(self, tipo_contenido):
        return self.precios.get(tipo_contenido, 0)

    def devolverContenido(self, alquiler_id):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM alquileres WHERE id=?", (alquiler_id,))
            conexion.commit()
