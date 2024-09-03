class Negocio(): #primaria
    def venta(self, pren, cant, pre):
        self.prenda = pren
        self.cantidad = cant
        self.precio = pre
        self.totalCamisas = 0
        self.totalVerde = 0
        self.totalNegro = 0

        if venta1 == "Camisa": 
            self.totalCamisas = Camisa.stock - self.cantidad  
            #aca puse Camisa.stock para referirme al atributo stock de la clase camisa pero no se como hacer 
            #para que pueda ser leido en esta clase, supongo que deberia hacer composicion pero trate y no me salio
            if Camisa.stock > 20:
                print(f"COMPRAR CAMISAS") 
                self.totalCamisas + 100
            else:
                pass    

        if venta1 == "Remera verde":
            self.totalVerde = Remera.colorVerde - self.cantidad
        elif venta1 == "Remera negra":
            self.totalNegro = Remera.colorNegro - self.cantidad
            if  Remera.colorVerde > Remera.colorNegro:
                print(f"Hay mas remeras verdes")
            elif Remera.colorVerde < Remera.colorNegro:
                print(f"Hay mas remeras negras")
   
    def mostrarDatos(self):
        print(f"Remeras: Verdes = {self.totalVerde} / Negras = {self.totalNegro} --- Camisas = {self.totalCamisas} --- Facturacion: ${(self.precio * self.cantidad)}")
    
class Ropa(): #secundaria de Negocio(Negocio tiene Ropa)/madre de Remera y Camisa
    def __init__(self, pre, pren) -> None:
        self.precio = pre
        self.prenda = pren

class Remera(Ropa): #hija de Ropa
    def __init__(self, pre, ver, neg) -> None:
        super().__init__(pre, ver, neg)
        self.precio = int(15000)
        self.colorVerde = ver
        self.colorNegro = neg
        self.colorVerde = int(100)
        self.colorNegro = int(100)
    #aviso que color hay mas (verdes/negras)

class Camisa(Ropa): #hija de Ropa
    def __init__(self, sto, pre) -> None:
        super().__init__(sto, pre)
        self.stock = int(100)
        self.precio = int(30000)
    #menos de 20 u, aviso y compra de 100 camisas
    
#VENTAS
#10 remeras verdes y 40 camisas
#50 camisas
#30 remeras negras
venta1 = Negocio()
venta1.venta("Remera verde", 10, 15000)
venta1.venta("Camisa", 40, 30000)
print(" NO ME SALIO :((( ")
venta1.mostrarDatos()