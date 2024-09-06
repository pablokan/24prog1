class Bandas:
    def __init__(self,nombre,cantidad_albunes,cantidad_repro,integrantes) -> None:
        self.nombre=nombre
        self.cantidad_albunes=cantidad_albunes
        self.cantidad_repro=cantidad_repro
        self.integrantes=integrantes
    def nombre_cantantes_bandas(self):
        print(" Robert Plant","Zack de la Rocha","David Lebón","Charly García")


class Solistas(Bandas):
    def __init__(self,nombre,cantidad_albunes, cantidad_repro, edad ) -> None:
        super().__init__(self,nombre, cantidad_albunes,cantidad_repro)
        self.edad=edad

    def Solista_mas_viejo (self):
        lista_solistas =("Peter Gabriel",70,"Jeff Beck", 76)
        numero_grande = None
        for i in range(0, len(lista_solistas), 2):nombre = lista_solistas[i]
        numero = lista_solistas[i + 1]
        if numero_grande is None:
            numero_grande = numero
            nombre_max = nombre
        elif numero > numero_grande:
            numero_grande = numero
            nombre_max = nombre
        print(nombre_max)
class Plataforma:
    def __init__(self,nombre) -> None:
            self.nombre=nombre

    def Total_repro (self):
        lista_repro=[123456,243490,32419,17319533,1023998]
        suma=sum(lista_repro)
        print (f"total de reproducciones del sitio:{suma}")
      

    def nombre_mayor_cantidad_de_albunes(self):
            print=(f"El nombre de la banda o el solista con mayor cantidad de álbumes es:{cantante1}")

    def mostrar_todo(self):
         plataforma.Total_repro
         plataforma.Solista_mas_viejo  
         plataforma.nombre_cantantes_bandas
         plataforma.nombre_mayor_cantidad_de_albunes  
        
plataforma=Plataforma("SPOTY")

plataforma.mostrar_todo()






