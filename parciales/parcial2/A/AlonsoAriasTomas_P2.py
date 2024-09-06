# Se crea una plataforma de música tipo Spotify.
# Se dispone de los siguientes datos (Listas iniciales posibles):
# bandas = [
# ["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
# ["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
# ["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]
# ]
# solistas = [
# ["Peter Gabriel", 10, 17_319_533,70], 
# ["Jeff Beck", 3, 1_023_998, 76]
# ]
# Cada sublista contiene: nombre, cantidad de álbumes y cantidad de reproducciones. El cuarto dato son los integrantes en el caso de las bandas y la edad en el caso de los solistas.
# Pueden desarmar y rearmar estas listas como les resulte más cómodo.
# Importante: Las estructuras con los datos iniciales (listas, diccionarios o cualquier combinación de almacenamiento, sean las propuestas aquí o las construidas por ustedes) solamente pueden usarse para la instanciación de las bandas y los solistas. NO para la algoritmia posterior que debe trabajar sobre los objetos.
# Necesitamos saber:
# La suma total de reproducciones de todos (bandas y solistas, un solo total final).
# El apellido del solista más viejo.
# Los nombres de los cantantes de las bandas.
# El nombre de la banda o el solista con mayor cantidad de álbumes.
# Realizar al menos un método para cada uno de los puntos pedidos.

class Artista():
    def __init__(self, nombre, cant_de_albunes, cant_de_reproducciones) -> None:
        self.nombre = nombre
        self.cant_de_albunes= cant_de_albunes
        self.cant_de_reproducciones=cant_de_reproducciones

class Banda(Artista):
    def __init__(self, nombre, cant_de_albunes, cant_de_reproducciones, integrantes) -> None:
        super().__init__(nombre, cant_de_albunes, cant_de_reproducciones)
        self.integrantes= integrantes

class Solista(Artista):
    def __init__(self, nombre, cant_de_albunes, cant_de_reproducciones, edad) -> None:
        super().__init__(nombre, cant_de_albunes, cant_de_reproducciones)
        self.edad = edad

class Spotify():
    def __init__(self) -> None:
        self.bandas = [
        ["Led Zeppelin", 9, 123456, "Jimmy Page, Robert Plant (voz), John Bonham, John Paul Jones"],
        ["Rage Against the Machine", 4, 243490, "Zack de la Rocha(voz), Tom Morello, Tim Commerford"],
        ["Seru Giran", 5, 32419, "Pedro Aznar, Oscar Moro, David Lebón (voz), Charly García (voz)"]]
        self.solistas = [["Peter Gabriel", 10, 17_319_533,70], 
        ["Jeff Beck", 3, 1_023_998, 76]]
    
    def agregar_banda(self,tipo):
        nombre = input("Nombre")
        cant_albunes = int(input("Cantidad de albunes: "))
        cant_reproducciones =  float(input("Cantidad de reproducciones: "))
        if tipo == "Banda":
            integrantes = input("Ingresa los integrandes")
            banda = Banda(nombre,cant_albunes,cant_reproducciones,integrantes)
            self.bandas.append(banda)
        elif tipo == "Solista":
            edad = int(input("Edad: "))
            solista = Solista(nombre,cant_albunes,cant_reproducciones,edad)
            self.solistas.append(solista)
    """     
    def solista_mas_viejo(self):
        edad = 0
        solista_mas_viejo = ""
        if Solista().edad > edad:
            Solista().nombre = solista_mas_viejo
        return solista_mas_viejo
       """
    
    def solista_mas_viejo(self):
        nombre_del_mas_viejo = ""
        edad_mas_viejo = 0
        for x in range(len(self.solistas)):
            if self.solistas[x][3] > edad_mas_viejo:
                edad_mas_viejo = self.solistas[x][3]
                nombre_del_mas_viejo = self.solistas[x][0]
        return nombre_del_mas_viejo


    def total_reproducciones_plataforma(self):
        total_reproducciones = 0
        total_reproducciones = total_reproducciones + Solista().cant_de_reproducciones + Banda().cant_de_reproducciones
        return total_reproducciones


    
    def total_de_reproducciones(self):
        total = 0
        for x in range(len(self.bandas)):
            total = total + self.bandas[x][2]
        for x in range(len(self.solistas)):
            total = total + self.solistas[x][2]
        return total
    

    def nombre_cantante_de_la_banda(slef):
        pass
    
    def mayor_cant_albunes(self):
        nombre = ""
        cantidad = 0
        for x in range(len(self.bandas)):
            if self.bandas[x][1] > cantidad:
                nombre = self.bandas[x][0]
        for x in range(len(self.solistas)):
            if self.solistas[x][1] > cantidad:
                nombre = self.solistas[x][0]
        return nombre
    
    """
    def mayor_cant_abunes(self):
        nombre = ""
        cantidad = 0
        for albunes in Banda().cant_de_albunes:
            if albunes > cantidad:
                nombre = Banda().nombre
        for albunes in Solista().cant_de_albunes:
            if albunes > cantidad:
                nombre = Solista().nombre
        return nombre
    """
    def mostrar_datos(slef):
        print(f"El sitio tiene: {slef.total_de_reproducciones()} reproducciones")
        print(f"El solista mas viejo es: {slef.solista_mas_viejo()}")    
        print(".")
        print(f"El artista con mayor cantidad de albunes es: {slef.mayor_cant_albunes()}")

prueba = Spotify()
prueba.mostrar_datos()