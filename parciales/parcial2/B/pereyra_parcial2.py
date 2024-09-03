class Mascota(): 
    def __init__(self, n, e): 
        self.nombre=n #Atributo para ingresar nombre de la mascota
        self.edad=e #Atributo para ingresar la edad de la mascota
        
class Perro(Mascota):
    def __init__(self, n, e, r, cc, mc): 
        super().__init__(n, e)
        self.raza=r     #Atributo para ingresar raza del perro
        self.colorCollar=cc     #Atributo para ingresar el color del collar
        self.materialCollar=mc  #Atributo para ingresar el material del collar
        
    def estadoPerro(self):  #Metodo que devuelve si el perro esta contento o no
        accion=input(f"{self.nombre} mueve rapido la cola?(si/no): ")  #Variable para ingresar la condicion del if, no lleva el self por ser variable local
        if accion=="si": #"Si el perro mueve la cola"
            self.estado="está contento"
        else:#"No mueve la cola"
            self.estado="está triste"
      
    def mostrarDatos(self): #Metodo que muestra toda la informacion ingresada
        print(f"{self.nombre} tiene {self.edad} años, es un {self.raza} que lleva un collar {self.colorCollar} de {self.materialCollar} y {self.estado}")    
        
class Gato(Mascota):
    def __init__(self, n, e, co, s):
        super().__init__(n, e)
        self.color=co #Atributo para ingresar el color del pelaje del gato
        self.sexo=s #Atributo para ingresar el sexo del gato
        if self.sexo=="m": #Si el sexo es masculino
            self.sexo="un gato"
        elif self.sexo=="f": #Femenino
            self.sexo="una gata"
        
    def estadoGato(self): #Metodo para devolver si el gato tiene hambre o no
        accion=input(f"{self.nombre} maulla?(si/no): ") #variable local, que sera la condicion del if
        if accion=="si": #Si el gato/a maulla
            self.estado="tiene hambre"
        else:
            self.estado="no tiene hambre"
        
    def mostrarDatos(self):
        print(f"{self.nombre} tiene {self.edad} años, es {self.sexo} {self.color} y {self.estado}")

class Familia():
    
    perro1=Perro("Bobby", 3, "Rottweiler", "Rojo", "Cuero")
    perro1.estadoPerro()#No
    
    perro2=Perro("Toffe", 5, "Ovejero Aleman", "Negro", "Tela")
    perro2.estadoPerro()#Si
    
    gato1=Gato("Grisina", 4, "Gris", "f")
    gato1.estadoGato()#No
    
    gato2=Gato("Shevek", 1, "Naranja", "m")
    gato2.estadoGato()#si
    #Mostrar informacion de las mascotas
    perro1.mostrarDatos()
    perro2.mostrarDatos()
    gato1.mostrarDatos()
    gato2.mostrarDatos()
    
    
    #Grisina tiene 4 años, es una gata gris y no tiene hambre.
    #Shevek tiene 1 año, es un gato naranja y tiene hambre.


