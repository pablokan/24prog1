from database import Database
from models import Usuario, Contenido, Alquiler
from datetime import datetime, timedelta

class PlataformaStreaming:
    def __init__(self):
        self.db = Database()
        self.lista_usuarios = self.cargarUsuarios()
        self.lista_contenidos = self.cargarContenidos()
        self.lista_alquileres = self.cargarAlquileres()

    def cargarUsuarios(self):
        return [Usuario(usuario[0], *usuario[1:]) for usuario in self.db.mostrarUsuarios()]

    def cargarContenidos(self):
        return [Contenido(*contenido) for contenido in self.db.mostrarContenidos()]

    def cargarAlquileres(self):
        alquileres_data = self.db.mostrarAlquileres()
        return [Alquiler(*alquiler) for alquiler in alquileres_data]

    def agregarContenido(self):
        titulo = input("Título: ")
        genero = input("Género: ")
        ano = int(input("Año: "))
        director = input("Director: ")
        protagonista = input("Protagonista: ")
        tipo_contenido = input("Tipo de contenido (documental, película, serie): ")
        contenido = Contenido(len(self.lista_contenidos) + 1, titulo, genero, ano, director, protagonista, tipo_contenido)
        self.lista_contenidos.append(contenido)
        self.db.agregarContenido(contenido)
        print("Contenido añadido correctamente.")

    def agregarUsuario(self):
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        email = input("Email: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        usuario = Usuario(len(self.lista_usuarios) + 1, nombre, dni, email, telefono, direccion)
        self.lista_usuarios.append(usuario)
        self.db.agregarUsuario(usuario)
        print("Usuario añadido correctamente.")

    def borrarUsuario(self):
        self.mostrarUsuarios()
        usuario_id = input("Ingrese el DNI del usuario a borrar: ")
        usuario_a_borrar = next((usuario for usuario in self.lista_usuarios if usuario.dni == usuario_id), None)
        
        if usuario_a_borrar:
            self.lista_usuarios.remove(usuario_a_borrar)
            self.db.borrarUsuario(usuario_id)
            print("Usuario borrado correctamente.")
        else:
            print("DNI de usuario no válido.")

    def borrarContenido(self):
        self.mostrarContenidos()
        contenido_id = input("Ingrese el título del contenido a borrar: ")

        contenido_a_borrar = next((contenido for contenido in self.lista_contenidos if contenido.titulo == contenido_id), None)
        if contenido_a_borrar:
            self.lista_contenidos.remove(contenido_a_borrar)
            self.db.borrarContenido(contenido_id)
            print("Contenido borrado correctamente.")
        else:
            print("Título de contenido no válido.")

    def alquilarContenido(self):
        usuario_id = input("ID del usuario: ")
        contenido_id = input("ID del contenido: ")

        usuario_a_alquilar = next((usuario for usuario in self.lista_usuarios if usuario.id == int(usuario_id)), None)
        contenido_a_alquilar = next((contenido for contenido in self.lista_contenidos if contenido.id == int(contenido_id)), None)

        if usuario_a_alquilar and contenido_a_alquilar:
            print(f"Datos del usuario: {usuario_a_alquilar.nombre}, DNI: {usuario_a_alquilar.dni}, Email: {usuario_a_alquilar.email}")
            print(f"Datos del contenido: {contenido_a_alquilar.titulo}, Género: {contenido_a_alquilar.genero}")

            dias = int(input("Cantidad de días a alquilar: "))
            tipo_precio = self.db.obtenerPrecioPorTipo(contenido_a_alquilar.tipo_contenido)
            total_importe = tipo_precio * dias
            
            if tipo_precio > 0:
                alquiler = Alquiler(len(self.lista_alquileres) + 1, usuario_id, contenido_id, dias, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), (datetime.now() + timedelta(days=dias)).strftime('%Y-%m-%d %H:%M:%S'), total_importe)
                self.lista_alquileres.append(alquiler)
                self.db.alquilarContenido(usuario_id, contenido_id, dias, total_importe)
                print(f"Alquiler registrado correctamente. Total a pagar: ${total_importe}.")
            else:
                print("El tipo de contenido no es válido.")
        else:
            if not usuario_a_alquilar:
                print("El usuario no existe.")
            if not contenido_a_alquilar:
                print("El contenido no existe.")

    def devolverContenido(self):
        self.mostrarAlquileres()
        alquiler_id = int(input("Ingrese el ID del alquiler a devolver: ")) - 1
        if 0 <= alquiler_id < len(self.lista_alquileres):
            alquiler = self.lista_alquileres[alquiler_id]
            print(f"Devolviendo alquiler con ID: {alquiler.id}")
            self.db.devolverContenido(alquiler.id)  
            del self.lista_alquileres[alquiler_id]  
            print("Contenido devuelto correctamente.")
        else:
            print("ID de alquiler no válido.")

    def mostrarAlquileres(self):
        alquileres = self.lista_alquileres
        if alquileres:
            print("\n--- Lista de Alquileres ---")
            for idx, alquiler in enumerate(alquileres):
                print(f"ID: {idx + 1}, Usuario ID: {alquiler.usuario_id}, Contenido ID: {alquiler.contenido_id}, Días: {alquiler.dias}, Fecha de Alquiler: {alquiler.fecha_alquiler}, Fecha de Devolución: {alquiler.fecha_devolucion}")
        else:
            print("No hay alquileres registrados.")

    def mostrarUsuarios(self):
        if self.lista_usuarios:
            print("\n--- Lista de Usuarios ---")
            for idx, usuario in enumerate(self.lista_usuarios):
                print(f"ID: {idx + 1}, Nombre: {usuario.nombre}, DNI: {usuario.dni}, Email: {usuario.email}, Telefono: {usuario.telefono}, Direccion: {usuario.direccion}")
        else:
            print("No hay usuarios registrados.")

    def mostrarContenidos(self):
        if self.lista_contenidos:
            print("\n--- Lista de Contenidos ---")
            for contenido in self.lista_contenidos:
                print(f"ID: {contenido.id}, Título: {contenido.titulo}, Género: {contenido.genero}, Año: {contenido.ano}, Director: {contenido.director}, Protagonista: {contenido.protagonista}, Tipo: {contenido.tipo_contenido}")
        else:
            print("No hay contenidos disponibles.")

    def mostrarMenu(self):
        seguir = True
        while seguir:
            print("\n--- Menú Principal ---")
            print("1. Usuarios")
            print("2. Contenidos")
            print("3. Alquileres")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.mostrarMenuUsuarios()
            elif opcion == '2':
                self.mostrarMenuContenidos()
            elif opcion == '3':
                self.mostrarMenuAlquileres()
            elif opcion == '4':
                seguir = False
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def mostrarMenuUsuarios(self):
        seguir = True
        while seguir:
            print("\n--- Menú Usuarios ---")
            print("1. Añadir usuario")
            print("2. Borrar usuario")
            print("3. Mostrar usuarios")
            print("4. Volver")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.agregarUsuario()
            elif opcion == '2':
                self.borrarUsuario()
            elif opcion == '3':
                self.mostrarUsuarios()
            elif opcion == '4':
                seguir = False
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def mostrarMenuContenidos(self):
        seguir = True
        while seguir:
            print("\n--- Menú Contenidos ---")
            print("1. Añadir contenido")
            print("2. Borrar contenido")
            print("3. Mostrar contenidos")
            print("4. Volver")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.agregarContenido()
            elif opcion == '2':
                self.borrarContenido()
            elif opcion == '3':
                self.mostrarContenidos()
            elif opcion == '4':
                seguir = False
            else:
                print("Opción no válida. Inténtalo de nuevo.")

    def mostrarMenuAlquileres(self):
        seguir = True
        while seguir:
            print("\n--- Menú Alquileres ---")
            print("1. Alquilar contenido")
            print("2. Devolver alquiler")
            print("3. Mostrar alquileres")
            print("4. Volver")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.alquilarContenido()
            elif opcion == '2':
                self.devolverContenido()
            elif opcion == '3':
                self.mostrarAlquileres()
            elif opcion == '4':
                seguir = False
            else:
                print("Opción no válida. Inténtalo de nuevo.")
