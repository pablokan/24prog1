# Clase mascota con atributos nombre y edad
class Mascota:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def estado_animo(self):
        pass

# Clase perro con atributos nombre, edad, raza, color de collar y material de collar
class Perro(Mascota):
    def __init__(self,nombre,edad,raza,color_c,material_c):
        super().__init__(nombre,edad)
        self.raza = raza
        self.color_c = color_c
        self.material_c = material_c
    # Metodo que define el atributo animo segun si mueve la cola o no    
    def estado_animo(self):
        valido = False
        while not valido:
            mover = input("Ingrese si el perro mueve la cola (si/no): ")
            if mover.lower().strip() == "si":
                self.animo = "feliz"
                valido = True
                break
            elif mover.lower().strip() == "no":
                self.animo = "triste"
                valido = True
                break
            print("Intente de nuevo")

# Clase Gato con atributos nombre, edad, sexo y color
class Gato(Mascota):
    def __init__(self,nombre,edad,sexo,color):
        super().__init__(nombre,edad)
        self.sexo = sexo
        self.color = color
    # Metodo que define atributo animo segun si maulla o no        
    def estado_animo(self):
        valido = False
        while not valido:
            maullido = input("Ingrese si el gato maulla (si/no): ")
            if maullido.lower().strip() == "si":
                self.animo = "tiene hambre"
                valido = True
                break
            elif maullido.lower().strip() == "no":
                self.animo = "no tiene hambre"
                valido = True
                break
            print("Intente de nuevo")

# Clase principal 
class Aplicacion:
    # Lista de mascotas
    def __init__(self):
        self.lista_perros = []
        self.lista_gatos = []
    # Metodo que permite agregar un perro         
    def agregar_perro(self):
        # Pedir datos
        print("Ingrese los datos del perro")
        nombre = input("Nombre: ")
        edad = input("Edad")
        raza = input("Raza: ")
        color = input("Color del collar: ")
        material = input("Material del collar: ")
        # Crear perro y agregar a la lista 
        perro = Perro(nombre,edad,raza,color,material)
        perro.estado_animo()
        self.lista_perros.append(perro)
    # Metodo que permite agregar un gato
    def agregar_gato(self):
        # Pedir datos
        print("Ingrese los datos del gato")        
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        sexo = input("Sexo: ")
        color = input("Color: ")
        gato = Gato(nombre,edad,sexo,color)
        gato.estado_animo()
        self.lista_gatos.append(gato)
    def mostrar_mascotas(self):
        print("Informacion sobre las mascotas")
        for perro in self.lista_perros:
            print(f"{perro.nombre} tiene {perro.edad} años,", end =" ")
            print(f"es un {perro.raza} que lleva un collar {perro.color_c} de {perro.material_c} y está {perro.animo}.")
        for gato in self.lista_gatos:
            print(f"{gato.nombre} tiene {gato.edad} años, es {gato.sexo} y {gato.animo}.")

programa = Aplicacion()
for i in range(2):
    programa.agregar_perro()
    programa.agregar_gato()
programa.mostrar_mascotas()
